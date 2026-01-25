# AUTO_COMMENTS_OTHER - iPurchase System Setting

**Category:** Purchase Orders

Specifies fields whose values are automatically added to PO line comments.

### How It Works

When a PO is created, the system automatically adds comments containing the values of fields listed here. Useful for passing requisition information to suppliers.

### Valid Values

| Value | Example |
|-------|---------|
| Comma-separated field names | `xxreqd_project,xxreqd_cc` |
| Blank | No auto-comments |

### Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | AUTO_COMMENTS_OTHER |
| **Category** | Purchase Orders |
| **Owner** | Admin |
| **Default Value** | (none) |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'AUTO_COMMENTS_OTHER'
```

### Related Settings

- [AUTO_COMMENTS_BUYER](AUTO_COMMENTS_BUYER.md)
- [AUTO_COMMENTS_CO](AUTO_COMMENTS_CO.md)
- [AUTO_COMMENTS_LINE_SITE](AUTO_COMMENTS_LINE_SITE.md)
