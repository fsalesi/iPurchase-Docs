# LINE_VIEW_FIELDS - iPurchase System Setting

**Category:** User Management

System default for which fields are displayed in the Requisition Item browse.

**Common questions this answers:**
- What is LINE_VIEW_FIELDS?
- What does LINE_VIEW_FIELDS do?
- What is the default value for LINE_VIEW_FIELDS?
- How do I configure LINE_VIEW_FIELDS?

## Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | LINE_VIEW_FIELDS |
| **Category** | User Management |
| **Owner** | Power Users |
| **Default Value** | xxreqd_line_type:LT:1,full_item:Item:45,xxreqd_due_date:Due::center,xxreqd_acct::15:center,xxreqd_project,xxreqd_qty,xxreqd_cost |

## How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'LINE_VIEW_FIELDS'
```
