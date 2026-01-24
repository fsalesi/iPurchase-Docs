# xxpo_archive - PO Archive Table - Fields

Stores archived Purchase Order PDF documents as BLOBs. Each PO can have multiple revisions stored.

**Common questions this answers:**
- What fields are in the xxpo_archive table?
- What is xxpoa_pdf?

**Related tables:** BLOB extraction tools, po_mstr (QAD PO header)

## Fields

| Field | Type | Flags | Description |
|-------|------|:-----:|-------------|
| `xxpoa_domain` | char | i | Domain code |
| `xxpoa_nbr` | char | i | PO number |
| `xxpoa_datetime` | datetm-tz |  | Archive timestamp |
| `xxpoa_user` | char |  | User who archived |
| `xxpoa_rev` | deci-2 | i | Revision number |
| `xxpoa_pdf` | blob |  | BLOB PDF data |
| `xxpoa_os_file` | char |  |  |