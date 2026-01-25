# NO_APPROVAL_EMAILS - iPurchase System Setting

**Category:** Approval Workflow

Comma separated list of requisition types that will not send approval emails to approvers.

### How It Works

This email-related setting controls how iPurchase communicates with users via email notifications.

### Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | NO_APPROVAL_EMAILS |
| **Category** | Approval Workflow |
| **Owner** | Admin |
| **Default Value** | (none) |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'NO_APPROVAL_EMAILS'
```

### Related Settings

- [NO_MGR_ROUTE_TO](NO_MGR_ROUTE_TO.md)