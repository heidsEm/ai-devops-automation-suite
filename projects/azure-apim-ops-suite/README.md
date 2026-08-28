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
- Azure DevOps (ADO) REST API
- Diagrams-as-Code (Graphviz / `diagrams`)
- openpyxl

## Architecture / Workflow
Inspect APIM REST API -> Extract API Definitions & Version Sets -> Generate Excel Classification Matrix -> Render Diagrams-as-Code Architecture Image.

## Key Features
- Automated Azure DevOps secret and pipeline key synchronization
- APIM version classification and Excel matrix generation
- Programmatic Azure APIM architecture diagram generation (`azure_apim_diagram.py`)
- Clean command-line interface

## Project Structure
```
projects/azure-apim-ops-suite/
├── README.md
└── src/
    ├── ado-migration/
    │   ├── ado_delete.py
    │   └── ado_gh_wf_keys.py
    ├── api-identifier/
    │   ├── api_classification.xlsx
    │   └── identify_api_version.py
    └── diagram-generator/
        └── azure_apim_diagram.py
```

## Setup
1. Set Azure credentials (`AZURE_SUBSCRIPTION_ID`, `AZURE_RESOURCE_GROUP`, `APIM_SERVICE_NAME`).
2. Run diagram generator: `python src/diagram-generator/azure_apim_diagram.py`.

## Example
```bash
python src/api-identifier/identify_api_version.py --apim-name YOUR_APIM
```

## Security & Privacy
Subscription IDs, resource group names, and tenant details are sanitized.

## Skills Demonstrated
- Cloud API Management & Azure Infrastructure
- Diagrams-as-Code Visualization
- CI/CD Secret & Pipeline Synchronization
