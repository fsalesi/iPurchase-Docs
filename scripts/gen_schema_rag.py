#!/usr/bin/env python3
"""
Generate RAG-optimized version of database-schema.md

Reads the clean schema file and outputs a verbose version with
additional context for better vector search matching.
"""

import re
import os

# Table metadata - add context for important tables
TABLE_CONTEXT = {
    "wus_mstr": {
        "title": "User Master Table",
        "description": "Stores all user accounts, profiles, and settings for iPurchase. Contains login credentials, approval limits, supervisor relationships, delegates, and user preferences.",
        "use_cases": [
            "Look up user information by ID or name",
            "Find a user's supervisor or delegate",
            "Check user approval limits",
            "Query user email addresses",
            "Find users by department or role"
        ],
        "questions": [
            "What fields are in the user table?",
            "How do I find a user's supervisor?",
            "Where is the approval limit stored?",
            "What is wus_delegate?",
            "How do I check if a user is disabled?"
        ],
        "related": ["wgr_mstr (groups)", "wugr_mstr (group membership)", "pf_mstr (user preferences)"]
    },
    "wgr_mstr": {
        "title": "Group Master Table", 
        "description": "Defines groups used for approval routing, permissions, and organizational structure. Groups can be referenced in approval rules.",
        "use_cases": [
            "List all groups in the system",
            "Find group descriptions",
            "Query groups for approval routing"
        ],
        "questions": [
            "What groups exist in the system?",
            "How are groups defined?",
            "What is wgr_id?"
        ],
        "related": ["wugr_mstr (membership)", "xxapp_mstr (approval rules)"]
    },
    "wugr_mstr": {
        "title": "User-Group Membership Table",
        "description": "Links users to groups. Each record represents one user belonging to one group.",
        "use_cases": [
            "Find all members of a group",
            "Find which groups a user belongs to",
            "Check group membership for approval routing"
        ],
        "questions": [
            "Who is in a specific group?",
            "What groups does a user belong to?",
            "How is group membership stored?"
        ],
        "related": ["wus_mstr (users)", "wgr_mstr (groups)"]
    },
    "pf_mstr": {
        "title": "Parameter/Preferences Master Table",
        "description": "Stores all system settings, user preferences, and configuration parameters. The central configuration table for iPurchase.",
        "use_cases": [
            "Query system settings",
            "Find user-specific preferences",
            "Check feature flags",
            "Look up requisition type settings"
        ],
        "questions": [
            "Where are system settings stored?",
            "How do I find a specific setting?",
            "What is pf_chr1?",
            "How do I query settings by attribute name?"
        ],
        "related": ["System Settings documentation"]
    },
    "xxreq_mstr": {
        "title": "Requisition Header Table",
        "description": "The main requisition table containing header-level information: status, dates, totals, vendor, buyer, and workflow state. Every requisition has one record here.",
        "use_cases": [
            "Query requisitions by status, date, or user",
            "Find requisition totals and vendors",
            "Track approval workflow state",
            "Look up change order information"
        ],
        "questions": [
            "What fields are in the requisition header?",
            "How do I find requisitions by status?",
            "What is xxreq_obo (on behalf of)?",
            "Where is the requisition total stored?",
            "How do I identify change orders?"
        ],
        "related": ["xxreqd_det (line items)", "xxreq_audit (approvals)", "xxreq_attach (attachments)"]
    },
    "xxreqd_det": {
        "title": "Requisition Detail/Line Items Table",
        "description": "Stores individual line items within requisitions. Each line has quantity, cost, GL coding, and item details.",
        "use_cases": [
            "Query line items for a requisition",
            "Find line totals and quantities",
            "Look up GL account coding",
            "Analyze spending by cost center"
        ],
        "questions": [
            "What fields are in requisition line items?",
            "How do I find lines for a requisition?",
            "Where is the line total stored?",
            "What is xxreqd_cc (cost center)?"
        ],
        "related": ["xxreq_mstr (header)", "GL account structure"]
    },
    "xxreq_audit": {
        "title": "Requisition Approval Audit Trail Table",
        "description": "Records all approval actions taken on requisitions. Shows who approved/rejected, when, and any comments. Critical for audit and workflow analysis.",
        "use_cases": [
            "Find who approved a requisition",
            "Track approval workflow history",
            "Calculate approval cycle times",
            "Audit approval actions"
        ],
        "questions": [
            "Who approved this requisition?",
            "What is the approval history?",
            "How long did approval take?",
            "What is xxreq_actual_approver vs xxreq_app_id?"
        ],
        "related": ["xxreq_mstr (requisition)", "xxapp_mstr (rules)"]
    },
    "xxapp_mstr": {
        "title": "Simple Approval Rules Table",
        "description": "Stores simple approval rules using AND logic. The primary table for configuring approval routing based on amount, cost center, account, and other criteria.",
        "use_cases": [
            "Query approval rules",
            "Find who approves for specific criteria",
            "Check approval thresholds",
            "Debug approval routing"
        ],
        "questions": [
            "What fields are in the approval rules table?",
            "How do I find rules by cost center?",
            "What is xxapp_seq (sequence)?",
            "How do amount thresholds work?",
            "What does xxapp_which_cost mean?"
        ],
        "related": ["xxAppRule (complex rules)", "xxAppField (conditions)", "xxreq_audit (history)"]
    },
    "xxAppRule": {
        "title": "Complex Approval Rules Table",
        "description": "Stores complex approval rules with nested AND/OR logic. Used for advanced routing scenarios that simple rules cannot handle.",
        "use_cases": [
            "Query complex approval rules",
            "Find rules with OR conditions",
            "Debug advanced routing logic"
        ],
        "questions": [
            "When should I use complex vs simple rules?",
            "How do complex rules work?",
            "What is xxAR_Approver?",
            "How do I use $SUPERVISORS variable?"
        ],
        "related": ["xxAppField (conditions)", "xxapp_mstr (simple rules)"]
    },
    "xxAppField": {
        "title": "Complex Rule Conditions Table",
        "description": "Stores the conditions for complex approval rules. Forms a tree structure with AND/OR operators linking field comparisons.",
        "use_cases": [
            "Query rule conditions",
            "Understand rule logic tree",
            "Debug why rules match or don't match"
        ],
        "questions": [
            "How are complex rule conditions structured?",
            "What is xxAF_Parent?",
            "How does the condition tree work?"
        ],
        "related": ["xxAppRule (rule header)"]
    }
}

def generate_table_section(table_name, original_content, metadata):
    """Generate verbose section for a table"""
    output = []
    
    # Title with table name
    title = metadata.get("title", f"{table_name} Table")
    output.append(f"## {table_name} - {title}\n")
    
    # Description
    desc = metadata.get("description", "")
    if desc:
        output.append(f"{desc}\n")
    
    # Use cases
    use_cases = metadata.get("use_cases", [])
    if use_cases:
        output.append("\n**Use this table when you need to:**")
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
    
    # Related tables
    related = metadata.get("related", [])
    if related:
        output.append(f"**Related tables:** {', '.join(related)}\n")
    
    # Original content (fields, indexes)
    output.append(original_content)
    
    return "\n".join(output)

def parse_schema_file(filepath):
    """Parse the schema file into sections by table"""
    with open(filepath, 'r') as f:
        content = f.read()
    
    # Split by ### headers (table names)
    sections = re.split(r'^(### \w+)', content, flags=re.MULTILINE)
    
    tables = {}
    current_table = None
    
    for i, section in enumerate(sections):
        if section.startswith('### '):
            current_table = section.replace('### ', '').strip()
        elif current_table:
            tables[current_table] = section.strip()
            current_table = None
    
    return tables

def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    repo_root = os.path.dirname(script_dir)
    
    input_file = os.path.join(repo_root, "reference", "database-schema.md")
    output_file = os.path.join(repo_root, "rag-optimized", "database-schema-rag.md")
    
    print(f"Reading: {input_file}")
    tables = parse_schema_file(input_file)
    
    output = []
    output.append("# Database Schema Reference (RAG-Optimized)\n")
    output.append("> This file is auto-generated for AI/RAG vector search optimization.")
    output.append("> Do not edit directly. Edit `reference/database-schema.md` and regenerate.\n")
    output.append("This document describes the iPurchase database tables, fields, and relationships.\n")
    
    for table_name, content in tables.items():
        metadata = TABLE_CONTEXT.get(table_name, {})
        if metadata:
            # Has custom metadata - generate verbose section
            section = generate_table_section(table_name, content, metadata)
        else:
            # No custom metadata - use original with just header upgrade
            section = f"## {table_name}\n\n{content}"
        
        output.append(section)
        output.append("\n---\n")
    
    # Write output
    os.makedirs(os.path.dirname(output_file), exist_ok=True)
    with open(output_file, 'w') as f:
        f.write("\n".join(output))
    
    print(f"Generated: {output_file}")
    print(f"Tables processed: {len(tables)}")
    print(f"Tables with custom context: {len([t for t in tables if t in TABLE_CONTEXT])}")

if __name__ == "__main__":
    main()
