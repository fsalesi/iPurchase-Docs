#!/usr/bin/env python3
"""
Generate individual RAG pages for each system setting.
Each setting gets its own file with context and related settings.
"""

import os
import re
import csv

# Category descriptions for context
CATEGORY_CONTEXT = {
    "Approval Workflow": "Controls how requisitions are routed for approval, who can approve, approval thresholds, escalation rules, and delegation behavior.",
    "Change Orders": "Controls change order behavior, tolerance thresholds, and re-routing rules when requisitions or POs are modified.",
    "Email Configuration": "Settings for email notifications, SMTP configuration, email templates, and automated email behavior.",
    "Purchase Orders": "Controls PO creation, numbering, printing, vendor communication, and PO-related workflow.",
    "Requisitions": "Controls requisition entry, validation, defaults, and requisition-related behavior.",
    "Security & Authentication": "Settings for user authentication, SSO, password policies, session management, and security controls.",
    "User Management": "Settings for user accounts, profiles, permissions, delegation, and user-related behavior.",
    "System Configuration": "General system settings for iPurchase configuration, logging, performance, and system-wide behavior.",
    "GL Accounts & Finance": "Settings for GL account validation, financial controls, currency, and accounting-related behavior.",
    "Catalog & Vendors": "Settings for vendor catalogs, punchout suppliers, and vendor management.",
    "Receiving": "Settings for receiving goods and receipt processing.",
    "Inventory & MRP": "Settings for inventory management and MRP integration.",
    "RFQ Management": "Settings for Request for Quote functionality.",
    "Reporting & Inquiry": "Settings for reports and inquiry screens.",
    "ACH Integration": "Settings for ACH payment processing integration.",
    "QAD Integration": "Settings for QAD ERP integration.",
    "Qxtend Integration": "Settings for Qxtend integration.",
    "EAM Integration": "Settings for Enterprise Asset Management integration.",
    "Portal Integration": "Settings for portal integration.",
    "iApprove Integration": "Settings for iApprove mobile app integration.",
}

# Related settings mapping (key settings and what they relate to)
RELATED_SETTINGS = {
    "MULTIPLE_APPROVALS": ["AUTO_APPROVE_FORWARD", "REMOVE_APPROVER_FROM_GROUPS"],
    "AUTO_APPROVE_FORWARD": ["MULTIPLE_APPROVALS"],
    "USE_CHAINED_DELEGATES": ["OOF_LIMIT_TO_APPROVERS", "ALLOW_SUPERVISORS_TO_APPROVE"],
    "ALLOW_SUPERVISORS_TO_APPROVE": ["USE_SUPERVISORS_TO_APPROVE", "SUPERVISOR_ESCALATION_DAYS", "SUPERVISOR_ESCALATION_LEVEL"],
    "SUPERVISOR_ESCALATION_DAYS": ["SUPERVISOR_ESCALATION_LEVEL", "ALLOW_SUPERVISORS_TO_APPROVE"],
    "SUPERVISOR_ESCALATION_LEVEL": ["SUPERVISOR_ESCALATION_DAYS", "ALLOW_SUPERVISORS_TO_APPROVE"],
    "USE_LINE_APPROVALS": ["DEFAULT_LINES_TO_APPROVED", "DEFAULT_LINES_TO_APPROVED_AUTO"],
    "CO_TOLERANCE_AMOUNT": ["CO_TOLERANCE_PERCENT", "ALLOWED_DOLLAR_INCREASE", "ALLOWED_PERCENT_INCREASE"],
    "CO_TOLERANCE_PERCENT": ["CO_TOLERANCE_AMOUNT", "ALLOWED_DOLLAR_INCREASE", "ALLOWED_PERCENT_INCREASE"],
    "ALLOWED_DOLLAR_INCREASE": ["ALLOWED_PERCENT_INCREASE", "CO_TOLERANCE_AMOUNT"],
    "ALLOWED_PERCENT_INCREASE": ["ALLOWED_DOLLAR_INCREASE", "CO_TOLERANCE_PERCENT"],
    "OOF_LIMIT_TO_APPROVERS": ["USE_CHAINED_DELEGATES"],
    "BATCH_APPROVE_GROUPS": ["BATCH_APPROVE_GROUPS_ALWAYS", "BATCH_APPROVE_GROUPS_FINAL"],
    "BATCH_APPROVE_GROUPS_ALWAYS": ["BATCH_APPROVE_GROUPS"],
    "BATCH_APPROVE_GROUPS_FINAL": ["BATCH_APPROVE_GROUPS"],
}

def parse_settings_file(filepath):
    """Parse the settings reference file into individual settings"""
    with open(filepath, 'r') as f:
        content = f.read()
    
    settings = []
    current_category = None
    
    # Find category headers and their tables
    lines = content.split('\n')
    i = 0
    while i < len(lines):
        line = lines[i]
        
        # Check for category header
        if line.startswith('## ') and not line.startswith('## Table'):
            current_category = line[3:].strip()
            i += 1
            continue
        
        # Check for table row with setting
        if line.startswith('| **') and current_category:
            # Parse: | **SETTING_NAME** | Owner | `Default` | Description |
            match = re.match(r'\| \*\*([A-Z0-9_]+)\*\* \| ([^|]*) \| ([^|]*) \| ([^|]*) \|', line)
            if match:
                setting_name = match.group(1)
                owner = match.group(2).strip()
                default = match.group(3).strip().strip('`')
                description = match.group(4).strip()
                
                settings.append({
                    'name': setting_name,
                    'category': current_category,
                    'owner': owner,
                    'default': default,
                    'description': description
                })
        
        i += 1
    
    return settings

def generate_setting_page(setting):
    """Generate a page for a single setting"""
    name = setting['name']
    category = setting['category']
    owner = setting['owner']
    default = setting['default']
    description = setting['description']
    
    category_desc = CATEGORY_CONTEXT.get(category, f"Settings in the {category} category.")
    related = RELATED_SETTINGS.get(name, [])
    
    output = []
    output.append(f"# {name} - iPurchase System Setting\n")
    output.append(f"**Category:** {category}\n")
    output.append(f"{description}\n")
    
    # Common questions
    output.append("**Common questions this answers:**")
    output.append(f"- What is {name}?")
    output.append(f"- What does {name} do?")
    output.append(f"- What is the default value for {name}?")
    output.append(f"- How do I configure {name}?")
    if 'APPROVAL' in name or 'APPROVE' in name:
        output.append(f"- How does {name} affect approval routing?")
    if 'EMAIL' in name:
        output.append(f"- How does {name} affect email notifications?")
    output.append("")
    
    # Setting details
    output.append("## Setting Details\n")
    output.append(f"| Property | Value |")
    output.append(f"|----------|-------|")
    output.append(f"| **Setting Name** | {name} |")
    output.append(f"| **Category** | {category} |")
    output.append(f"| **Owner** | {owner} |")
    output.append(f"| **Default Value** | {default if default else '(none)'} |")
    output.append("")
    
    # SQL query
    output.append("## How to Query\n")
    output.append("```sql")
    output.append(f"SELECT pf_chr1 FROM PUB.pf_mstr")
    output.append(f"WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = '{name}'")
    output.append("```\n")
    
    # Related settings
    if related:
        output.append(f"**Related settings:** {', '.join(related)}")
    
    return "\n".join(output)

def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    repo_root = os.path.dirname(script_dir)
    
    input_file = os.path.join(repo_root, "reference", "system-settings-reference.md")
    output_dir = os.path.join(repo_root, "rag-optimized", "settings")
    
    os.makedirs(output_dir, exist_ok=True)
    
    print(f"Reading: {input_file}")
    settings = parse_settings_file(input_file)
    
    print(f"Found {len(settings)} settings")
    
    max_size = 0
    categories = {}
    
    for setting in settings:
        page = generate_setting_page(setting)
        filename = f"{setting['name']}.md"
        filepath = os.path.join(output_dir, filename)
        
        with open(filepath, 'w') as f:
            f.write(page)
        
        size = len(page)
        if size > max_size:
            max_size = size
        
        cat = setting['category']
        categories[cat] = categories.get(cat, 0) + 1
    
    print(f"\nSettings by category:")
    for cat, count in sorted(categories.items()):
        print(f"  {cat}: {count}")
    
    print(f"\nTotal files: {len(settings)}")
    print(f"Max page size: {max_size} chars")

if __name__ == "__main__":
    main()
