#!/usr/bin/env python3
"""
Environment Variable Loader Helper
Safely loads environment configurations from .env files without hardcoding credentials.
"""
import os

def get_required_env(var_name: str, fallback: str = "") -> str:
    val = os.getenv(var_name, fallback)
    if not val:
        print(f"[NOTICE] Environment variable '{var_name}' is not set. Using placeholder fallback.")
        return f"YOUR_{var_name}"
    return val
