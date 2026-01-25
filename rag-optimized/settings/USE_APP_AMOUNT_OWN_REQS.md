# USE_APP_AMOUNT_OWN_REQS - iPurchase System Setting

**Category:** Approval Workflow

Controls whether users can approve their own requisitions when the requisition amount is within their approval limit. This setting determines if a requisition can automatically convert to a PO without additional approvals when the originator has sufficient approval authority.

### How It Works

When a user submits a requisition and their approval amount (wus_app_amt) exceeds the requisition total, this setting determines whether the requisition:
- Automatically converts to a PO (if enabled and no other approval rules apply)
- Still requires supervisor approval (if disabled)

If the requisition has an "On Behalf Of" user specified, the OBO user's approval limit is used instead of the originator's.

### Valid Values

This setting uses [Can-Do list format](../../reference/can-do-list-format.md).

| Value | Behavior |
|-------|----------|
| `*` (asterisk) | Everyone can self-approve within their limit |
| Blank/empty | No one can self-approve - always requires supervisor |
| User/Group list | Only specified users or group members can self-approve |

### Important Notes

- Only applies to supervisory approval rules (rules using $SUPERVISORS)
- If other approval rules add approvers (e.g., CFO rule, cost center owner), the PO will not auto-create
- Works in conjunction with the user's wus_app_amt field

### Common Questions

- Can someone approve their own requisition?
- What is USE_APP_AMOUNT_OWN_REQS?
- How do I enable self-approval?
- Why didn't my requisition auto-approve?
- How does approval amount affect self-approval?

### Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | USE_APP_AMOUNT_OWN_REQS |
| **Category** | Approval Workflow |
| **Owner** | Admin |
| **Default Value** | (none) |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'USE_APP_AMOUNT_OWN_REQS'
```

### Related Settings

- [USE_LINE_APPROVALS](USE_LINE_APPROVALS.md)
- [USE_SUPERVISORS_TO_APPROVE](USE_SUPERVISORS_TO_APPROVE.md)
