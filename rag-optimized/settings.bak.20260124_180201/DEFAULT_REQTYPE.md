# DEFAULT_REQTYPE - iPurchase System Setting

**Category:** System Configuration

In this setting the administrator can set the default value for "Requisition Type" field.

**Common questions this answers:**
- What is DEFAULT_REQTYPE?
- What does DEFAULT_REQTYPE do?
- What is the default value for DEFAULT_REQTYPE?
- How do I configure DEFAULT_REQTYPE?

## Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | DEFAULT_REQTYPE |
| **Category** | System Configuration |
| **Owner** | Power Users |
| **Default Value** | (none) |

## How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'DEFAULT_REQTYPE'
```
