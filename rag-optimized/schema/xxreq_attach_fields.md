# xxreq_attach - Requisition Attachments Table - Fields

Stores file attachments linked to requisitions. Contains attachment metadata and the file content as a BLOB.

**Common questions this answers:**
- What fields are in the xxreq_attach table?
- What fields are in the requisition attachments table?
- What is xxreq_file?

**Related tables:** xxreq_mstr (requisition), BLOB extraction tools

## Fields

| Field | Type | Flags | Description |
|-------|------|:-----:|-------------|
| `xxreq_domain` | char | i | Domain/company code |
| `xxreq_nbr` | char | i | Requisition number |
| `xxreq_filename` | char | i |  |
| `xxreq_line` | inte | i |  |
| `xxreq_os_filename` | char |  |  |
| `xxreq_int_ext` | logi |  |  |
| `xxreq_security` | char |  |  |
| `xxreq_file` | blob |  | BLOB file data |
| `xxreq_user` | char |  |  |
| `xxreq_date` | datetm-tz |  | Need-by date |