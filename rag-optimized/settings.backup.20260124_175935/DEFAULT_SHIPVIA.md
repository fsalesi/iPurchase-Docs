# DEFAULT_SHIPVIA - iPurchase System Setting

**Category:** Purchase Orders

In this setting the administrator can set the default value for "Ship Via" field.

**Common questions this answers:**
- What is DEFAULT_SHIPVIA?
- What does DEFAULT_SHIPVIA do?
- What is the default value for DEFAULT_SHIPVIA?
- How do I configure DEFAULT_SHIPVIA?

## Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | DEFAULT_SHIPVIA |
| **Category** | Purchase Orders |
| **Owner** | Purchasing |
| **Default Value** | (none) |

## How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'DEFAULT_SHIPVIA'
```
