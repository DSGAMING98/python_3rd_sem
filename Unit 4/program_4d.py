"""Program 4D: Analyze structured application logs stored in JSON."""

import json
from collections import Counter
from pathlib import Path

path = Path(__file__).with_name("sample_logs.json")

try:
    logs = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(logs, list):
        raise ValueError("Logs must be a list")

    counts = Counter()
    print("JSON LOG ANALYZER")
    for item in logs:
        level = item["level"].upper()
        message = item["message"]
        print(f"[{level}] {message}")
        counts[level] += 1

    print("LOG SUMMARY")
    for level in ("INFO", "WARNING", "ERROR"):
        print(f"{level}: {counts[level]}")
    print("Total:", len(logs))
except (OSError, ValueError, KeyError, TypeError, json.JSONDecodeError) as error:
    print("Unable to analyze log:", error)
