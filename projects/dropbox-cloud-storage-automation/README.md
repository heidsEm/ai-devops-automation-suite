# Dropbox Cloud Storage Automation

## Overview
Automated cloud directory hierarchy generator and master Excel sheet exporter for Dropbox.

## Problem
Organizing monthly master content plans into individual project folders and uploading them manually is labor-intensive.

## Solution
Uses Python openpyxl to parse master Excel workbooks, split monthly worksheets into standalone `.xlsx` files, and upload them via Dropbox SDK.

## Tech Stack
- Python 3.10+
- Dropbox SDK (`dropbox`)
- openpyxl Excel Automation
- Dry-Run Verification Engine

## Architecture / Workflow
Load Master Excel -> Validate Sheets -> Split Worksheets to Individual .xlsx -> Create Dropbox Directory Structure -> Upload Files.

## Key Features
- Automated sheet extraction preserving styles, formulas, and column widths
- Defensive Dropbox API handling (conflict detection & auto-retry)
- OAuth2 refresh-token authentication support
- Complete `--dry-run` simulation mode

## Project Structure
```
projects/dropbox-cloud-storage-automation/
├── README.md
└── scripts/
    └── create_dropbox_master_plan_folders.py
```

## Setup
1. Install dependencies: `pip install dropbox openpyxl`.
2. Set `DROPBOX_ACCESS_TOKEN` or OAuth2 refresh credentials.
3. Run: `python scripts/create_dropbox_master_plan_folders.py --workbook master_plan.xlsx`.

## Example
```bash
python scripts/create_dropbox_master_plan_folders.py --workbook plan.xlsx --dry-run
```

## Security & Privacy
All cloud access tokens are managed via environment variables and never hardcoded in scripts.

## Skills Demonstrated
- Cloud Storage SDK Integration (Dropbox API)
- Programmatic Spreadsheet Parsing (openpyxl)
- Safe Dry-Run Automation Design
