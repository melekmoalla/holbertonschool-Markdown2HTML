#!/usr/bin/python3
"""
markdown2html module
"""

import sys
import os


def convert_heading(line):
    """
    Converts a Markdown heading to an HTML heading
    """
    heading_level = 0
    while heading_level < len(line) and line[heading_level] == '#':
        heading_level += 1
    if heading_level > 0 and heading_level <= 6:
        return f"<h{heading_level}>{line[heading_level:].strip()}</h{heading_level}>"
    return line


def convert_unordered_list(lines):
    """
    Converts Markdown unordered list to HTML unordered list
    """
    in_list = False
    html_lines = []
    for line in lines:
        if line.startswith('- '):
            if not in_list:
                html_lines.append("<ul>")
                in_list = True
            html_lines.append(f"<li>{line[2:].strip()}</li>")
        else:
            if in_list:
                html_lines.append("</ul>")
                in_list = False
            html_lines.append(line)
    if in_list:
        html_lines.append("</ul>")
    return html_lines


def convert_ordered_list(lines):
    """
    Converts Markdown ordered list to HTML ordered list
    """
    in_list = False
    html_lines = []
    for line in lines:
        if line.startswith('* '):
            if not in_list:
                html_lines.append("<ol>")
                in_list = True
            html_lines.append(f"<li>{line[2:].strip()}</li>")
        else:
            if in_list:
                html_lines.append("</ol>")
                in_list = False
            html_lines.append(line)
    if in_list:
        html_lines.append("</ol>")
    return html_lines


def convert_bold_and_emphasis(line):
    """
    Converts Markdown bold and emphasis to HTML tags
    """
    line = line.replace('**', '<b>', 1).replace('**', '</b>', 1)
    line = line.replace('__', '<em>', 1).replace('__', '</em>', 1)
    return line


def convert_paragraphs(lines):
    """
    Converts plain text to HTML paragraphs
    """
    html_lines = []
    in_paragraph = False
    paragraph_lines = []

    def close_paragraph():
        """
        Closes the current paragraph and adds it to the HTML lines
        """
        if paragraph_lines:
            html_lines.append("<p>")
            for i, pline in enumerate(paragraph_lines):
                if i > 0:
                    html_lines.append("<br/>")
                html_lines.append(convert_bold_and_emphasis(pline))
            html_lines.append("</p>")
            paragraph_lines.clear()

    for line in lines:
        stripped_line = line.strip()
        if stripped_line == '':
            close_paragraph()
            in_paragraph = False
        else:
            paragraph_lines.append(line.strip())
            in_paragraph = True

    close_paragraph()
    return html_lines


def main():
    """
    Main function that handles the conversion from Markdown to HTML
    """
    # Check the number of arguments
    if len(sys.argv) < 3:
        print("Usage: ./markdown2html.py README.md README.html", file=sys.stderr)
        sys.exit(1)

    # Get the input and output file names from the arguments
    input_file = sys.argv[1]
    output_file = sys.argv[2]

    # Check if the input file exists
    if not os.path.isfile(input_file):
        print(f"Missing {input_file}", file=sys.stderr)
        sys.exit(1)

    # Read the Markdown file
    with open(input_file, 'r') as f:
        markdown_content = f.readlines()

    # Convert Markdown to HTML
    html_lines = convert_ordered_list(markdown_content)
    html_lines = convert_unordered_list(html_lines)
    html_lines = [convert_heading(line) if not line.startswith(
        '- ') and not line.startswith('* ') else line for line in html_lines]
    html_lines = convert_paragraphs(html_lines)

    # Write the HTML content to the output file
    with open(output_file, 'w') as f:
        f.write("\n".join(html_lines))

    # Exit successfully
    sys.exit(0)


if __name__ == "__main__":
    main()
