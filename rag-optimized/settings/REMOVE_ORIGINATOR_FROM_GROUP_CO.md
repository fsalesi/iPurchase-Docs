# REMOVE_ORIGINATOR_FROM_GROUP_CO - iPurchase System Setting

**Category:** Approval Workflow

TRUE | FALSE.

### Valid Values

| Value | Behavior |
|-------|----------|
| **TRUE** | removes originator from approval routing on change orders |
| **FALSE** | Disables this feature |

### How It Works

This setting affects the approval workflow process, determining how requisitions are routed and approved.

### Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | REMOVE_ORIGINATOR_FROM_GROUP_CO |
| **Category** | Approval Workflow |
| **Owner** | Admin |
| **Default Value** | FALSE |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'REMOVE_ORIGINATOR_FROM_GROUP_CO'
```

### Related Settings

- [REMOVE_APPROVER_FROM_GROUPS](REMOVE_APPROVER_FROM_GROUPS.md)
- [REMOVE_APPROVER_ROLE_LIST](REMOVE_APPROVER_ROLE_LIST.md)