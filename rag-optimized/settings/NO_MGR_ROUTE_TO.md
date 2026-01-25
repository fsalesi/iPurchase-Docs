# NO_MGR_ROUTE_TO - iPurchase System Setting

**Category:** Approval Workflow

User/group.

### How It Works

This setting affects the approval workflow process, determining how requisitions are routed and approved.

### Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | NO_MGR_ROUTE_TO |
| **Category** | Approval Workflow |
| **Owner** | Admin |
| **Default Value** | (none) |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'NO_MGR_ROUTE_TO'
```

### Related Settings

- [NO_APPROVAL_EMAILS](NO_APPROVAL_EMAILS.md)