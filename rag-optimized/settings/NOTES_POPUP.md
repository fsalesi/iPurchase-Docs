# NOTES_POPUP - iPurchase System Setting

**Category:** System Configuration

TRUE | FALSE.

### Valid Values

| Value | Behavior |
|-------|----------|
| **TRUE** | displays notes in popup window instead of inline |
| **FALSE** | Disables this feature |

### How It Works

This setting configures system configuration behavior in iPurchase.

### Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | NOTES_POPUP |
| **Category** | System Configuration |
| **Owner** | Admin |
| **Default Value** | FALSE |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'NOTES_POPUP'
```