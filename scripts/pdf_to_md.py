#!/usr/bin/env python3
"""
Extract PDF content to markdown, using OCR fallback for image-based PDFs.
Arnold first activates 'conda activate ocr' before running.
"""

import sys
import os
from pathlib import Path

# Try text extraction first
try:
    from pypdf import PdfReader
    HAS_PYPDF = True
except ImportError:
    HAS_PYPDF = False

# OCR fallback
try:
    import pytesseract
    from pdf2image import convert_from_path
    HAS_OCR = True
except ImportError:
    HAS_OCR = False


def extract_text_pypdf(path):
    """Extract text via pypdf. Returns (text, page_count) or (None, 0) on failure."""
    if not HAS_PYPDF:
        return None, 0
    try:
        reader = PdfReader(path)
        pages = []
        for page in reader.pages:
            t = page.extract_text()
            if t and len(t.strip()) > 20:
                pages.append(t.strip())
        return "\n\n".join(pages), len(reader.pages)
    except Exception:
        return None, 0


def extract_text_ocr(path):
    """Extract text via OCR. Returns text or None."""
    if not HAS_OCR:
        return None
    try:
        images = convert_from_path(path, dpi=300)
        pages = []
        for img in images:
            t = pytesseract.image_to_string(img, lang="eng")
            if t.strip():
                pages.append(t.strip())
        return "\n\n".join(pages)
    except Exception as e:
        print(f"  OCR failed: {e}", file=sys.stderr)
        return None


def pdf_to_markdown(path, output_dir="."):
    path = Path(path).resolve()
    stem = path.stem

    print(f"Processing: {path.name}")

    # Try text extraction
    text, page_count = extract_text_pypdf(path)

    if text and len(text) > 100:
        print(f"  Text-based PDF ({page_count} pages, {len(text)} chars extracted)")
        method = "pypdf (text extraction)"
    else:
        print(f"  Image-based PDF or low text content — falling back to OCR...")
        text = extract_text_ocr(path)
        if not text:
            print(f"  ERROR: Could not extract text from {path.name}", file=sys.stderr)
            return None
        method = "tesseract OCR"

    out_path = Path(output_dir) / f"{stem}.md"
    out_path.write_text(
        f"# {stem}\n\n"
        f"> Extracted from `{path.name}` via {method}\n\n"
        f"{text}\n"
    )
    print(f"  Wrote: {out_path}")
    return str(out_path)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: pdf_to_md.py <pdf1> [pdf2 ...] [-o output_dir]")
        sys.exit(1)

    output_dir = "."
    pdfs = []
    for arg in sys.argv[1:]:
        if arg == "-o" and len(sys.argv) > sys.argv.index(arg) + 1:
            output_dir = sys.argv[sys.argv.index(arg) + 1]
        elif arg != "-o" and (sys.argv.index(arg) < 1 or sys.argv[sys.argv.index(arg) - 1] != "-o"):
            pdfs.append(arg)

    Path(output_dir).mkdir(parents=True, exist_ok=True)

    for pdf in pdfs:
        pdf_to_markdown(pdf, output_dir)
