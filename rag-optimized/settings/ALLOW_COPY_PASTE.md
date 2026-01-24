# ALLOW_COPY_PASTE - iPurchase System Setting

**Category:** User Management

This settings controls if users can copy paste in the requisition workbench. Sometimes copying from internet or PDF files cause item number

### How It Works

See the description above for details on how this setting affects system behavior.

### Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | ALLOW_COPY_PASTE |
| **Category** | User Management |
| **Owner** | description |
| **Default Value** | true |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'ALLOW_COPY_PASTE'
```