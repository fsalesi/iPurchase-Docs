# VIEW_DEPARTMENT_REQS - iPurchase System Setting

**Category:** User Management

TRUE | FALSE.

### Valid Values

| Value | Behavior |
|-------|----------|
| **TRUE** | Enables this feature |
| **FALSE** | Disables this feature |

### How It Works

This setting configures user management behavior in iPurchase.

### Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | VIEW_DEPARTMENT_REQS |
| **Category** | User Management |
| **Owner** | Admin |
| **Default Value** | FALSE |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'VIEW_DEPARTMENT_REQS'
```

### Related Settings

- [VIEW_REQS_DEPARTMENT](VIEW_REQS_DEPARTMENT.md)
- [VIEW_REQS_RESTRICTED_MODE](VIEW_REQS_RESTRICTED_MODE.md)
- [VIEW_SUPPLIER_DOCS](VIEW_SUPPLIER_DOCS.md)