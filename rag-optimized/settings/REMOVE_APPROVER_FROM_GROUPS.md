# REMOVE_APPROVER_FROM_GROUPS - iPurchase System Setting

**Category:** Approval Workflow

TRUE | FALSE.

### Valid Values

| Value | Behavior |
|-------|----------|
| **TRUE** | removes approver from later groups if they already approved |
| **FALSE** | Disables this feature |

### How It Works

This setting affects the approval workflow process, determining how requisitions are routed and approved.

### Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | REMOVE_APPROVER_FROM_GROUPS |
| **Category** | Approval Workflow |
| **Owner** | Admin |
| **Default Value** | FALSE |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'REMOVE_APPROVER_FROM_GROUPS'
```

### Related Settings

- [REMOVE_APPROVER_ROLE_LIST](REMOVE_APPROVER_ROLE_LIST.md)
- [REMOVE_ORIGINATOR_FROM_GROUP_CO](REMOVE_ORIGINATOR_FROM_GROUP_CO.md)