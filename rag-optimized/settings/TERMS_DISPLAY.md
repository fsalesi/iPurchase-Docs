# TERMS_DISPLAY - iPurchase System Setting

**Category:** Uncategorized

This setting will display the supplier terms on the requisition header.

### Valid Values

| Value | Behavior |
|-------|----------|
| **TRUE** | Enables this feature |
| **FALSE** | Disables this feature |

### How It Works

This setting configures uncategorized behavior in iPurchase.

### Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | TERMS_DISPLAY |
| **Category** | Uncategorized |
| **Owner** | Purchasing |
| **Default Value** | TRUE |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'TERMS_DISPLAY'
```