# Dropbox Cloud Storage Automation

## Overview
Automated cloud directory hierarchy generator and master Excel sheet exporter for Dropbox.

## Problem
Organizing monthly master content plans into individual project folders and uploading them manually is labor-intensive.

## Solution
Uses Python openpyxl to parse master Excel workbooks, split monthly worksheets into standalone `.xlsx` files, and upload them via Dropbox SDK.

## Tech Stack
- Python 3.10+
- Dropbox SDK
- openpyxl Excel Automation

## Architecture / Workflow
Load Master Excel -> Validate Sheets -> Split Worksheets to Individual .xlsx -> Create Dropbox Directory Structure -> Upload Files.

## Key Features
- Automated sheet extraction preserving styles & formulas
- Defensive Dropbox API handling
- Complete `--dry-run` simulation mode

## Project Structure
```
projects/dropbox-cloud-storage-automation/
├── README.md
└── scripts/
```

## Setup
1. Run `python scripts/create_dropbox_master_plan_folders.py --workbook plan.xlsx`.

## Example
```bash
python scripts/create_dropbox_master_plan_folders.py --workbook plan.xlsx --dry-run
```

## Security & Privacy
Tokens loaded from environment variables.

## Skills Demonstrated
- Cloud SDK Integration & Spreadsheet Parsing
