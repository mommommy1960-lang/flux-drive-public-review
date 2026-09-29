"""Update a public GitHub issue with reviewed, opt-in challenge contributions.

Participation accounting only, not a measure of propulsion or scientific truth.
Only maintainers can add the reviewed-entry or validated-counterexample labels.
"""
import json
import os
import urllib.request

REPO = "mommommy1960-lang/flux-drive-public-review"
API = "https://api.github.com"
BOARD_MARKER = "FLUX_SYNTHETIC_CONTRIBUTION_BOARD"


def request(path, data=None, method=None):
    req = urllib.request.Request(
        API + path,
        data=json.dumps(data).encode() if data is not None else None,
        method=method,
        headers={
            "Authorization": "Bearer " + os.environ["GH_TOKEN"],
            "Accept": "application/vnd.github+json",
            "X-GitHub-Api-Version": "2022-11-28",
            "User-Agent": "flux-synthetic-contribution-board",
            "Content-Type": "application/json",
        },
    )
    with urllib.request.urlopen(req, timeout=30) as response:
        return json.load(response)


def issues():
    page = 1
    while True:
        batch = request(f"/repos/{REPO}/issues?state=all&per_page=100&page={page}")
        yield from batch
        if len(batch) < 100:
            return
        page += 1


def opt_in(body):
    if "**Public credit:**" not in body:
        return False
    answer = body.split("**Public credit:**", 1)[1].strip().splitlines()
    return bool(answer) and answer[0].strip().lower() == "yes"


def eligible(issue):
    """No unreviewed issue is promoted to the public board."""
    if "pull_request" in issue or not issue["title"].startswith("[Challenge]"):
        return False
    labels = {x["name"] for x in issue.get("labels", [])}
    return "reviewed-entry" in labels and opt_in(issue.get("body") or "")


def main():
    all_issues = list(issues())
    board = next((i for i in all_issues if BOARD_MARKER in (i.get("body") or "")), None)
    if board is None:
        board = request(f"/repos/{REPO}/issues", {"title": "Synthetic challenge contribution board", "body": BOARD_MARKER})
    rows = []
    for issue in all_issues:
        if not eligible(issue):
            continue
        labels = {x["name"] for x in issue.get("labels", [])}
        status = "Validated critique" if "validated-counterexample" in labels else "Reviewed entry; reproduction pending"
        login = issue["user"]["login"]
        number = issue["number"]
        rows.append((status == "Validated critique", number, login, status))
    rows.sort(key=lambda r: (-int(r[0]), r[1]))
    table = "\n".join(
        f"| [@{login}](https://github.com/{login}) | [#{number}](https://github.com/{REPO}/issues/{number}) | {status} |"
        for _, number, login, status in rows
    ) or "| — | — | No reviewed opt-in submissions yet |"
    content = (
        f"{BOARD_MARKER}\n\n# Synthetic challenge contribution board\n\n"
        "This board credits reviewed, opt-in participants in a fictional data exercise, **not propulsion or flight**. "
        "Maintainers add `reviewed-entry` after checking for personal data, confidential material, unsafe instructions and spam. "
        "A maintainer adds `validated-counterexample` only after independently reproducing a critique. "
        "Issue authors can remove public credit by changing their opt-in answer to no; GitHub's underlying issue history may remain public. "
        "A physical claim needs a separate calibrated experiment and independent replication.\n\n"
        "| Contributor | Submission | Review status |\n|---|---|---|\n"
        f"{table}\n"
    )
    if (board.get("body") or "") != content:
        request(f"/repos/{REPO}/issues/{board['number']}", {"body": content}, method="PATCH")
        print(f"Updated board issue #{board['number']} with {len(rows)} reviewed opt-in submissions")
    else:
        print("Board already current")


if __name__ == "__main__":
    main()
