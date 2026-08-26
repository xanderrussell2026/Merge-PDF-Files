# Merge PDF Files

A PDF merger that takes two PDFs from your filesystem and writes them into a given output file.

## Install

```bash
python -m pip install -r requirements.txt
```

## Usage

```bash
python merge_files.py <path1.pdf> <path2.pdf> <output.pdf>
```

Pages from `path1` come first, then pages from `path2`.

### Example

```bash
python merge_files.py cover.pdf report.pdf merged.pdf
```
