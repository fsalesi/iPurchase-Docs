# UNSPSC_FILTER - iPurchase System Setting

**Category:** Uncategorized

To modify this setting to control which UNSPSC codes are available to choose from. The syntax for this settings uses the CAN-DO functionality similar to a lot of the other settings. To re-cap, the ...

**Common questions this answers:**
- What is UNSPSC_FILTER?
- What does UNSPSC_FILTER do?
- What is the default value for UNSPSC_FILTER?
- How do I configure UNSPSC_FILTER?

## Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | UNSPSC_FILTER |
| **Category** | Uncategorized |
| **Owner** | Purchasing |
| **Default Value** | * |

## How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'UNSPSC_FILTER'
```
