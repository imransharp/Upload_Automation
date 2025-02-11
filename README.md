# Upload_Automation
To upload larger files

# CSV Split & Upload Automation (Python)

## 📌 Overview
This script automatically:
- Detects the latest CSV file in a directory
- Splits it into smaller files
- Prepares files for database upload (without credentials for security)

## 🚀 Features
- Uses Python's `csv` and `os` modules
- Automatically finds the latest CSV file
- Supports configurable file sizes
- Handles errors gracefully

## 🛠 How to Use
1. Place CSV files in the `big_file/` directory.
2. Run the script.
3. Processed files will be saved in `upload/`.

> **Note:** This repo does not contain sensitive credentials.
