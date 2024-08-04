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
    ##
    line_html=[]
    m = 0
    for line in content:
        if line[0] == '-' :
            if m == 0:
                m = 1
                line_html.append('<ul>')
            line_html.append(f"<li>{line[2:].strip()}</li>")
        else:
            if m == 1:
                m = 0
                line_html.append("</ul>")
            line_html.append(line)
    if m == 1:
        line_html.append("</ul>")
        
    ##
    html_lines = []
    print(line_html)
    for i in line_html:
        if i[0] == '#':
            b = 0
            for a in i:
                if a == '#':
                    b += 1
            if b > 0 and b <= 6:
                text = f"<h{b}>{i[b:].strip()}</h{b}>"
                # print(text)
                html_lines.append(text)
        else:
            html_lines.append(i)

    with open(sys.argv[2], 'w') as f:
        f.write("\n".join(html_lines))

    sys.exit(0)


if __name__ == "__main__":
    main()
