# DEFAULT_REQTYPE - iPurchase System Setting

**Category:** System Configuration

In this setting the administrator can set the default value for "Requisition Type" field.

### How It Works

See the description above for details on how this setting affects system behavior.

### Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | DEFAULT_REQTYPE |
| **Category** | System Configuration |
| **Owner** | Power Users |
| **Default Value** | (none) |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'DEFAULT_REQTYPE'
```