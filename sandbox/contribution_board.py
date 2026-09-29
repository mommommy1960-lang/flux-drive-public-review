"""Update a public GitHub issue with opt-in challenge contributions.

This is participation accounting, not a measure of propulsion or scientific truth.
Only maintainers can award a validated finding by applying the named label.
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


def main():
    all_issues = list(issues())
    board = next((i for i in all_issues if BOARD_MARKER in (i.get("body") or "")), None)
    if board is None:
        board = request(f"/repos/{REPO}/issues", {"title": "Synthetic challenge contribution board", "body": BOARD_MARKER})
    rows = []
    for issue in all_issues:
        if "pull_request" in issue or not issue["title"].startswith("[Challenge]"):
            continue
        body = issue.get("body") or ""
        if not opt_in(body):
            continue
        labels = {x["name"] for x in issue.get("labels", [])}
        status = "Validated critique" if "validated-counterexample" in labels else "Awaiting reproduction"
        login = issue["user"]["login"]
        number = issue["number"]
        rows.append((status == "Validated critique", number, login, status))
    rows.sort(key=lambda r: (-int(r[0]), r[1]))
    table = "\n".join(
        f"| [@{login}](https://github.com/{login}) | [#{number}](https://github.com/{REPO}/issues/{number}) | {status} |"
        for _, number, login, status in rows
    ) or "| — | — | No opt-in submissions yet |"
    content = (
        f"{BOARD_MARKER}\n\n# Synthetic challenge contribution board\n\n"
        "This board credits opt-in participants. It measures contributions to finding weaknesses in a fictional data exercise, **not propulsion or flight**. "
        "A maintainer adds `validated-counterexample` only after independently reproducing a critique. "
        "A reported physical effect needs a separate calibrated experiment and independent replication.\n\n"
        "| Contributor | Submission | Review status |\n|---|---|---|\n"
        f"{table}\n"
    )
    if (board.get("body") or "") != content:
        request(f"/repos/{REPO}/issues/{board['number']}", {"body": content}, method="PATCH")
        print(f"Updated board issue #{board['number']} with {len(rows)} opt-in submissions")
    else:
        print("Board already current")


if __name__ == "__main__":
    main()
