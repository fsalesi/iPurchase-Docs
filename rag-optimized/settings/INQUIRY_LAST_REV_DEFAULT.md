# INQUIRY_LAST_REV_DEFAULT - iPurchase System Setting

**Category:** Reporting & Inquiry

Setting this to true will check the Last Revision Only in the requisition inquiry.

### Valid Values

| Value | Behavior |
|-------|----------|
| **TRUE** | Enables this feature |
| **FALSE** | Disables this feature |

### How It Works

This setting provides a default value that pre-populates fields, reducing data entry and ensuring consistency.

### Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | INQUIRY_LAST_REV_DEFAULT |
| **Category** | Reporting & Inquiry |
| **Owner** | Admin |
| **Default Value** | TRUE |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'INQUIRY_LAST_REV_DEFAULT'
```

### Related Settings

- [INQUIRY_AFTER_REJECT](INQUIRY_AFTER_REJECT.md)
- [INQUIRY_NOTES_MATCHES](INQUIRY_NOTES_MATCHES.md)
- [INQUIRY_NO_NAME_SEARCH](INQUIRY_NO_NAME_SEARCH.md)
