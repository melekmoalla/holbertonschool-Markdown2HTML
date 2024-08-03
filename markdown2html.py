#!/usr/bin/python3
"""markdown2html.py: A script that converts a Markdown file to an HTML file."""

import sys
import os


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: ./markdown2html.py README.md README.html", file=sys.stderr)
        exit(1)
    if not os.path.isfile(sys.argv[1]):
        print(f'Missing {sys.argv[1]}', file=sys.stderr)
        exit(1)
