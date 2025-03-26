import os
import subprocess
import argparse

def main():
    # Set up argument parser
    parser = argparse.ArgumentParser(description='Convert EPUB files to Markdown or plain text.')
    parser.add_argument('--md', action='store_true', help='Output in Markdown format')
    parser.add_argument('--txt', action='store_true', help='Output in plain text format')
    parser.add_argument('--input', default='input', help='Input directory containing EPUB files')
    parser.add_argument('--output', default='output', help='Output directory for converted files')

    args = parser.parse_args()

    # Determine which script to run
    if args.txt:
        script = 'epub_to_txt.py'
    else:
        script = 'epub_to_md.py'  # default to markdown

    # Run the selected script with the same arguments
    cmd = f"python {script} --input {args.input} --output {args.output}"
    subprocess.run(cmd, shell=True)

if __name__ == "__main__":
    main()
