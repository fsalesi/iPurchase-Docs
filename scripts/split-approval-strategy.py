#!/usr/bin/env python3
"""
Split approval-strategy-guide.md into RAG-optimized topic files.
Each output file uses ### headers only (no ##) for single-chunk retrieval.
"""

import os
import re

INPUT_FILE = 'reference/approval-strategy-guide.md'
OUTPUT_DIR = 'rag-optimized/approvals'

# Map sections to output files with custom intro text
SECTION_MAP = {
    'Simple Rules (xxapp_mstr)': {
        'file': 'simple-rules.md',
        'title': 'Simple Approval Rules (xxapp_mstr) - iPurchase',
        'intro': 'Cost center-based approvals with straightforward AND conditions. Stored in xxapp_mstr table.'
    },
    'Complex Rules (xxAppRule)': {
        'file': 'complex-rules.md', 
        'title': 'Complex Approval Rules (xxAppRule) - iPurchase',
        'intro': 'Executive approvals, OR conditions, and scenarios requiring nested AND/OR logic. Stored in xxAppRule/xxAppField tables.'
    },
    'Role-Based Approvals': {
        'file': 'role-based-approvals.md',
        'title': 'Role-Based Approvals - iPurchase',
        'intro': 'Reduce rule maintenance by using roles instead of creating rules for every cost center.'
    },
    'Supervisor Chain Variables': {
        'file': 'supervisor-chain.md',
        'title': 'Supervisor Chain Variables - iPurchase Approval Routing',
        'intro': 'Dynamically determine approvers based on the organizational hierarchy ($SUPERVISORS, $FIRST_SUPERVISOR, $LAST_SUPERVISOR).'
    },
    'Approver List Behavior': {
        'file': 'approver-groups.md',
        'title': 'Approval Groups and Approver Lists - iPurchase',
        'intro': 'Understanding how approver fields work with groups, comma-separated lists, and dynamic variables.'
    },
    'Using Groups Effectively': {
        'file': 'approver-groups.md',  # Append to same file
        'append': True
    },
    'Special Rule Options': {
        'file': 'special-options.md',
        'title': 'Special Approval Rule Options - iPurchase',
        'intro': 'Advanced rule options: stop processing, notify only, active flag, and validation rules.'
    },
    'The Three Default Rules': {
        'file': 'default-rules.md',
        'title': 'Default Approval Rules - iPurchase Safety Nets',
        'intro': 'Built-in rules that ensure compliance and catch configuration gaps.'
    },
    'Additional Default Rules': {
        'file': 'default-rules.md',  # Append to same file
        'append': True
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
    """Convert ## to ### and ### to #### for proper chunking"""
    content = re.sub(r'^## ', '### ', content, flags=re.MULTILINE)
    # Don't convert ### to #### - we want ### as the max level
    return content

def write_rag_file(filepath, title, intro, content):
    """Write a RAG-optimized file"""
    # Convert headers
    content = convert_headers(content)
    
    output = f"# {title}\n\n**Purpose:** {intro}\n\n{content.strip()}\n"
    
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(output)

def append_to_file(filepath, content):
    """Append content to existing file"""
    content = convert_headers(content)
    with open(filepath, 'a', encoding='utf-8') as f:
        f.write(f"\n{content.strip()}\n")

def main():
    content = read_file(INPUT_FILE)
    sections = extract_sections(content)
    
    # Track which files we've created (vs appended to)
    created_files = set()
    
    for section_name, config in SECTION_MAP.items():
        if section_name not in sections:
            print(f"  Warning: Section '{section_name}' not found")
            continue
        
        filepath = os.path.join(OUTPUT_DIR, config['file'])
        section_content = sections[section_name]
        
        if config.get('append') and filepath in created_files:
            append_to_file(filepath, section_content)
            print(f"  Appended to {config['file']}")
        else:
            write_rag_file(filepath, config['title'], config['intro'], section_content)
            created_files.add(filepath)
            print(f"  Created {config['file']}")

if __name__ == '__main__':
    main()
