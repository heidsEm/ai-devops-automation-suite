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

## Architecture / Workflow
Apigee API Authentication -> Proxy / Policy Inspection -> Automated Policy Modification -> Backup/Restore Archive Execution.

## Key Features
- Full Apigee Edge proxy and KVM artifact backup & restoration
- Automated quota policy modification
- Apigee X activity and API key expiration date calculation

## Project Structure
```
projects/apigee-gateway-management/
├── README.md
└── src/
```

## Setup
1. Set `APIGEE_USER`, `APIGEE_PASS`, `APIGEE_ORG`.
2. Run `python src/edge-backup/api_backup.py`.

## Example
```bash
python src/apigeex/add_use_effective_count.py --org YOUR_ORG --env prod
```

## Security & Privacy
Org names and tokens sanitized.

## Skills Demonstrated
- Enterprise API Gateway Administration
