# Apigee Gateway Management

## Overview
Management and backup/restore utilities for Apigee Edge and Apigee X API Gateways.

## Problem
Administering API proxy lifecycle, backing up configurations, and calculating quota policies across Apigee environments requires repeatable automation.

## Solution
Provides Python management scripts for Apigee X activity monitoring, quota policy injection (`useEffectiveCount`), and full Apigee Edge proxy backup/restore.

## Tech Stack
- Python 3.10+
- Apigee Management API
- Apigee X Admin API
- REST / JSON Automation

## Architecture / Workflow
Apigee API Authentication -> Proxy / Policy Inspection -> Automated XML/JSON Policy Modification -> Backup/Restore Archive Execution.

## Key Features
- Full Apigee Edge proxy and KVM artifact backup & restoration
- Automated quota policy modification (`useEffectiveCount` injection)
- Apigee X activity and API key expiration date calculation
- Environment configuration decoupling

## Project Structure
```
projects/apigee-gateway-management/
├── README.md
└── src/
    ├── apigeex/
    │   ├── add_use_effective_count.py
    │   ├── api_key_date_calculator.py
    │   └── get_apgx_activity.py
    └── edge-backup/
        ├── api_backup.py
        ├── api_restore.py
        ├── artifact_backup.py
        └── artifact_restore.py
```

## Setup
1. Set Apigee credentials in environment variables (`APIGEE_USER`, `APIGEE_PASS`, `APIGEE_ORG`).
2. Run backup: `python src/edge-backup/api_backup.py`.

## Example
```bash
python src/apigeex/add_use_effective_count.py --org YOUR_ORG --env prod
```

## Security & Privacy
All organization names, credentials, and API endpoints use placeholder parameters.

## Skills Demonstrated
- Enterprise API Gateway Administration
- Automated Backup & Disaster Recovery Pipelines
- XML/JSON Policy Manipulation
