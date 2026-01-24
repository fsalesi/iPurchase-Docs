# CART_SUM_LINES - iPurchase System Setting

**Category:** Uncategorized

Within a catalog requisition, iPurchase will add up the quantities of all the items chosen by default.  If the administrator sets this setting to true the system will display number of lines instea...

**Common questions this answers:**
- What is CART_SUM_LINES?
- What does CART_SUM_LINES do?
- What is the default value for CART_SUM_LINES?
- How do I configure CART_SUM_LINES?

## Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | CART_SUM_LINES |
| **Category** | Uncategorized |
| **Owner** | Admin |
| **Default Value** | False  |

## How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'CART_SUM_LINES'
```
