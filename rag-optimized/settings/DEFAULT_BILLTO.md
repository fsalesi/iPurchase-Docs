# DEFAULT_BILLTO - iPurchase System Setting

**Category:** System Configuration

The administrator can enter a default value for the "Bill To" field.

**Common questions this answers:**
- What is DEFAULT_BILLTO?
- What does DEFAULT_BILLTO do?
- What is the default value for DEFAULT_BILLTO?
- How do I configure DEFAULT_BILLTO?

## Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | DEFAULT_BILLTO |
| **Category** | System Configuration |
| **Owner** | Finance |
| **Default Value** | (none) |

## How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'DEFAULT_BILLTO'
```
