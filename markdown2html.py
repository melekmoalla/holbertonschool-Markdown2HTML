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
    html_lines = [convert_heading(line) for line in markdown_content]

    # Write the HTML content to the output file
    with open(output_file, 'w') as f:
        f.write("\n".join(html_lines))

    # Exit successfully
    sys.exit(0)


if __name__ == "__main__":
    main()
