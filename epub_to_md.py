import os
import argparse
from pathlib import Path
from ebooklib import epub
from bs4 import BeautifulSoup
from tqdm import tqdm

def epub_to_markdown(epub_path, output_dir):
    """Convert an EPUB file to Markdown."""
    # Load the EPUB file
    book = epub.read_epub(epub_path)

    # Extract the book title for the output filename
    title = book.get_metadata('DC', 'title')[0][0] if book.get_metadata('DC', 'title') else Path(epub_path).stem
    output_path = Path(output_dir) / f"{title}.md"

    # Process each item in the EPUB
    content = []
    for item in book.get_items():
        if item.media_type == 'application/xhtml+xml':
            # Parse HTML content
            soup = BeautifulSoup(item.get_content(), 'html.parser')
            text = soup.get_text()
            content.append(text)

    # Save the output file with markdown formatting
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write("\n\n".join(content))

def batch_convert_epub_to_markdown(input_dir, output_dir):
    """Batch convert EPUB files in a directory to markdown files."""
    input_dir = Path(input_dir)
    output_dir = Path(output_dir)

    # Ensure the output directory exists
    output_dir.mkdir(parents=True, exist_ok=True)

    # Find all EPUB files in the input directory
    epub_files = list(input_dir.glob("*.epub"))

    # Process each EPUB file with a progress bar
    for epub_file in tqdm(epub_files, desc="Converting EPUBs", unit="file"):
        epub_to_markdown(epub_file, output_dir)

if __name__ == "__main__":
    # Set up argument parser
    parser = argparse.ArgumentParser(description='Convert EPUB files to Markdown.')
    parser.add_argument('--input', default='input', help='Input directory containing EPUB files')
    parser.add_argument('--output', default='output', help='Output directory for converted files')

    args = parser.parse_args()

    # Run the batch conversion
    batch_convert_epub_to_markdown(args.input, args.output)
