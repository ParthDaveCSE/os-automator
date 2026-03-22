# src/automator.py

from pathlib import Path
import shutil
import logging
import time
from src.schema import FILE_CATEGORIES, DEFAULT_CATEGORY


# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s: %(message)s"
)


def get_category(extension: str) -> str:
    for category, extensions in FILE_CATEGORIES.items():
        if extension.lower() in extensions:
            return category
    return DEFAULT_CATEGORY


def organize_folder(folder_path: str) -> None:
    folder = Path(folder_path)

    # Check if folder exists
    if not folder.exists():
        logging.error(f"Folder does not exist: {folder}")
        return

    logging.info(f"Organizing folder: {folder}")

    for file in folder.iterdir():

        # Ignore directories
        if file.is_dir():
            continue

        # Ignore hidden files
        if file.name.startswith("."):
            continue

        ext = file.suffix
        category = get_category(ext)

        target_folder = folder / category
        target_folder.mkdir(exist_ok=True)

        # Skip if already in correct folder
        if file.parent == target_folder:
            continue

        target_path = target_folder / file.name

        # Handle duplicate filenames
        counter = 1
        while target_path.exists():
            new_name = f"{file.stem}_{counter}{file.suffix}"
            target_path = target_folder / new_name
            counter += 1

        # Move file with retry logic
        for attempt in range(3):
            try:
                shutil.move(str(file), str(target_path))
                logging.info(f"Moved {file.name} → {category}")
                break

            except PermissionError:
                logging.warning(
                    f"File in use: {file.name}, retrying..."
                )
                time.sleep(1)

            except Exception as e:
                logging.error(f"Error moving {file.name}: {e}")
                break

    logging.info("Organization completed successfully")