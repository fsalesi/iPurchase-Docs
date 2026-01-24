# DELIVER_TO_FILL_IN - iPurchase System Setting

**Category:** Uncategorized

Rather than the Deliver To field being a drop down list of users defined in iPurchase, setting this to TRUE makes the deliver to field an non-validated text field.

### How It Works

See the description above for valid values and usage.

### Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | DELIVER_TO_FILL_IN |
| **Category** | Uncategorized |
| **Owner** | Power Users |
| **Default Value** | FALSE |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'DELIVER_TO_FILL_IN'
```
