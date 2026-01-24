# SHOW_INVOICE_INQUIRY - iPurchase System Setting

**Category:** System Configuration

TRUE | FALSE. Show invoice inquiry link.

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
| **Setting Name** | SHOW_INVOICE_INQUIRY |
| **Category** | System Configuration |
| **Owner** | Admin |
| **Default Value** | FALSE |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'SHOW_INVOICE_INQUIRY'
```