# AUDIT_TRAIL_TABLE_LABEL - iPurchase System Setting

**Category:** Uncategorized

Technical - Do Not Modify without consulting ISS

**Common questions this answers:**
- What is AUDIT_TRAIL_TABLE_LABEL?
- What does AUDIT_TRAIL_TABLE_LABEL do?
- What is the default value for AUDIT_TRAIL_TABLE_LABEL?
- How do I configure AUDIT_TRAIL_TABLE_LABEL?

## Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | AUDIT_TRAIL_TABLE_LABEL |
| **Category** | Uncategorized |
| **Owner** | ISS |
| **Default Value** | ,Requisition Detail,Requisition Header,Rule Field,Rule Header,System Settings,Group Master,User Group Relations,User Master |

## How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'AUDIT_TRAIL_TABLE_LABEL'
```
