# RESTRICT_USER_SUB_ACCOUNTS - iPurchase System Setting

**Category:** User Management

Is the Sub Acct selection limited to those sub accounts defined in the user's profile? See RESTRICT_USER_DEPARTMENTS for more information on how to set the Sub Acct field in User Maintenance

### Valid Values

| Value | Behavior |
|-------|----------|
| **TRUE** | Enables this feature |
| **FALSE** | Disables this feature |

### How It Works

See the description above for details on how this setting affects system behavior.

### Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | RESTRICT_USER_SUB_ACCOUNTS |
| **Category** | User Management |
| **Owner** | Power Users |
| **Default Value** | FALSE |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'RESTRICT_USER_SUB_ACCOUNTS'
```