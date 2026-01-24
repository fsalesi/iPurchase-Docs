# INQUIRY_NO_NAME_SEARCH - iPurchase System Setting

**Category:** Reporting & Inquiry

If this setting is set to true then when a user searches for a supplier they will not be allowed to search by name, only by supplier number. a value of false enables the user to search by both supplier number and name.

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
| **Setting Name** | INQUIRY_NO_NAME_SEARCH |
| **Category** | Reporting & Inquiry |
| **Owner** | Power Users |
| **Default Value** | FALSE |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'INQUIRY_NO_NAME_SEARCH'
```