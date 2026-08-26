"""
Merge two PDF files into one PDF (page order: path1, then path2).

Uses pypdf 6+ API: PdfWriter.append(). (PdfMerger was removed from the
public pypdf package in v6, so `from pypdf import PdfMerger` fails.)

Usage:
  python merge_files.py <path1.pdf> <path2.pdf> <output.pdf>

Install:
  python -m pip install -r requirements.txt
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Merge two PDF files into a single PDF (path1 pages, then path2 pages)."
    )
    parser.add_argument("path1", type=Path, help="First PDF file")
    parser.add_argument("path2", type=Path, help="Second PDF file")
    parser.add_argument("output", type=Path, help="Output path (should end with .pdf)")
    args = parser.parse_args()

    if args.output.suffix.lower() != ".pdf":
        print("Error: output path should use a .pdf extension.", file=sys.stderr)
        sys.exit(1)

    for label, p in ("path1", args.path1), ("path2", args.path2):
        if not p.exists():
            print(f"Error: {label} does not exist: {p}", file=sys.stderr)
            sys.exit(1)
        if not p.is_file():
            print(f"Error: {label} is not a file: {p}", file=sys.stderr)
            sys.exit(1)
        if p.suffix.lower() != ".pdf":
            print(f"Warning: {label} is not named .pdf: {p}", file=sys.stderr)

    try:
        from pypdf import PdfWriter
    except ImportError:
        print("Error: install pypdf: python -m pip install pypdf", file=sys.stderr)
        sys.exit(1)

    args.output.parent.mkdir(parents=True, exist_ok=True)
    writer = PdfWriter()
    writer.append(str(args.path1))
    writer.append(str(args.path2))
    writer.write(str(args.output))
    writer.close()

    print(f"Wrote merged PDF to {args.output}")


if __name__ == "__main__":
    main()
