# SKIP_QAD_ACTIVE_CHECK - iPurchase System Setting

**Category:** QAD Integration

True or False Do not check the QAD user's active flag. Normally a user (if the QAD User ID matches the iPurchase User ID) needs to be active in QAD in order to login to iPurchase. This does not alw...

**Common questions this answers:**
- What is SKIP_QAD_ACTIVE_CHECK?
- What does SKIP_QAD_ACTIVE_CHECK do?
- What is the default value for SKIP_QAD_ACTIVE_CHECK?
- How do I configure SKIP_QAD_ACTIVE_CHECK?

## Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | SKIP_QAD_ACTIVE_CHECK |
| **Category** | QAD Integration |
| **Owner** | Admin |
| **Default Value** | TRUE |

## How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'SKIP_QAD_ACTIVE_CHECK'
```
