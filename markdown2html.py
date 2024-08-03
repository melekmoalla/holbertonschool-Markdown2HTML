#!/usr/bin/python3
"""
markdown2html.py: A script that converts a Markdown file to an HTML file.

Usage:
    ./markdown2html.py README.md README.html

The script takes two arguments:
    - The name of the Markdown file to be converted.
    - The name of the output HTML file.

Requirements:
    - If the number of arguments is less than 2, print a usage message and exit with status 1.
    - If the Markdown file doesn’t exist, print a missing file message and exit with status 1.
    - Otherwise, convert the Markdown content to HTML and write it to the output file.
"""
import sys
import os
import markdown


def main():
    """Main function to handle the Markdown to HTML conversion."""
    if len(sys.argv) != 3:
        print("Usage: ./markdown2html.py README.md README.html", file=sys.stderr)
        exit(1)

    # Get the filenames from the arguments
    md_filename = sys.argv[1]
    html_filename = sys.argv[2]

    # Check if the Markdown file exists
    if not os.path.isfile(md_filename):
        print(f"Missing {md_filename}", file=sys.stderr)
        exit(1)

    # Read the content of the Markdown file
    try:
        with open(md_filename, 'r') as md_file:
            md_content = md_file.read()
    except IOError as e:
        print(f"Error reading {md_filename}: {e}", file=sys.stderr)
        exit(1)

    # Convert the Markdown content to HTML
    html_content = markdown.markdown(md_content)

    # Write the HTML content to the output file
    try:
        with open(html_filename, 'w') as html_file:
            html_file.write(html_content)
    except IOError as e:
        print(f"Error writing to {html_filename}: {e}", file=sys.stderr)
        exit(1)

    # Exit with status 0 indicating success
    exit(0)


# Ensure the script does not execute when imported
if __name__ == "__main__":
    main()
