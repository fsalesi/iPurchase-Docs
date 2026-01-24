#!/usr/bin/env python3
"""
Generate RAG-optimized version of system-settings-reference.md

Reads the clean settings file and outputs a verbose version with
additional context for better vector search matching.
"""

import re
import os

# Category metadata - add context for each category
CATEGORY_CONTEXT = {
    "Approval Workflow": {
        "description": "Settings that control how requisitions are routed for approval, who can approve, approval thresholds, escalation rules, and delegation behavior.",
        "use_cases": [
            "Configure approval routing behavior",
            "Set up supervisor chain approvals",
            "Control who can modify approvers",
            "Configure approval escalation and reminders",
            "Set up batch approval permissions"
        ],
        "questions": [
            "How do I configure approval routing?",
            "What settings control supervisor approvals?",
            "How do I enable batch approvals?",
            "How does approval escalation work?",
            "What is MULTIPLE_APPROVALS?",
            "How do I configure delegation/OOF?"
        ]
    },
    "Change Orders": {
        "description": "Settings that control change order behavior, tolerance thresholds, and re-routing rules when requisitions or POs are modified.",
        "use_cases": [
            "Set change order tolerance amounts",
            "Configure when changes require re-approval",
            "Control change order routing behavior"
        ],
        "questions": [
            "How do change order tolerances work?",
            "When do changes require re-approval?",
            "What is CO_TOLERANCE_AMOUNT?"
        ]
    },
    "Email Configuration": {
        "description": "Settings for email notifications, SMTP configuration, email templates, and automated email behavior throughout iPurchase.",
        "use_cases": [
            "Configure SMTP server settings",
            "Control which emails are sent",
            "Set up email templates and formatting",
            "Configure approval notification emails"
        ],
        "questions": [
            "How do I configure email settings?",
            "How do I disable certain email notifications?",
            "What is the SMTP configuration?"
        ]
    },
    "Purchase Orders": {
        "description": "Settings that control PO creation, numbering, printing, vendor communication, and PO-related workflow.",
        "use_cases": [
            "Configure PO number formats",
            "Control PO creation behavior",
            "Set up PO printing and distribution",
            "Configure vendor PO emails"
        ],
        "questions": [
            "How are PO numbers generated?",
            "How do I configure PO printing?",
            "How do I control PO creation?"
        ]
    },
    "Requisitions": {
        "description": "Settings that control requisition entry, validation, defaults, and requisition-related behavior.",
        "use_cases": [
            "Configure requisition defaults",
            "Set up validation rules",
            "Control requisition numbering",
            "Configure requisition types"
        ],
        "questions": [
            "How do I configure requisition defaults?",
            "How do requisition numbers work?",
            "How do I set up requisition types?"
        ]
    },
    "Security & Authentication": {
        "description": "Settings for user authentication, SSO, password policies, session management, and security controls.",
        "use_cases": [
            "Configure SSO/SAML settings",
            "Set password policies",
            "Control session timeouts",
            "Configure security permissions"
        ],
        "questions": [
            "How do I configure SSO?",
            "What are the password requirements?",
            "How do session timeouts work?"
        ]
    },
    "User Management": {
        "description": "Settings for user accounts, profiles, permissions, delegation, and user-related behavior.",
        "use_cases": [
            "Configure user permissions",
            "Set up delegation/out-of-office",
            "Control user defaults",
            "Configure supervisor relationships"
        ],
        "questions": [
            "How do I configure user permissions?",
            "How does delegation work?",
            "How do I set up supervisors?"
        ]
    },
    "System Configuration": {
        "description": "General system settings for iPurchase configuration, logging, performance, and system-wide behavior.",
        "use_cases": [
            "Configure system defaults",
            "Set up logging and debugging",
            "Control system-wide behavior"
        ],
        "questions": [
            "How do I configure system settings?",
            "Where are system logs?",
            "How do I enable debugging?"
        ]
    },
    "GL Accounts & Finance": {
        "description": "Settings for GL account validation, financial controls, currency, and accounting-related behavior.",
        "use_cases": [
            "Configure GL account validation",
            "Set up financial controls",
            "Configure currency settings"
        ],
        "questions": [
            "How do I validate GL accounts?",
            "How do I configure account ranges?",
            "How does currency handling work?"
        ]
    }
}

# Key settings to highlight with extra context
KEY_SETTINGS = {
    "MULTIPLE_APPROVALS": "Controls behavior when same approver appears multiple times in routing. Options: KEEP_ALL (all instances), KEEP_FIRST (first only), KEEP_LAST (last only, recommended).",
    "AUTO_APPROVE_FORWARD": "Automatically marks subsequent approvals as approved when same user/group appears multiple times.",
    "USE_CHAINED_DELEGATES": "When TRUE, follows delegation chains (A delegates to B who delegates to C). When FALSE, stops at first delegate.",
    "ALLOW_SUPERVISORS_TO_APPROVE": "Can-Do list of who can approve on behalf of their subordinates. Use '*' for everyone.",
    "SUPERVISOR_ESCALATION_DAYS": "Days before approval can escalate to supervisor. Used with SUPERVISOR_ESCALATION_LEVEL.",
    "USE_LINE_APPROVALS": "Enable line-by-line approval instead of whole requisition approval.",
    "CO_TOLERANCE_AMOUNT": "Dollar amount threshold for change order re-routing. Changes within tolerance don't require re-approval.",
    "CO_TOLERANCE_PERCENT": "Percentage threshold for change order re-routing.",
    "ALLOWED_DOMAINS": "Comma-separated list of valid domain codes in the system.",
    "OOF_LIMIT_TO_APPROVERS": "When TRUE, users can only delegate to other approvers.",
}

def parse_settings_file(filepath):
    """Parse the settings file into categories and settings"""
    with open(filepath, 'r') as f:
        content = f.read()
    
    # Split by ## headers (category names)
    sections = re.split(r'^(## [^\n]+)', content, flags=re.MULTILINE)
    
    categories = {}
    current_category = None
    
    for section in sections:
        if section.startswith('## ') and not section.startswith('## Table of Contents'):
            current_category = section.replace('## ', '').strip()
        elif current_category and section.strip():
            categories[current_category] = section.strip()
    
    return categories

def generate_category_section(category_name, original_content, metadata):
    """Generate verbose section for a category"""
    output = []
    
    # Category header
    output.append(f"## {category_name}\n")
    
    # Description
    desc = metadata.get("description", "")
    if desc:
        output.append(f"{desc}\n")
    
    # Use cases
    use_cases = metadata.get("use_cases", [])
    if use_cases:
        output.append("**Configure these settings when you need to:**")
        for uc in use_cases:
            output.append(f"- {uc}")
        output.append("")
    
    # Common questions
    questions = metadata.get("questions", [])
    if questions:
        output.append("**Common questions this answers:**")
        for q in questions:
            output.append(f"- {q}")
        output.append("")
    
    # Original content (settings table)
    output.append("### Settings\n")
    output.append(original_content)
    
    return "\n".join(output)

def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    repo_root = os.path.dirname(script_dir)
    
    input_file = os.path.join(repo_root, "reference", "system-settings-reference.md")
    output_file = os.path.join(repo_root, "rag-optimized", "system-settings-rag.md")
    
    print(f"Reading: {input_file}")
    categories = parse_settings_file(input_file)
    
    output = []
    output.append("# iPurchase System Settings Reference (RAG-Optimized)\n")
    output.append("> This file is auto-generated for AI/RAG vector search optimization.")
    output.append("> Do not edit directly. Edit `reference/system-settings-reference.md` and regenerate.\n")
    output.append("Complete catalog of iPurchase system settings organized by category. These settings are stored in the pf_mstr table and control all aspects of iPurchase behavior.\n")
    output.append("**To query a setting:**")
    output.append("```sql")
    output.append("SELECT pf_chr1 FROM PUB.pf_mstr")
    output.append("WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'SETTING_NAME'")
    output.append("```\n")
    
    for category_name, content in categories.items():
        metadata = CATEGORY_CONTEXT.get(category_name, {})
        if metadata:
            section = generate_category_section(category_name, content, metadata)
        else:
            section = f"## {category_name}\n\n{content}"
        
        output.append(section)
        output.append("\n---\n")
    
    # Write output
    os.makedirs(os.path.dirname(output_file), exist_ok=True)
    with open(output_file, 'w') as f:
        f.write("\n".join(output))
    
    print(f"Generated: {output_file}")
    print(f"Categories processed: {len(categories)}")
    print(f"Categories with custom context: {len([c for c in categories if c in CATEGORY_CONTEXT])}")

if __name__ == "__main__":
    main()
