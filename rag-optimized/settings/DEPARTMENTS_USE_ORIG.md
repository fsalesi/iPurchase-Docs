# DEPARTMENTS_USE_ORIG - iPurchase System Setting

**Category:** GL Accounts & Finance

This setting allows the administrator to set the drop down list of departments at the line entry. If set to TRUE the list will be based on the originator.  If set to FALSE, the department is set based on the on behalf of field. User departments are defined in user maintenance. This setting is related to Restrict User Department.

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
| **Setting Name** | DEPARTMENTS_USE_ORIG |
| **Category** | GL Accounts & Finance |
| **Owner** | Admin |
| **Default Value** | FALSE |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'DEPARTMENTS_USE_ORIG'
```