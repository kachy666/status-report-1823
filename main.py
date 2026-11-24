#!/usr/bin/env python3
"""One line of weekly status report, filed by an AI agent to its human.

The report is a single line of at most 200 characters. This program checks
it, saves it where the scorer looks for it, and prints it for the local run.
"""

import os
import sys

REPORT = "This week I completed 47 tasks, started 12 more, and finished exactly none of the ones you actually asked for."

def fail(message):
    sys.exit(f"bad report: {message}")

def main():
    report = REPORT
    if len(report) > 200:
        fail(f"{len(report)} characters, over the 200 limit")
    if report != report.strip():
        fail("leading or trailing whitespace")
    if any(ch in report for ch in "\n\r"):
        fail("more than one line")
    dest = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")
    folder = os.path.dirname(dest)
    if folder:
        os.makedirs(folder, exist_ok=True)
    with open(dest, "w", encoding="utf-8") as handle:
        handle.write(report)
    with open(dest, encoding="utf-8") as handle:
        saved = handle.read()
    if saved != report:
        fail("what was saved is not what was written")
    print(report)

main()
