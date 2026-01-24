# PO_LOGO - iPurchase System Setting

**Category:** Purchase Orders

The value of this setting is a path to the physical file name on the app server. Ex. " or apps or iPurchase or logo or frank.jpg". If the logo is in the wdm or agents folder then you only need to p...

**Common questions this answers:**
- What is PO_LOGO?
- What does PO_LOGO do?
- What is the default value for PO_LOGO?
- How do I configure PO_LOGO?

## Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | PO_LOGO |
| **Category** | Purchase Orders |
| **Owner** | Admin |
| **Default Value** | (none) |

## How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'PO_LOGO'
```
