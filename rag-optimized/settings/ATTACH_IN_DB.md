# ATTACH_IN_DB - iPurchase System Setting

**Category:** ACH Integration

Store attachments in iPurchase database (True) or store attachments on disk (False).

### How It Works

### Valid Values

| Value | Behavior |
|-------|----------|
| `TRUE` | Enabled |
| `FALSE` | Disabled |

### Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | ATTACH_IN_DB |
| **Category** | ACH Integration |
| **Owner** | IT |
| **Default Value** | TRUE |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'ATTACH_IN_DB'
```
