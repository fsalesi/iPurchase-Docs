# HELP_URL - iPurchase System Setting

**Category:** Uncategorized

If you've developed customized help, then enter the URL to that file here. ex. https://google.com

### How It Works

See the description above for details on how this setting affects system behavior.

### Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | HELP_URL |
| **Category** | Uncategorized |
| **Owner** | Admin |
| **Default Value** | (none) |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'HELP_URL'
```