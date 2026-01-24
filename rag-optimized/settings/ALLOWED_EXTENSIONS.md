# ALLOWED_EXTENSIONS - iPurchase System Setting

**Category:** Uncategorized

This is a comma separated list of allowed or not-allowed file extensions which can be uploaded to iPurchase. This works using the Progress "can-do" function. See Progress Help if needed A default value of !exe,!dll,!js*,!com,!bat,!lnk,!ws*,!scr,!msi,* is set.  This excludes all file types lists

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
| **Setting Name** | ALLOWED_EXTENSIONS |
| **Category** | Uncategorized |
| **Owner** | Admin |
| **Default Value** | !exe,!dll,!js*,!com,!bat,!lnk,!ws*,!scr,!msi,* |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'ALLOWED_EXTENSIONS'
```
