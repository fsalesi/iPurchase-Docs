# ALLOW_APPROVAL_SIMULATION - iPurchase System Setting

**Category:** Approval Workflow

Comma separated list of User ID's or Group ID's that are allowed to view an Approval Simulation. Asterisk indicates everyone, a blank indicates no one.

**Common questions this answers:**
- What is ALLOW_APPROVAL_SIMULATION?
- What does ALLOW_APPROVAL_SIMULATION do?
- What is the default value for ALLOW_APPROVAL_SIMULATION?
- How do I configure ALLOW_APPROVAL_SIMULATION?
- How does ALLOW_APPROVAL_SIMULATION affect approval routing?

## Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | ALLOW_APPROVAL_SIMULATION |
| **Category** | Approval Workflow |
| **Owner** | Admin |
| **Default Value** | * |

## How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'ALLOW_APPROVAL_SIMULATION'
```
