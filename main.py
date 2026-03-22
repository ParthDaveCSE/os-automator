# main.py

import argparse
from pathlib import Path
from src.automator import organize_folder


def main():
    parser = argparse.ArgumentParser(
        description="Organize files in a folder by category"
    )

    parser.add_argument(
        "--folder",
        required=True,
        help="Path to the folder to organize"
    )

    args = parser.parse_args()

    folder_path = Path(args.folder).resolve()

    organize_folder(str(folder_path))


if __name__ == "__main__":
    main()