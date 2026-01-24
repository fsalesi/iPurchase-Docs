# DEFAULT_LINES_TO_APPROVED_AUTO - iPurchase System Setting

**Category:** Approval Workflow

Comma-Separated List of User ID's or Group ID's. If setting DEFAULT_LINES_TO_APPROVED is set to false, then adding a user or group to this setting will automatically approve any line items which ar...

**Common questions this answers:**
- What is DEFAULT_LINES_TO_APPROVED_AUTO?
- What does DEFAULT_LINES_TO_APPROVED_AUTO do?
- What is the default value for DEFAULT_LINES_TO_APPROVED_AUTO?
- How do I configure DEFAULT_LINES_TO_APPROVED_AUTO?
- How does DEFAULT_LINES_TO_APPROVED_AUTO affect approval routing?

## Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | DEFAULT_LINES_TO_APPROVED_AUTO |
| **Category** | Approval Workflow |
| **Owner** | Admin |
| **Default Value** | (none) |

## How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'DEFAULT_LINES_TO_APPROVED_AUTO'
```
