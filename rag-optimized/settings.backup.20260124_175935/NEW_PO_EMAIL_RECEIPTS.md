# NEW_PO_EMAIL_RECEIPTS - iPurchase System Setting

**Category:** Email Configuration

This setting determines if delivery receipts and read receipts are requested from the recipient's mail server when the email which includes the new PO attached is sent. To turn off this functionali...

**Common questions this answers:**
- What is NEW_PO_EMAIL_RECEIPTS?
- What does NEW_PO_EMAIL_RECEIPTS do?
- What is the default value for NEW_PO_EMAIL_RECEIPTS?
- How do I configure NEW_PO_EMAIL_RECEIPTS?
- How does NEW_PO_EMAIL_RECEIPTS affect email notifications?

## Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | NEW_PO_EMAIL_RECEIPTS |
| **Category** | Email Configuration |
| **Owner** | Purchasing |
| **Default Value** | no,no |

## How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'NEW_PO_EMAIL_RECEIPTS'
```
