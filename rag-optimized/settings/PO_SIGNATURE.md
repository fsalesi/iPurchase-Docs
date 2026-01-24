# PO_SIGNATURE - iPurchase System Setting

**Category:** Purchase Orders

The value of this setting is a path to the physical file name on the app server. Ex " or apps or iPurchase or signatures or frank.jpg". If the signature is in the wdm or agents folder then you only...

**Common questions this answers:**
- What is PO_SIGNATURE?
- What does PO_SIGNATURE do?
- What is the default value for PO_SIGNATURE?
- How do I configure PO_SIGNATURE?

## Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | PO_SIGNATURE |
| **Category** | Purchase Orders |
| **Owner** | Admin |
| **Default Value** | (none) |

## How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'PO_SIGNATURE'
```
