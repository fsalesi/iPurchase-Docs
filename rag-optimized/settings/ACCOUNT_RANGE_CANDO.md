# ACCOUNT_RANGE_CANDO - iPurchase System Setting

**Category:** GL Accounts & Finance

This is a comma separated list of accounts that can be used with iPurchase. The field uses the Progress �Can-Do� function. See Progress help if needed. A sample value can be 5521,!5622,56*,7*,!* This is interpreted as account 5521 is valid, account 5622 is not valid, any accounts that begin with 56 (except 5622) are valid, any accounts that begin with a 7 are valid, and finally, all other accounts are invalid. These can be further restricted by Requisition Type with other settings.

### How It Works

This setting uses [Can-Do list format](../../reference/can-do-list-format.md) for specifying users and groups.

### Valid Values

| Value | Behavior |
|-------|----------|
| `*` (asterisk) | Everyone/all users |
| Blank/empty | No one/disabled |
| User/Group list | Only specified users/groups |

### Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | ACCOUNT_RANGE_CANDO |
| **Category** | GL Accounts & Finance |
| **Owner** | Finance |
| **Default Value** | * |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'ACCOUNT_RANGE_CANDO'
```
