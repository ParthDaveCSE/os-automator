# OS Automator 🚀

A Python-based Command Line Interface (CLI) tool to automatically organize files into categorized folders based on file extensions.

---

## 📌 Overview

Managing cluttered folders manually is inefficient and time-consuming.  
OS Automator scans a folder, detects file types, and organizes them into structured directories automatically.

---

## ✨ Features

- Automatic file categorization (Images, Documents, Data, etc.)
- CLI support using argparse
- Safe file movement (prevents overwriting)
- Retry mechanism for files in use
- Ignores hidden files and directories
- Logging for tracking execution
- Unit testing using pytest
- Configurable rules via schema.py

---

## 🛠 Tech Stack

- Python 3
- pathlib
- argparse
- logging
- pytest

---

## 📂 Project Structure

os-automator/
│
├── src/
│   ├── automator.py
│   └── schema.py
│
├── tests/
│   └── test_automator.py
│
├── main.py
├── requirements.txt
├── README.md
├── LICENSE
└── .gitignore

---

## 🚀 Installation

1. Clone the repository

git clone https://github.com/ParthDaveCSE/os-automator.git  
cd os-automator

2. Create virtual environment

python -m venv venv  
source venv/bin/activate

3. Install dependencies

pip install -r requirements.txt

---

## ▶️ Usage

Run the tool:

python main.py --folder <path_to_folder>

Example:

python main.py --folder ~/Downloads

---

## 🧪 Run Tests

pytest

---

## ⚙️ How It Works

Scan Folder  
→ Detect File Extension  
→ Map to Category  
→ Create Folder  
→ Move File Safely  

---

## ⚠️ Edge Cases Handled

- Duplicate filenames (auto rename)
- Files currently in use (retry logic)
- Unknown file types → "Others"
- Hidden files ignored
- Already organized files skipped

---

## 👨‍💻 Author

Parth Dave

---

## 📄 License

MIT License