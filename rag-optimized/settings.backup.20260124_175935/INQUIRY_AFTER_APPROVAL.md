# INQUIRY_AFTER_APPROVAL - iPurchase System Setting

**Category:** Approval Workflow

Comma separated list of User ID's or group id's that are re-directed to the pending queue once they have approved a requisition. Asterisk indicates everyone, a blank indicates no one. This setting ...

**Common questions this answers:**
- What is INQUIRY_AFTER_APPROVAL?
- What does INQUIRY_AFTER_APPROVAL do?
- What is the default value for INQUIRY_AFTER_APPROVAL?
- How do I configure INQUIRY_AFTER_APPROVAL?
- How does INQUIRY_AFTER_APPROVAL affect approval routing?

## Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | INQUIRY_AFTER_APPROVAL |
| **Category** | Approval Workflow |
| **Owner** | Power Users |
| **Default Value** | * |

## How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'INQUIRY_AFTER_APPROVAL'
```
