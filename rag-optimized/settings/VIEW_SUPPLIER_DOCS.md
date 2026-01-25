# VIEW_SUPPLIER_DOCS - iPurchase System Setting

**Category:** User Management

True or False or list of users groups.

### How It Works

This setting configures user management behavior in iPurchase.

### Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | VIEW_SUPPLIER_DOCS |
| **Category** | User Management |
| **Owner** | Admin |
| **Default Value** | buyers,admin |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'VIEW_SUPPLIER_DOCS'
```

### Related Settings

- [VIEW_DEPARTMENT_REQS](VIEW_DEPARTMENT_REQS.md)
- [VIEW_REQS_DEPARTMENT](VIEW_REQS_DEPARTMENT.md)
- [VIEW_REQS_RESTRICTED_MODE](VIEW_REQS_RESTRICTED_MODE.md)