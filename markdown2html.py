#!/usr/bin/python3
"""
markdown2html.py: A script that converts a Markdown file to an HTML file.
"""
import sys
import os
import markdown


def main():

    if (sys.argv) < 3:
        print("Usage: ./markdown2html.py README.md README.html")
        exit(1)
    if not os.path.isfile(sys.argv[1]):
        print(f'Missing {sys.argv[1]}', file=sys.stderr)
        exit(1)
    with open(sys.argv[1], 'r') as file:
        read_file = file.read()

    html_content = markdown.markdown(read_file)

    with open(sys.argv[2], 'w') as file_mark:
        file_mark.write(html_content)

    exit(0)


if __name__ == "__main__":
    main()
