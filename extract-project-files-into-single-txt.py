#!/usr/bin/env python3
"""
collect_sources.py

Recursively scans a project directory for source files
(e.g. .java, .jsp, .xml, .js) and writes them all into one
text file with headings and fenced code blocks.
"""

import os
import argparse
from pathlib import Path

def collect_sources(src_dir: Path, out_file: Path, extensions):
    counter = 1
    with out_file.open('w', encoding='utf-8') as writer:
        for file_path in src_dir.rglob('*'):
            if file_path.suffix.lower() in extensions:
                fname = file_path.name
                writer.write(f"{counter}. {fname} :\n")
                writer.write("```\n")
                try:
                    # read source file
                    text = file_path.read_text(encoding='utf-8', errors='ignore')
                except Exception as e:
                    text = f"// ERROR reading file: {e}\n"
                writer.write(text.rstrip() + "\n")
                writer.write("```\n\n")
                counter += 1

def main():
    parser = argparse.ArgumentParser(
        description="Collect all source files into one text document."
    )
    parser.add_argument(
        "project_dir",
        type=Path,
        help="Path to the root of your project folder"
    )
    parser.add_argument(
        "-o", "--output",
        type=Path,
        default=Path("all_sources.txt"),
        help="Output text file (default: all_sources.txt)"
    )
    parser.add_argument(
        "-e", "--ext",
        nargs="+",
        default=[".java", ".jsp", ".xml", ".js"],
        help="List of extensions to include (default: .java .jsp .xml .js)"
    )

    args = parser.parse_args()

    if not args.project_dir.is_dir():
        parser.error(f"{args.project_dir} is not a directory")
    collect_sources(args.project_dir, args.output, set(ext.lower() for ext in args.ext))
    print(f"Wrote sources to {args.output}")

if __name__ == "__main__":
    main()
