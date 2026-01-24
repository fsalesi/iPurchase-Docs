#!/usr/bin/env python3
"""
Generate individual RAG pages for each database table.
Each table gets two files: one for fields, one for indexes.
"""

import os
import re

# Table metadata - descriptions and common questions
TABLE_META = {
    "wus_mstr": {
        "title": "User Master Table",
        "description": "Stores all user accounts, profiles, and settings for iPurchase. Contains login credentials, approval limits, supervisor relationships, delegates, and user preferences.",
        "questions": [
            "What fields are in the wus_mstr table?",
            "What fields are in the user master table?",
            "How do I find a user's supervisor?",
            "Where is the user approval limit stored?",
            "What is wus_delegate?",
            "How do I check if a user is disabled?",
            "What is the user ID field?",
            "How do I find a user by email?"
        ],
        "related": ["wgr_mstr (groups)", "wugr_mstr (group membership)", "pf_mstr (user preferences)"]
    },
    "wgr_mstr": {
        "title": "Group Master Table",
        "description": "Defines groups used for approval routing, permissions, and organizational structure. Groups can be referenced in approval rules as approvers.",
        "questions": [
            "What fields are in the wgr_mstr table?",
            "What fields are in the group master table?",
            "How are groups defined?",
            "What is wgr_id?",
            "How do I list all groups?"
        ],
        "related": ["wugr_mstr (membership)", "xxapp_mstr (approval rules)", "wus_mstr (users)"]
    },
    "wugr_mstr": {
        "title": "User-Group Membership Table",
        "description": "Links users to groups. Each record represents one user belonging to one group. Used to determine group membership for approval routing.",
        "questions": [
            "What fields are in the wugr_mstr table?",
            "What fields are in the user-group membership table?",
            "How do I find all members of a group?",
            "What groups does a user belong to?",
            "How is group membership stored?"
        ],
        "related": ["wus_mstr (users)", "wgr_mstr (groups)"]
    },
    "pf_mstr": {
        "title": "Parameter/Settings Master Table",
        "description": "Stores all system settings, user preferences, and configuration parameters. The central configuration table for iPurchase. Query with pf_us_id='SYSTEM' and pf_group='DEFAULT' for system settings.",
        "questions": [
            "What fields are in the pf_mstr table?",
            "What fields are in the settings table?",
            "Where are system settings stored?",
            "How do I find a specific setting value?",
            "What is pf_chr1?",
            "How do I query settings by attribute name?"
        ],
        "related": ["System Settings Reference documentation"]
    },
    "xxreq_mstr": {
        "title": "Requisition Header Table",
        "description": "The main requisition table containing header-level information: status, dates, totals, vendor, buyer, and workflow state. Every requisition has one record here. Primary key is domain + requisition number.",
        "questions": [
            "What fields are in the xxreq_mstr table?",
            "What fields are in the requisition header table?",
            "How do I find requisitions by status?",
            "What is xxreq_obo (on behalf of)?",
            "Where is the requisition total stored?",
            "How do I identify change orders?",
            "What is xxreq_status?",
            "How do I find requisitions by user?"
        ],
        "related": ["xxreqd_det (line items)", "xxreq_audit (approvals)", "xxreq_attach (attachments)"]
    },
    "xxreqd_det": {
        "title": "Requisition Detail/Line Items Table",
        "description": "Stores individual line items within requisitions. Each line has quantity, cost, GL coding (account, cost center, sub-account, project), and item details.",
        "questions": [
            "What fields are in the xxreqd_det table?",
            "What fields are in the requisition line items table?",
            "How do I find lines for a requisition?",
            "Where is the line total stored?",
            "What is xxreqd_cc (cost center)?",
            "How do I find lines by account?",
            "What is xxreqd_total_gl?"
        ],
        "related": ["xxreq_mstr (header)", "GL account coding"]
    },
    "xxreq_audit": {
        "title": "Requisition Approval Audit Trail Table",
        "description": "Records all approval actions taken on requisitions. Shows who approved/rejected, when, and any comments. Critical for audit compliance and workflow analysis.",
        "questions": [
            "What fields are in the xxreq_audit table?",
            "What fields are in the approval audit table?",
            "Who approved this requisition?",
            "What is the approval history?",
            "How long did approval take?",
            "What is xxreq_actual_approver vs xxreq_app_id?",
            "How do I find pending approvals?"
        ],
        "related": ["xxreq_mstr (requisition)", "xxapp_mstr (rules)", "wus_mstr (users)"]
    },
    "xxreq_attach": {
        "title": "Requisition Attachments Table",
        "description": "Stores file attachments linked to requisitions. Contains attachment metadata and the file content as a BLOB.",
        "questions": [
            "What fields are in the xxreq_attach table?",
            "What fields are in the requisition attachments table?",
            "How do I find attachments for a requisition?",
            "Where are requisition files stored?",
            "What is xxreq_file?"
        ],
        "related": ["xxreq_mstr (requisition)", "BLOB extraction tools"]
    },
    "xxapp_mstr": {
        "title": "Simple Approval Rules Table",
        "description": "Stores simple approval rules using AND logic. The primary table for configuring approval routing based on amount, cost center, account, and other criteria. Recommended for most approval routing scenarios.",
        "questions": [
            "What fields are in the xxapp_mstr table?",
            "What fields are in the simple approval rules table?",
            "How do I find approval rules by cost center?",
            "What is xxapp_seq (sequence)?",
            "How do amount thresholds work?",
            "What does xxapp_which_cost mean?",
            "How do I find rules for a specific approver?",
            "What is xxapp_id?"
        ],
        "related": ["xxAppRule (complex rules)", "xxAppField (conditions)", "xxreq_audit (history)"]
    },
    "xxAppRule": {
        "title": "Complex Approval Rules Table",
        "description": "Stores complex approval rules with nested AND/OR logic. Used for advanced routing scenarios that simple rules cannot handle. Rule conditions are stored in xxAppField.",
        "questions": [
            "What fields are in the xxAppRule table?",
            "What fields are in the complex approval rules table?",
            "When should I use complex vs simple rules?",
            "How do complex rules work?",
            "What is xxAR_Approver?",
            "How do I use $SUPERVISORS variable?"
        ],
        "related": ["xxAppField (conditions)", "xxapp_mstr (simple rules)"]
    },
    "xxAppField": {
        "title": "Complex Rule Conditions Table",
        "description": "Stores the conditions for complex approval rules. Forms a hierarchical tree structure with AND/OR operators linking field comparisons.",
        "questions": [
            "What fields are in the xxAppField table?",
            "What fields are in the rule conditions table?",
            "How are complex rule conditions structured?",
            "What is xxAF_Parent?",
            "How does the condition tree work?"
        ],
        "related": ["xxAppRule (rule header)"]
    },
    "xxpo_archive": {
        "title": "PO Archive Table",
        "description": "Stores archived Purchase Order PDF documents as BLOBs. Each PO can have multiple revisions stored.",
        "questions": [
            "What fields are in the xxpo_archive table?",
            "Where are PO PDFs stored?",
            "How do I find archived POs?",
            "What is xxpoa_pdf?",
            "How do I download a PO PDF?"
        ],
        "related": ["BLOB extraction tools", "po_mstr (QAD PO header)"]
    },
    "xxnote_mstr": {
        "title": "Notes Master Table",
        "description": "Stores notes and comments with optional file attachments. Can be linked to requisitions and other records.",
        "questions": [
            "What fields are in the xxnote_mstr table?",
            "Where are notes stored?",
            "How do I find notes for a requisition?"
        ],
        "related": ["xxreq_mstr (requisitions)"]
    },
    "xxmaild_det": {
        "title": "Email Detail Table",
        "description": "Stores email detail records including attachments for outbound notifications.",
        "questions": [
            "What fields are in the xxmaild_det table?",
            "Where are email attachments stored?",
            "How do I find emails for a requisition?"
        ],
        "related": ["xxmail_mstr (email header)"]
    },
    "xxloc_mstr": {
        "title": "Location Master Table",
        "description": "Location/site master defining valid ship-to and bill-to locations for requisitions.",
        "questions": [
            "What fields are in the xxloc_mstr table?",
            "What fields are in the location table?",
            "How do I find valid ship-to locations?",
            "How do I find valid bill-to locations?"
        ],
        "related": ["xxreq_mstr (requisitions)"]
    },
    "xxmail_mstr": {
        "title": "Email Queue Header Table",
        "description": "Email queue header records for outbound notifications. Tracks email status and delivery.",
        "questions": [
            "What fields are in the xxmail_mstr table?",
            "Where is the email queue?",
            "How do I find pending emails?"
        ],
        "related": ["xxmaild_det (email details)"]
    }
}

def parse_schema_file(filepath):
    """Parse the schema file into individual table sections"""
    with open(filepath, 'r') as f:
        content = f.read()
    
    # Find all ### table sections
    pattern = r'^### (\w+)\n(.*?)(?=^### |\Z)'
    matches = re.findall(pattern, content, re.MULTILINE | re.DOTALL)
    
    tables = {}
    for table_name, table_content in matches:
        tables[table_name] = table_content.strip()
    
    return tables

def extract_fields_and_indexes(content):
    """Extract fields table and indexes table from content"""
    # Split on #### headers
    parts = re.split(r'^#### (Fields|Indexes)\n', content, flags=re.MULTILINE)
    
    description = parts[0].strip() if parts else ""
    fields_table = ""
    indexes_table = ""
    
    i = 1
    while i < len(parts):
        section_name = parts[i]
        section_content = parts[i+1] if i+1 < len(parts) else ""
        
        # Extract just the table
        table_match = re.search(r'(\|[^\n]+\|\n)+', section_content)
        if table_match:
            if section_name == "Fields":
                fields_table = table_match.group(0).strip()
            elif section_name == "Indexes":
                indexes_table = table_match.group(0).strip()
        i += 2
    
    return description, fields_table, indexes_table

def generate_fields_page(table_name, description, fields_table, meta):
    """Generate the fields page for a table"""
    title = meta.get("title", f"{table_name} Table")
    full_desc = meta.get("description", description)
    questions = meta.get("questions", [])
    related = meta.get("related", [])
    
    # Filter questions to fields-related ones
    field_questions = [q for q in questions if "field" in q.lower() or "what is" in q.lower() or table_name.lower() in q.lower()]
    if not field_questions:
        field_questions = questions[:4]  # Take first 4 if no field questions
    
    output = []
    output.append(f"# {table_name} - {title} - Fields\n")
    output.append(f"{full_desc}\n")
    
    if field_questions:
        output.append("**Common questions this answers:**")
        for q in field_questions:
            output.append(f"- {q}")
        output.append("")
    
    if related:
        output.append(f"**Related tables:** {', '.join(related)}\n")
    
    output.append("## Fields\n")
    output.append(fields_table)
    
    return "\n".join(output)

def generate_indexes_page(table_name, indexes_table, meta):
    """Generate the indexes page for a table"""
    title = meta.get("title", f"{table_name} Table")
    
    output = []
    output.append(f"# {table_name} - {title} - Indexes\n")
    output.append(f"Database indexes for the {table_name} table. Use these indexes for efficient queries.\n")
    
    output.append("**Common questions this answers:**")
    output.append(f"- What indexes exist on {table_name}?")
    output.append(f"- How do I query {table_name} efficiently?")
    output.append(f"- What is the primary key of {table_name}?")
    output.append("")
    
    output.append("## Indexes\n")
    output.append(indexes_table)
    
    return "\n".join(output)

def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    repo_root = os.path.dirname(script_dir)
    
    input_file = os.path.join(repo_root, "reference", "database-schema.md")
    output_dir = os.path.join(repo_root, "rag-optimized", "schema")
    
    os.makedirs(output_dir, exist_ok=True)
    
    print(f"Reading: {input_file}")
    tables = parse_schema_file(input_file)
    
    print(f"Found {len(tables)} tables")
    
    max_fields_size = 0
    max_indexes_size = 0
    
    for table_name, content in tables.items():
        description, fields_table, indexes_table = extract_fields_and_indexes(content)
        meta = TABLE_META.get(table_name, {})
        
        # Generate fields page
        if fields_table:
            fields_page = generate_fields_page(table_name, description, fields_table, meta)
            fields_file = os.path.join(output_dir, f"{table_name}_fields.md")
            with open(fields_file, 'w') as f:
                f.write(fields_page)
            
            size = len(fields_page)
            if size > max_fields_size:
                max_fields_size = size
            print(f"  {table_name}_fields.md ({size} chars)")
        
        # Generate indexes page
        if indexes_table:
            indexes_page = generate_indexes_page(table_name, indexes_table, meta)
            indexes_file = os.path.join(output_dir, f"{table_name}_indexes.md")
            with open(indexes_file, 'w') as f:
                f.write(indexes_page)
            
            size = len(indexes_page)
            if size > max_indexes_size:
                max_indexes_size = size
            print(f"  {table_name}_indexes.md ({size} chars)")
    
    print(f"\nMax fields page: {max_fields_size} chars")
    print(f"Max indexes page: {max_indexes_size} chars")
    print(f"Recommended CHUNK_SIZE: {max(max_fields_size, max_indexes_size) + 200}")

if __name__ == "__main__":
    main()
