# ATTACH_IN_DB - iPurchase System Setting

**Category:** ACH Integration

Store attachments in iPurchase database (True) or store attachments on disk (False).

### Valid Values

| Value | Behavior |
|-------|----------|
| **TRUE** | Enables this feature |
| **FALSE** | Disables this feature |

### How It Works

See the description above for details on how this setting affects system behavior.

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