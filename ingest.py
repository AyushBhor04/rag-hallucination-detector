"""
ingest.py
Reads PDF, HTML, and Markdown files from data/, extracts clean text,
splits into overlapping chunks, and saves everything as one unified
JSON file for the embedding step (Step 4).
"""

import json
from pathlib import Path
from pypdf import PdfReader
from bs4 import BeautifulSoup
import markdown

# ---------- CONFIG ----------
CHUNK_SIZE = 300      # words per chunk
CHUNK_OVERLAP = 50    # words shared between consecutive chunks

DATA_DIR = Path("data")
OUTPUT_DIR = Path("data/processed")
OUTPUT_FILE = OUTPUT_DIR / "chunks.json"


# ---------- PER-FORMAT TEXT EXTRACTORS ----------

def extract_text_from_pdf(filepath: Path) -> str:
    """Reads a PDF page by page and concatenates the text."""
    reader = PdfReader(str(filepath))
    text_parts = []
    for page in reader.pages:
        page_text = page.extract_text()
        if page_text:
            text_parts.append(page_text)
    return "\n".join(text_parts)


def extract_text_from_html(filepath: Path) -> str:
    """Strips non-content tags, keeps visible page text."""
    with open(filepath, "r", encoding="utf-8", errors="ignore") as f:
        raw_html = f.read()

    soup = BeautifulSoup(raw_html, "html.parser")
    for tag in soup(["script", "style", "nav", "header", "footer", "noscript"]):
        tag.decompose()

    text = soup.get_text(separator="\n")
    lines = [line.strip() for line in text.splitlines()]
    lines = [line for line in lines if line]
    return "\n".join(lines)


def extract_text_from_markdown(filepath: Path) -> str:
    """Converts Markdown to HTML, then strips tags to get plain text."""
    with open(filepath, "r", encoding="utf-8", errors="ignore") as f:
        md_text = f.read()

    html = markdown.markdown(md_text)
    soup = BeautifulSoup(html, "html.parser")
    text = soup.get_text(separator="\n")

    lines = [line.strip() for line in text.splitlines()]
    lines = [line for line in lines if line]
    return "\n".join(lines)


# ---------- CHUNKING ----------

def chunk_text(text: str, chunk_size=CHUNK_SIZE, overlap=CHUNK_OVERLAP):
    """Splits text into overlapping word-based chunks."""
    words = text.split()
    if not words:
        return []

    chunks = []
    start = 0
    while start < len(words):
        end = start + chunk_size
        chunk_words = words[start:end]
        chunks.append(" ".join(chunk_words))
        if end >= len(words):
            break
        start = end - overlap

    return chunks


# ---------- MAIN PIPELINE ----------

def process_folder(folder: Path, file_ext: str, extractor_fn, format_name: str, all_chunks: list):
    """Loops over files of one format, extracts + chunks, appends to all_chunks."""
    files = list(folder.glob(f"*.{file_ext}"))
    print(f"Found {len(files)} .{file_ext} files in {folder}")

    for filepath in files:
        print(f"  Processing: {filepath.name}")
        try:
            text = extractor_fn(filepath)
        except Exception as e:
            print(f"    FAILED to extract {filepath.name}: {e}")
            continue

        if not text.strip():
            print(f"    WARNING: no text extracted from {filepath.name}")
            continue

        chunks = chunk_text(text)
        for i, chunk in enumerate(chunks):
            all_chunks.append({
                "chunk_id": f"{filepath.stem}_{i}",
                "text": chunk,
                "source_file": filepath.name,
                "format": format_name,
                "chunk_index": i
            })
        print(f"    -> {len(chunks)} chunks created")


def main():
    all_chunks = []

    process_folder(DATA_DIR / "pdf", "pdf", extract_text_from_pdf, "pdf", all_chunks)
    process_folder(DATA_DIR / "html", "html", extract_text_from_html, "html", all_chunks)
    process_folder(DATA_DIR / "markdown", "md", extract_text_from_markdown, "markdown", all_chunks)

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        json.dump(all_chunks, f, indent=2, ensure_ascii=False)

    print(f"\nDONE. Total chunks created: {len(all_chunks)}")
    print(f"Saved to: {OUTPUT_FILE}")


if __name__ == "__main__":
    main()