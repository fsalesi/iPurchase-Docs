# INQUIRY_AFTER_REJECT - iPurchase System Setting

**Category:** Reporting & Inquiry

Comma separated list of User ID's or Group ID's that are re-directed to the pending queue once they have rejected a requisition. Asterisk indicates everyone, a blank indicates no one. This setting ...

**Common questions this answers:**
- What is INQUIRY_AFTER_REJECT?
- What does INQUIRY_AFTER_REJECT do?
- What is the default value for INQUIRY_AFTER_REJECT?
- How do I configure INQUIRY_AFTER_REJECT?

## Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | INQUIRY_AFTER_REJECT |
| **Category** | Reporting & Inquiry |
| **Owner** | Power Users |
| **Default Value** | * |

## How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'INQUIRY_AFTER_REJECT'
```
