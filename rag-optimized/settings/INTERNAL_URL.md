# INTERNAL_URL - iPurchase System Setting

**Category:** Email Configuration

Internal network URL for application. Used when APPLICATION_URL/BASE_URL are external-facing.

### How It Works

See the description above for valid values and usage.

### Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | INTERNAL_URL |
| **Category** | Email Configuration |
| **Owner** | Admin |
| **Default Value** | (none) |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'INTERNAL_URL'
```
