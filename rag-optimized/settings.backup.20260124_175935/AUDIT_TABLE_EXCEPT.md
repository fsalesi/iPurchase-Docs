# AUDIT_TABLE_EXCEPT - iPurchase System Setting

**Category:** System Configuration

Comma-separated field names. Fields to exclude from audit trail for the specified table. Replace {TABLE} with actual table name (e.g., AUDIT_xxreq_mstr_EXCEPT). Used to reduce audit trail volume.

**Common questions this answers:**
- What is AUDIT_TABLE_EXCEPT?
- What does AUDIT_TABLE_EXCEPT do?
- What is the default value for AUDIT_TABLE_EXCEPT?
- How do I configure AUDIT_TABLE_EXCEPT?

## Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | AUDIT_TABLE_EXCEPT |
| **Category** | System Configuration |
| **Owner** | Admin |
| **Default Value** | (none) |

## How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'AUDIT_TABLE_EXCEPT'
```
