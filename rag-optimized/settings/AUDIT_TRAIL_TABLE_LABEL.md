# AUDIT_TRAIL_TABLE_LABEL - iPurchase System Setting

**Category:** Uncategorized

Technical - Do Not Modify without consulting ISS

### How It Works

See the description above for details on how this setting affects system behavior.

### Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | AUDIT_TRAIL_TABLE_LABEL |
| **Category** | Uncategorized |
| **Owner** | ISS |
| **Default Value** | ,Requisition Detail,Requisition Header,Rule Field,Rule Header,System Settings,Group Master,User Group Relations,User Master |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'AUDIT_TRAIL_TABLE_LABEL'
```