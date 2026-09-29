"""Public synthetic force-trace challenge. Standard library only.

Arbitrary teaching data, not hardware measurements or settings.
No untrusted code execution, network calls, or private-repository access.
"""
import csv
import math
from pathlib import Path
import statistics
import sys

MAX_BYTES = 1_000_000
MAX_ROWS = 10_000


def summarize(path):
    source = Path(path)
    if source.stat().st_size > MAX_BYTES:
        raise ValueError("Synthetic CSV exceeds 1 MB limit")
    csv.field_size_limit(10_000)
    with source.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        required = {"run", "step", "signal", "artifact_proxy"}
        if not reader.fieldnames or not required.issubset(reader.fieldnames):
            raise ValueError("Expected run, step, signal, artifact_proxy columns")
        groups = {}
        for count, row in enumerate(reader, 1):
            if count > MAX_ROWS:
                raise ValueError("Synthetic CSV exceeds row limit")
            name = row.get("run") or ""
            if not name or len(name) > 64:
                raise ValueError(f"Invalid run label on row {count}")
            try:
                signal = float(row["signal"])
                proxy_text = row.get("artifact_proxy")
                proxy = float(proxy_text) if proxy_text not in (None, "") else None
            except (TypeError, ValueError) as exc:
                raise ValueError(f"Non-numeric value on row {count}") from exc
            if not math.isfinite(signal) or (proxy is not None and not math.isfinite(proxy)):
                raise ValueError(f"Non-finite value on row {count}")
            groups.setdefault(name, []).append((signal, proxy))
    if not groups:
        raise ValueError("Synthetic CSV has no data")
    for name, group in sorted(groups.items()):
        signal = [s for s, _ in group]
        proxy = [p for _, p in group]
        if any(p is None for p in proxy):
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
    try:
        summarize(sys.argv[1] if len(sys.argv) > 1 else "challenge.csv")
    except (OSError, csv.Error, ValueError) as exc:
        print(f"Cannot analyze synthetic CSV: {exc}", file=sys.stderr)
        sys.exit(2)
