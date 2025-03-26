# EPUB Converter

This Python toolset converts EPUB files to either Markdown or plain text format, making them suitable for use with Large Language Models (LLMs).

## Features

- Flexible output formats: Convert to Markdown (default) or plain text
- Batch processing: Converts all EPUB files in a specified input directory
- Progress indicator: Uses `tqdm` to display a progress bar during conversion
- LLM-friendly output: Extracts text content from EPUB files

## Requirements

- Python 3.6 or higher
- `ebooklib`
- `beautifulsoup4`
- `tqdm`

## Installation

1. Install the required libraries:

```bash
pip install EbookLib beautifulsoup4 tqdm
```

## Usage

1. Place your EPUB files in an input directory (default: `input/`)
2. Run the main converter script:

```bash
python epub_convert.py [options]
```

### Options:

- `--md`: Output in Markdown format (default)
- `--txt`: Output in plain text format
- `--input`: Specify input directory (default: 'input')
- `--output`: Specify output directory (default: 'output')

### Examples:

```bash
# Convert to Markdown (default)
python epub_convert.py

# Convert to plain text
python epub_convert.py --txt

# Custom input/output directories
python epub_convert.py --input my_epubs --output my_markdowns
```

## Example

For an EPUB file named `example.epub` in the input directory, the script will generate:

- `example.md` when using Markdown output (default)
- `example.txt` when using `--txt` flag

## Notes

- The script extracts the text content from the EPUB files
- The script attempts to extract the book title from the EPUB metadata. If unavailable, it uses the EPUB filename
- Output files will be named `[title].md` or `[title].txt` based on format

## License

[Your License]
