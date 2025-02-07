# EPUB to Markdown Converter

This Python script converts EPUB files to Markdown files, making them suitable for use with Large Language Models (LLMs).

## Features

- Batch processing: Converts all EPUB files in a specified input directory.
- Progress indicator: Uses `tqdm` to display a progress bar during conversion.
- LLM-friendly output: Extracts text content from EPUB files and saves it in Markdown format.

## Requirements

- Python 3.6 or higher
- `ebooklib`
- `beautifulsoup4`
- `tqdm`

## Installation

1.  Install the required libraries:

    ```bash
    pip install EbookLib beautifulsoup4 tqdm
    ```

## Usage

1.  Place your EPUB files in an input directory (e.g., `input/`).
2.  Run the script:

    ```bash
    python epub_to_markdown.py
    ```

3.  The converted Markdown files will be saved in the output directory (e.g., `output/`).

## Configuration

Modify the `input_directory` and `output_directory` variables in the script to point to your desired input and output directories:

```python
if __name__ == "__main__":
    # Define input and output directories
    input_directory = "input"
    output_directory = "output"

    # Run the batch conversion
    batch_convert_epub_to_markdown(input_directory, output_directory)
```

## Example

For an EPUB file named `example.epub` in the input directory, the script will generate a Markdown file named `example.md` in the output directory.

## Notes

- The script extracts the text content from the EPUB files.
- The script attempts to extract the book title from the EPUB metadata. If the title is not available, the script uses the EPUB filename as the Markdown filename.

## License

[Your License]
