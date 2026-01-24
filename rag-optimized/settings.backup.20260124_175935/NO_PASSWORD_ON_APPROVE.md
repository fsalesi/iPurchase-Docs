# NO_PASSWORD_ON_APPROVE - iPurchase System Setting

**Category:** Security & Authentication

Comma separated list of User ID's or Group ID's that will not be prompted for their password when approving or rejecting a requisition.  Asterisk indicates everyone, a blank indicates no one.

**Common questions this answers:**
- What is NO_PASSWORD_ON_APPROVE?
- What does NO_PASSWORD_ON_APPROVE do?
- What is the default value for NO_PASSWORD_ON_APPROVE?
- How do I configure NO_PASSWORD_ON_APPROVE?
- How does NO_PASSWORD_ON_APPROVE affect approval routing?

## Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | NO_PASSWORD_ON_APPROVE |
| **Category** | Security & Authentication |
| **Owner** | Admin |
| **Default Value** | (none) |

## How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'NO_PASSWORD_ON_APPROVE'
```
