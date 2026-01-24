# ALLOW_RETRANSMIT_PO - iPurchase System Setting

**Category:** User Management

Comma separated list of User ID's or Group ID's that allow user to manually transmit cXML PO to Punchout supplier.  Asterisk indicates everyone, a blank indicates no one.

**Common questions this answers:**
- What is ALLOW_RETRANSMIT_PO?
- What does ALLOW_RETRANSMIT_PO do?
- What is the default value for ALLOW_RETRANSMIT_PO?
- How do I configure ALLOW_RETRANSMIT_PO?

## Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | ALLOW_RETRANSMIT_PO |
| **Category** | User Management |
| **Owner** | Admin |
| **Default Value** | buyers |

## How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'ALLOW_RETRANSMIT_PO'
```
