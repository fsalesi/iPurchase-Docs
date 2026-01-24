# MESSAGE_WARNING_TIMEOUT - iPurchase System Setting

**Category:** Uncategorized

This setting allows the administrator the ability to set the duration of how long the warning message will stay on the screen. A value of 0 will indicate to keep the message on the screen indefinitely until the user clicks the "x" in the top right of the message.

### How It Works

See the description above for details on how this setting affects system behavior.

### Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | MESSAGE_WARNING_TIMEOUT |
| **Category** | Uncategorized |
| **Owner** | Power Users |
| **Default Value** | 5 |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'MESSAGE_WARNING_TIMEOUT'
```