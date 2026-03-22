from pathlib import Path
from src.automator import get_category, organize_folder


def test_get_category_known():
    assert get_category(".pdf") == "Documents"
    assert get_category(".jpg") == "Images"


def test_get_category_unknown():
    assert get_category(".xyz") == "Others"


def test_organize_folder(tmp_path):
    file1 = tmp_path / "test.pdf"
    file2 = tmp_path / "image.jpg"
    file3 = tmp_path / "data.csv"

    file1.write_text("dummy")
    file2.write_text("dummy")
    file3.write_text("dummy")

    organize_folder(str(tmp_path))

    assert (tmp_path / "Documents" / "test.pdf").exists()
    assert (tmp_path / "Images" / "image.jpg").exists()
    assert (tmp_path / "Data" / "data.csv").exists()