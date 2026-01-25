#!/usr/bin/env python3
"""
Split admin-guide.md into RAG-optimized topic files.
"""

import os
import re

INPUT_FILE = 'reference/admin-guide.md'
OUTPUT_DIR = 'rag-optimized/admin'

# Map sections to output files
SECTION_MAP = {
    'User Management': {
        'file': 'user-management.md',
        'title': 'User Management - iPurchase Administration',
        'intro': 'Creating users, setting up supervisor chains, managing groups, and configuring approval limits.'
    },
    'Approval Rules Setup': {
        'file': 'approval-rules-setup.md',
        'title': 'Approval Rules Setup - iPurchase Administration',
        'intro': 'Step-by-step guide to creating and configuring approval rules.'
    },
    'Requisition Types Configuration': {
        'file': 'requisition-types.md',
        'title': 'Requisition Types Configuration - iPurchase Administration',
        'intro': 'Setting up different requisition types (Expense, Capital, Inventory) with type-specific settings.'
    },
    'Change Order Configuration': {
        'file': 'change-order-config.md',
        'title': 'Change Order Configuration - iPurchase Administration',
        'intro': 'Configuring change order tolerance, re-approval requirements, and change order workflows.'
    },
    'Delegation Configuration': {
        'file': 'delegation-config.md',
        'title': 'Delegation Configuration - iPurchase Administration',
        'intro': 'Setting up delegation rules, out-of-office, and chained delegation options.'
    },
    'Testing & Validation': {
        'file': 'testing-validation.md',
        'title': 'Testing & Validation - iPurchase Administration',
        'intro': 'How to test approval rules using approval simulation and validate configuration changes.'
    },
    'Troubleshooting': {
        'file': 'admin-troubleshooting.md',
        'title': 'Administrator Troubleshooting - iPurchase',
        'intro': 'Common administrative issues and how to resolve them.'
    },
    'Security Best Practices': {
        'file': 'security-best-practices.md',
        'title': 'Security Best Practices - iPurchase Administration',
        'intro': 'Security recommendations for user access, permissions, and audit controls.'
    },
}

def read_file(path):
    with open(path, 'r', encoding='utf-8') as f:
        return f.read()

def extract_sections(content):
    """Extract ## sections from content"""
    sections = {}
    current_section = None
    current_content = []
    
    for line in content.split('\n'):
        if line.startswith('## '):
            if current_section:
                sections[current_section] = '\n'.join(current_content)
            current_section = line[3:].strip()
            current_content = []
        elif current_section:
            current_content.append(line)
    
    if current_section:
        sections[current_section] = '\n'.join(current_content)
    
    return sections

def convert_headers(content):
    """Keep ### headers as-is"""
    return content

def write_rag_file(filepath, title, intro, content):
    """Write a RAG-optimized file"""
    content = convert_headers(content)
    
    output = f"# {title}\n\n**Purpose:** {intro}\n\n{content.strip()}\n"
    
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(output)

def main():
    content = read_file(INPUT_FILE)
    sections = extract_sections(content)
    
    for section_name, config in SECTION_MAP.items():
        if section_name not in sections:
            print(f"  Warning: Section '{section_name}' not found")
            continue
        
        filepath = os.path.join(OUTPUT_DIR, config['file'])
        section_content = sections[section_name]
        
        write_rag_file(filepath, config['title'], config['intro'], section_content)
        print(f"  Created {config['file']}")

if __name__ == '__main__':
    main()
