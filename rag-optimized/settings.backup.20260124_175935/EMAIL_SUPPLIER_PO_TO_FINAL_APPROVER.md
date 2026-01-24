# EMAIL_SUPPLIER_PO_TO_FINAL_APPROVER - iPurchase System Setting

**Category:** Approval Workflow

A value of true will send a copy of the supplier email to the final approver when the PO is created.

**Common questions this answers:**
- What is EMAIL_SUPPLIER_PO_TO_FINAL_APPROVER?
- What does EMAIL_SUPPLIER_PO_TO_FINAL_APPROVER do?
- What is the default value for EMAIL_SUPPLIER_PO_TO_FINAL_APPROVER?
- How do I configure EMAIL_SUPPLIER_PO_TO_FINAL_APPROVER?
- How does EMAIL_SUPPLIER_PO_TO_FINAL_APPROVER affect approval routing?
- How does EMAIL_SUPPLIER_PO_TO_FINAL_APPROVER affect email notifications?

## Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | EMAIL_SUPPLIER_PO_TO_FINAL_APPROVER |
| **Category** | Approval Workflow |
| **Owner** | Power Users |
| **Default Value** | FALSE |

## How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'EMAIL_SUPPLIER_PO_TO_FINAL_APPROVER'
```
