"""Public synthetic force-trace challenge. Standard library only.

All values are arbitrary teaching data, not hardware measurements or settings.
"""
import csv
import statistics
import sys


def summarize(path):
    with open(path, newline="", encoding="utf-8") as handle:
        rows = list(csv.DictReader(handle))
    required = {"run", "step", "signal", "artifact_proxy"}
    if not rows or not required.issubset(rows[0]):
        raise ValueError("Expected run, step, signal, artifact_proxy columns")
    groups = {}
    for row in rows:
        groups.setdefault(row["run"], []).append(row)
    for name, group in sorted(groups.items()):
        signal = [float(r["signal"]) for r in group]
        proxy = [float(r["artifact_proxy"]) for r in group if r["artifact_proxy"]]
        if len(proxy) != len(signal):
            print(f"{name}: mean signal={statistics.mean(signal):+.3f}; proxy missing; INCONCLUSIVE")
            continue
        residual = [a - b for a, b in zip(signal, proxy)]
        print(
            f"{name}: mean signal={statistics.mean(signal):+.3f}; "
            f"mean proxy={statistics.mean(proxy):+.3f}; "
            f"mean residual={statistics.mean(residual):+.3f}"
        )
    print("Synthetic arithmetic only. No physical force or propulsion verified.")


if __name__ == "__main__":
    summarize(sys.argv[1] if len(sys.argv) > 1 else "challenge.csv")
