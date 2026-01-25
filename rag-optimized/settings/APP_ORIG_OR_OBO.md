# APP_ORIG_OR_OBO - iPurchase System Setting

**Category:** Approval Workflow

ORIGINATOR | OBO.

### How It Works

This setting affects the approval workflow process, determining how requisitions are routed and approved.

### Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | APP_ORIG_OR_OBO |
| **Category** | Approval Workflow |
| **Owner** | Admin |
| **Default Value** | OBO |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'APP_ORIG_OR_OBO'
```

### Related Settings

- [APP_SUPERVISOR_SEQ](APP_SUPERVISOR_SEQ.md)