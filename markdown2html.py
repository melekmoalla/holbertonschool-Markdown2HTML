

if __name__ == '__main__':
    import sys
    import os
    if (sys.argv) < 3:
        print("Usage: ./markdown2html.py README.md README.html")
        sys.exit(1)
    if not os.path.isfile(sys.argv[1]):
        print(f'Missing {sys.argv[1]}', file=sys.stderr)
        sys.exit(1)
    else:
        sys.exit(0)