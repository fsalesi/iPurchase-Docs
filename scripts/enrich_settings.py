#!/usr/bin/env python3
"""
Enrich setting pages with full descriptions from CSV and context from other docs.
Process in batches - this script handles a specified batch.
"""

import csv
import os
import re
from pathlib import Path

DOCS_ROOT = "/home/frank/ipurchase-docs"
CSV_FILE = f"{DOCS_ROOT}/reference/system-settings-bible.csv"
NEW_CSV_FILE = f"{DOCS_ROOT}/reference/system-settings-bible.new.csv"
SETTINGS_DIR = f"{DOCS_ROOT}/rag-optimized/settings"
REFERENCED_FILE = "/tmp/referenced_settings.txt"

def load_csv_settings():
    """Load all settings from the CSV bible"""
    settings = {}
    with open(CSV_FILE, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            settings[row['Setting_Name']] = {
                'category': row['Category'],
                'owner': row['Owner'],
                'default': row['Default'],
                'description': row['Description']
            }
    return settings

def load_referenced_settings():
    """Load the list of settings referenced in other docs"""
    referenced = {}
    with open(REFERENCED_FILE, 'r') as f:
        for line in f:
            parts = line.strip().split('\t')
            if len(parts) >= 3:
                setting = parts[0]
                count = int(parts[1])
                docs = parts[2].split(',')
                referenced[setting] = docs
    return referenced

def extract_context(setting_name, doc_paths):
    """Extract context about a setting from the docs that reference it"""
    contexts = []
    for doc_path in doc_paths:
        full_path = f"{DOCS_ROOT}/{doc_path}"
        if not os.path.exists(full_path):
            continue
        
        with open(full_path, 'r') as f:
            content = f.read()
        
        # Find paragraphs/sections mentioning this setting
        # Look for the setting name and grab surrounding context
        pattern = r'([^\n]*' + re.escape(setting_name) + r'[^\n]*)'
        matches = re.findall(pattern, content, re.IGNORECASE)
        
        for match in matches:
            # Clean up and add if substantive
            match = match.strip()
            if len(match) > 50 and setting_name in match:
                contexts.append(match)
    
    return contexts

def generate_setting_page(setting_name, data, contexts=None):
    """Generate an enriched setting page"""
    category = data.get('category', 'Uncategorized')
    owner = data.get('owner', '')
    default = data.get('default', '').strip('`')
    description = data.get('description', '')
    new_description = data.get('new_description', description)
    
    lines = []
    lines.append(f"# {setting_name} - iPurchase System Setting")
    lines.append("")
    lines.append(f"**Category:** {category}")
    lines.append("")
    lines.append(new_description)
    lines.append("")
    
    # Common questions
    lines.append("**Common questions this answers:**")
    lines.append(f"- What is {setting_name}?")
    lines.append(f"- What does {setting_name} do?")
    lines.append(f"- What is the default value for {setting_name}?")
    lines.append(f"- How do I configure {setting_name}?")
    
    # Add category-specific questions
    if 'APPROVAL' in setting_name or 'APPROVE' in setting_name:
        lines.append(f"- How does {setting_name} affect approval routing?")
    if 'EMAIL' in setting_name:
        lines.append(f"- How does {setting_name} affect email notifications?")
    if 'PO_' in setting_name or '_PO' in setting_name:
        lines.append(f"- How does {setting_name} affect purchase orders?")
    
    lines.append("")
    
    # Setting details table
    lines.append("## Setting Details")
    lines.append("")
    lines.append("| Property | Value |")
    lines.append("|----------|-------|")
    lines.append(f"| **Setting Name** | {setting_name} |")
    lines.append(f"| **Category** | {category} |")
    lines.append(f"| **Owner** | {owner} |")
    lines.append(f"| **Default Value** | {default if default else '(none)'} |")
    lines.append("")
    
    # SQL query
    lines.append("## How to Query")
    lines.append("")
    lines.append("```sql")
    lines.append("SELECT pf_chr1 FROM PUB.pf_mstr")
    lines.append(f"WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = '{setting_name}'")
    lines.append("```")
    
    return "\n".join(lines)

def main():
    print("Loading settings from CSV...")
    csv_settings = load_csv_settings()
    print(f"Loaded {len(csv_settings)} settings from CSV")
    
    print("Loading referenced settings...")
    referenced = load_referenced_settings()
    print(f"Found {len(referenced)} settings referenced in other docs")
    
    # For now, just print first 5 to verify
    print("\nFirst 5 CSV settings:")
    for i, (name, data) in enumerate(list(csv_settings.items())[:5]):
        print(f"  {name}: {data['category']}")
    
    print("\nTop 5 referenced settings:")
    for name in list(referenced.keys())[:5]:
        print(f"  {name}: referenced in {len(referenced[name])} docs")

if __name__ == "__main__":
    main()
