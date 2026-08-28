#!/usr/bin/env python3
"""
Sanitization Scanner Utility
Scans target directories for accidental secret leaks, tokens, or PII.
"""
import os
import re
import sys

SECRET_PATTERNS = [
    (r'sk-[a-zA-Z0-9_\-]{20,}', 'OpenAI / API Key'),
    (r'ghp_[a-zA-Z0-9]{30,}', 'GitHub PAT Token'),
    (r'sl\.[a-zA-Z0-9_\-]{30,}', 'Dropbox Token'),
    (r'[a-zA-Z0-9._%+-]+@cpartners\.com\.au', 'Internal Email PII'),
]

def scan_directory(path):
    issues = 0
    for root, _, files in os.walk(path):
        for f in files:
            if f.endswith(('.py', '.json', '.html', '.md', '.yaml', '.yml')):
                fpath = os.path.join(root, f)
                with open(fpath, 'r', encoding='utf-8', errors='ignore') as handle:
                    content = handle.read()
                    for pattern, desc in SECRET_PATTERNS:
                        if re.search(pattern, content):
                            print(f"[WARNING] Potential {desc} found in: {fpath}")
                            issues += 1
    if issues == 0:
        print("[SUCCESS] 0 secrets or PII detected. Repository is clean!")

if __name__ == '__main__':
    target = sys.argv[1] if len(sys.argv) > 1 else '.'
    scan_directory(target)
