# AUDIT_XXREQ_MSTR_EXCEPT - iPurchase System Setting

**Category:** Requisitions

Technical - Do Not Modify without consulting ISS

**Common questions this answers:**
- What is AUDIT_XXREQ_MSTR_EXCEPT?
- What does AUDIT_XXREQ_MSTR_EXCEPT do?
- What is the default value for AUDIT_XXREQ_MSTR_EXCEPT?
- How do I configure AUDIT_XXREQ_MSTR_EXCEPT?

## Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | AUDIT_XXREQ_MSTR_EXCEPT |
| **Category** | Requisitions |
| **Owner** | ISS |
| **Default Value** | xxreq_cost,xxreq_word_idx,xxreq_word_idx2,xxreq_word_idx3,xxreq_master_comments,xxreq_submit_date,xxreq_submit_attempts,xxreq_submit_date,xxreq_approved,xxreq_app_by,xxreq_submitted |

## How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'AUDIT_XXREQ_MSTR_EXCEPT'
```
