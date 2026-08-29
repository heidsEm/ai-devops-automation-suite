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
- GitHub Actions (YAML)

## Architecture / Workflow
Read Repository Matrix -> Query GitHub API -> Apply Branch Protection & CODEOWNERS -> Trigger Actions Workflow on Release.

## Key Features
- Automated PR review & status check enforcement
- Role and permission matrix audit across organization repositories
- GitHub Actions reusable workflow caller injector

## Project Structure
```
projects/github-automation-suite/
├── README.md
└── src/
```

## Setup
1. Set `GITHUB_TOKEN`.
2. Run `python src/branch-protection/br_pr.py`.

## Example
```bash
python src/gh_role.py --org YOUR_GITHUB_ORG
```

## Security & Privacy
PAT tokens and org names sanitized.

## Skills Demonstrated
- GitHub API & Repository Governance
