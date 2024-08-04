#!/usr/bin/python3
"""
markdown2html module
"""

import sys
import os


def main():
    """
    Converts a Markdown heading to an HTML heading
    """

    if len(sys.argv) != 3:
        print("Usage: ./markdown2html.py README.md README.html", file=sys.stderr)
        sys.exit(1)

    if not os.path.isfile(sys.argv[1]):
        print(f'Missing {sys.argv[1]}', file=sys.stderr)
        sys.exit(1)

    with open(sys.argv[1], 'r') as f:
        content = f.readlines()

    html_lines = []
    for i in content:
        b = 0
        for a in i:
            if a == '#':
                b += 1
        if b > 0 and b <= 6:
            text = f"<h{b}>{i[b:].strip()}</h{b}>"
            # print(text)
            html_lines.append(text)

    with open(sys.argv[2], 'w') as f:
        f.write("\n".join(html_lines))

    sys.exit(0)


if __name__ == "__main__":
    main()
