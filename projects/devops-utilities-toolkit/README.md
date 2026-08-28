# DevOps Utilities Toolkit

## Overview
Comprehensive toolkit for TLS/SSL certificate conversions, code diff formatting, and XML API policy inspection.

## Problem
DevOps engineers frequently face repetitive certificate format conversions, IP list comparisons, and API policy inspection tasks.

## Solution
Provides robust Python utilities for `.cer`, `.pem`, and `.pfx` certificate conversion, IP list deduplication, and XML policy parsing.

## Tech Stack
- Python 3.10+
- OpenSSL / Cryptography Libraries
- XML ElementTree & Regex Parsing
- Matplotlib Analytics

## Architecture / Workflow
Input Security File / XML Policy -> Execute Specialized Converter or Parser -> Validate Output -> Generate Sanitized Artifact.

## Key Features
- Bi-directional X.509 certificate conversion (`.cer` <-> `.pem` <-> `.pfx`)
- Fast XML policy inspection (KVM extraction, endpoint listing, IP counting)
- Traffic analytics visualization generator (`traffic-analytics`)
- Zero external network dependencies for security operations

## Project Structure
```
projects/devops-utilities-toolkit/
├── README.md
└── src/
    ├── cert-converter/
    ├── formatting-tools/
    ├── policy-tools/
    └── traffic-analytics/
```

## Setup
1. Run certificate converter: `python src/cert-converter/cer_to_pem.py cert.cer cert.pem`.
2. Run XML policy inspector: `python src/policy-tools/extract_ips_xml.py policy.xml`.

## Example
```bash
python src/cert-converter/pem_to_pfx.py cert.pem cert.key output.pfx
```

## Security & Privacy
All test certificates and policy XMLs contain dummy placeholder data.

## Skills Demonstrated
- Security & PKI Certificate Engineering
- Static Code & XML Policy Analysis
- Lightweight Systems Automation Tools
