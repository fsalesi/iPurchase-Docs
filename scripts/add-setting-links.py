#!/usr/bin/env python3
"""
Add links to RAG setting pages in system-settings-reference.md
Converts **SETTING_NAME** to [**SETTING_NAME**](../rag-optimized/settings/SETTING_NAME.md)
"""

import os
import re

INPUT_FILE = '/home/frank/ipurchase-docs/reference/system-settings-reference.md'
OUTPUT_FILE = INPUT_FILE  # Overwrite
RAG_SETTINGS_DIR = '/home/frank/ipurchase-docs/rag-optimized/settings'

# Get list of actual RAG setting files
rag_settings = set()
for f in os.listdir(RAG_SETTINGS_DIR):
    if f.endswith('.md'):
        rag_settings.add(f[:-3])  # Remove .md

print(f"Found {len(rag_settings)} RAG setting files")

# Read the file
with open(INPUT_FILE, 'r', encoding='utf-8') as f:
    content = f.read()

# Pattern: | **SETTING_NAME** | in table rows
# Allow letters, numbers, underscores, brackets, and spaces in setting names
def replace_setting(match):
    setting_name = match.group(1)
    if setting_name in rag_settings:
        # Check if filename has special chars that need angle brackets
        if '[' in setting_name:
            return f'| [**{setting_name}**](<../rag-optimized/settings/{setting_name}.md>) |'
        else:
            return f'| [**{setting_name}**](../rag-optimized/settings/{setting_name}.md) |'
    else:
        # No RAG file exists, keep as-is
        return match.group(0)

# Match | **SETTING_NAME** | pattern - allow more characters
pattern = r'\| \*\*([A-Za-z0-9_\[\] ]+)\*\* \|'
new_content, count = re.subn(pattern, replace_setting, content)

print(f"Replaced {count} setting references with links")

# Write back
with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
    f.write(new_content)

print(f"Updated {OUTPUT_FILE}")
