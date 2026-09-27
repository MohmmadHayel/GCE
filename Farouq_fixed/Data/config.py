"""Load API settings without storing credentials in source code."""
import os
from pathlib import Path
from dotenv import load_dotenv

PROJECT_ROOT = Path(__file__).resolve().parents[1]
load_dotenv(PROJECT_ROOT / '.env', override=False)


def get_secret(name: str) -> str:
    """Environment variables locally; Streamlit secrets if deployed in Cloud."""
    value = os.getenv(name, '').strip()
    if value:
        return value
    try:
        import streamlit as st
        return str(st.secrets.get(name, '')).strip()
    except (ImportError, FileNotFoundError, KeyError, OSError):
        return ''
