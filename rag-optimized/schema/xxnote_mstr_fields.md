# xxnote_mstr - Notes Master Table - Fields

Stores notes and comments with optional file attachments. Can be linked to requisitions and other records.

**Common questions this answers:**
- What fields are in the xxnote_mstr table?

**Related tables:** xxreq_mstr (requisitions)

### Fields

| Field | Type | Flags | Description |
|-------|------|:-----:|-------------|
| `oid_xxnote_mstr` | deci-2 |  |  |
| `xxnote_datetime` | datetm-tz | i |  |
| `xxnot_userid` | char |  |  |
| `xxnote_comment` | char |  |  |
| `xxnote_ref` | deci-2 | i |  |
| `xxnote_file` | blob |  |  |
| `xxnote_filename` | char |  |  |
| `xxnote_internal` | logi |  |  |
| `xxnote_security` | char |  |  |
| `xxnote_type` | char |  |  |
| `xxnote_field` | char |  |  |
| `xxnote_label` | char |  |  |