# EMAIL_SUPPLIER_PO_TO_FINAL_APPROVER - iPurchase System Setting

**Category:** Approval Workflow

A value of true will send a copy of the supplier email to the final approver when the PO is created.

### Valid Values

| Value | Behavior |
|-------|----------|
| **TRUE** | Enables this feature |
| **FALSE** | Disables this feature |

### How It Works

Configure email recipients for this notification type. Multiple addresses can be comma-separated.

### Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | EMAIL_SUPPLIER_PO_TO_FINAL_APPROVER |
| **Category** | Approval Workflow |
| **Owner** | Power Users |
| **Default Value** | FALSE |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'EMAIL_SUPPLIER_PO_TO_FINAL_APPROVER'
```

### Related Settings

- [EMAIL_NO_APPROVE_LINK](EMAIL_NO_APPROVE_LINK.md)