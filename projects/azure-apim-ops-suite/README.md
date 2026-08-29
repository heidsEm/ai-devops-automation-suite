# Azure APIM Ops Suite

## Overview
Operations suite for Azure API Management (APIM), including ADO CI/CD migration, version identification, and Diagram-as-Code generation.

## Problem
Managing large APIM instances across Azure DevOps pipelines requires automated version classification, key synchronization, and visual architecture generation.

## Solution
Provides Python scripts for Azure DevOps key synchronization, APIM API version classification, and automated architecture diagram generation.

## Tech Stack
- Python 3.10+
- Azure APIM REST API
- Azure DevOps REST API
- Diagrams-as-Code

## Architecture / Workflow
Inspect APIM REST API -> Extract API Definitions -> Generate Excel Classification Matrix -> Render Diagrams-as-Code Architecture Image.

## Key Features
- Automated Azure DevOps secret and pipeline key synchronization
- APIM version classification and Excel matrix generation
- Programmatic Azure APIM architecture diagram generation

## Project Structure
```
projects/azure-apim-ops-suite/
├── README.md
└── src/
```

## Setup
1. Set Azure credentials.
2. Run `python src/diagram-generator/azure_apim_diagram.py`.

## Example
```bash
python src/api-identifier/identify_api_version.py --apim-name YOUR_APIM
```

## Security & Privacy
Subscription IDs and resource groups sanitized.

## Skills Demonstrated
- Cloud API Management & Architecture Visualization
