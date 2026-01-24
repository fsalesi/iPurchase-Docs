# REMOVE_ORIGINATOR_FROM_GROUP - iPurchase System Setting

**Category:** Uncategorized

If the originator is listed as a member of a group on the approval routing, if this person should be removed from the group set this setting to TRUE.

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
| **Setting Name** | REMOVE_ORIGINATOR_FROM_GROUP |
| **Category** | Uncategorized |
| **Owner** | Admin |
| **Default Value** | TRUE |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'REMOVE_ORIGINATOR_FROM_GROUP'
```