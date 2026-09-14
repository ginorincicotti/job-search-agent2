#!/usr/bin/env python3
"""
Placeholder job_search runner

This script is a minimal, safe placeholder so the workflow can run.
It checks for EMAIL_USER / EMAIL_PASS (without printing them), makes a
simple HTTP request to demonstrate network access, and exits with code 0.

Replace this with your real job search logic.
"""

import os
import sys

import requests


def main():
    user = os.getenv("EMAIL_USER")
    pw = os.getenv("EMAIL_PASS")

    print("Starting job_search.py placeholder")
    print(f"EMAIL_USER set: {bool(user)}")

    # Example network call to verify dependencies and connectivity.
    try:
        resp = requests.get("https://httpbin.org/get", timeout=10)
        print("Sample request status:", resp.status_code)
    except Exception as e:
        print("Sample request failed:", e, file=sys.stderr)
        # Don't fail the workflow for a placeholder; return non-error code
        return 0

    print("Job search placeholder ran successfully.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
