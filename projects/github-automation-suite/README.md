# GitHub Automation Suite

## Overview
Repository governance suite for managing branch protection rules, CODEOWNERS, role assignments, and automated changelog generation.

## Problem
Enforcing consistent PR review policies, branch protection, and release documentation across dozens of repositories is difficult to maintain manually.

## Solution
Provides Python scripts and GitHub Actions workflows for bulk branch protection configuration, role audit, and automatic changelog documentation.

## Tech Stack
- Python 3.10+
- GitHub REST API v3
- GitHub Actions (YAML Workflows)
- PyYAML & openpyxl

## Architecture / Workflow
Read Repository Matrix -> Query GitHub API -> Apply Branch Protection & CODEOWNERS -> Trigger Actions Workflow on Release.

## Key Features
- Automated PR review & status check enforcement (`branch-protection/br_pr.py`)
- Role and permission matrix audit across organization repositories
- GitHub Actions reusable workflow caller injector (`add-caller-workflow.py`)
- Automated documentation generator workflow (`generate-change-docs.yaml`)

## Project Structure
```
projects/github-automation-suite/
├── README.md
└── src/
    ├── CODEOWNERS
    ├── add-caller-workflow.py
    ├── gh_role.py
    ├── branch-protection/
    │   ├── apgx_repo.xlsx
    │   └── br_pr.py
    └── workflows/
        └── generate-change-docs.yaml
```

## Setup
1. Set `GITHUB_TOKEN` environment variable.
2. Run branch protection script: `python src/branch-protection/br_pr.py`.

## Example
```bash
python src/gh_role.py --org YOUR_GITHUB_ORG
```

## Security & Privacy
GitHub Personal Access Tokens and organization names are sanitized.

## Skills Demonstrated
- GitHub API & Enterprise Repository Governance
- CI/CD Workflow Engineering (GitHub Actions)
- Security & Access Control Automation
