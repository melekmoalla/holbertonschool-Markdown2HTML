#!/usr/bin/python3
"""
markdown2html.py: A script that converts a Markdown file to an HTML file.

Usage:
    ./markdown2html.py README.md README.html
"""
import sys
import os


def main():

    if len(sys.argv) < 3:
        sys.stderr.write("Usage: ./markdown2html.py README.md README.\n")
        exit(1)
    if not os.path.isfile(sys.argv[1]):
        print(f'Missing {sys.argv[1]}', file=sys.stderr)
        exit(1)

    exit(0)


if __name__ == "__main__":
    main()
