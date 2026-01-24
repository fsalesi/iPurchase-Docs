# DATE_FORMAT - iPurchase System Setting

**Category:** System Configuration

Controls the global display format for date fields throughout iPurchase.

### Valid Values

| Value | Format | Example |
|-------|--------|---------|
| **mdy** | Month/Day/Year | 01/15/2024 (DEFAULT) |
| **dmy** | Day/Month/Year | 15/01/2024 |
| **ymd** | Year/Month/Day | 2024/01/15 |

### How It Works

This setting globally changes how date fields are displayed and entered across the entire iPurchase application:
- Requisition entry screens (need-by date, entry date)
- Approval screens
- Reports and inquiries
- Purchase order documents

The format affects both display and data entry expectations. Users should enter dates in the configured format to avoid confusion.

**Important:** This is a system-wide setting. All users will see dates in the same format regardless of their locale preferences.

### Common Questions

- How do I change the date format in iPurchase?
- Why are dates showing in the wrong format?
- Can individual users have different date formats?
- What date format should I use for international users?

### Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | DATE_FORMAT |
| **Category** | System Configuration |
| **Owner** | Admin |
| **Default Value** | mdy |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'DATE_FORMAT'
```
