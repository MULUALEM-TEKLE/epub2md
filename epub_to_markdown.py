import os
from pathlib import Path
from ebooklib import epub
from bs4 import BeautifulSoup
from tqdm import tqdm

def epub_to_markdown(epub_path, output_dir):
    """Convert an EPUB file to a Markdown file."""
    # Load the EPUB file
    book = epub.read_epub(epub_path)

    # Extract the book title for the output filename
    title = book.get_metadata('DC', 'title')[0][0] if book.get_metadata('DC', 'title') else Path(epub_path).stem
    output_path = Path(output_dir) / f"{title}.md"

    # Process each item in the EPUB
    markdown_content = []
    for item in book.get_items():
        if item.media_type == 'application/xhtml+xml':
            # Parse HTML content
            soup = BeautifulSoup(item.get_content(), 'html.parser')
            text = soup.get_text()
            markdown_content.append(text)

    # Save the Markdown file
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write("\n\n".join(markdown_content))

def batch_convert_epub_to_markdown(input_dir, output_dir):
    """Batch convert EPUB files in a directory to Markdown files."""
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
    # Define input and output directories
    input_directory = "input"
    output_directory = "output"

    # Run the batch conversion
    batch_convert_epub_to_markdown(input_directory, output_directory)
