#!/usr/bin/python3
"""
markdown2html.py: A script that converts a Markdown file to an HTML file.

Usage:
    ./markdown2html.py README.md README.html
"""
import sys
import os
import markdown


def main():
    """Main function to handle the Markdown to HTML conversion."""
    if len(sys.argv) != 3:
        print("Usage: ./markdown2html.py README.md README.html", file=sys.stderr)
        exit(1)

    md_filename = sys.argv[1]
    html_filename = sys.argv[2]

    if not os.path.isfile(md_filename):
        print(f"Missing {md_filename}", file=sys.stderr)
        exit(1)

    with open(md_filename, 'r') as md_file:
        md_content = md_file.read()

    html_content = markdown.markdown(md_content)

    with open(html_filename, 'w') as html_file:
        html_file.write(html_content)

    exit(0)


if __name__ == "__main__":
    main()
