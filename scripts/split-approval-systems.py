#!/usr/bin/env python3
"""
Split approval-systems.md into RAG-optimized topic files.
This file contains more technical/database details that complement approval-strategy-guide.
Some sections merge into existing files from approval-strategy, others create new files.
"""

import os
import re

INPUT_FILE = 'reference/approval-systems.md'
OUTPUT_DIR = 'rag-optimized/approvals'

# Map sections to output files
SECTION_MAP = {
    'Approval Rule Evaluation Algorithm': {
        'file': 'rule-evaluation-algorithm.md',
        'title': 'Approval Rule Evaluation Algorithm - iPurchase Technical Reference',
        'intro': 'How iPurchase evaluates approval rules in sequence order and builds the approval routing list.'
    },
    'Validation Rules': {
        'file': 'validation-rules.md',
        'title': 'Validation Rules - iPurchase Pre-Submission Checks',
        'intro': 'Rules that block requisition submission if conditions are not met. Use MESSAGE: prefix in approver field.'
    },
    'Duplicate Approver Handling': {
        'file': 'duplicate-approvers.md',
        'title': 'Duplicate Approver Handling - iPurchase',
        'intro': 'How iPurchase handles when the same person appears multiple times in the approval routing (MULTIPLE_APPROVALS setting).'
    },
    'Delegation System': {
        'file': 'delegation.md',
        'title': 'Delegation System - iPurchase',
        'intro': 'How users can delegate approval authority to others, including out-of-office and chained delegation.'
    },
    'Supervisor Override': {
        'file': 'supervisor-override.md',
        'title': 'Supervisor Override - iPurchase',
        'intro': 'How supervisors can approve on behalf of their subordinates without explicit delegation.'
    },
    'Notification Rules': {
        'file': 'notification-rules.md',
        'title': 'Notification Rules - iPurchase FYI Emails',
        'intro': 'Rules that send FYI notifications after approval without requiring approval action (xxapp_notify = TRUE).'
    },
    'Troubleshooting': {
        'file': 'approval-troubleshooting.md',
        'title': 'Approval Troubleshooting - iPurchase',
        'intro': 'Common approval issues and how to diagnose them using database queries.'
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
    """Convert ### to stay as ### (no ## in source sections after extraction)"""
    # Source already uses ### for subsections, keep them
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
