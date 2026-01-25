# AUTO_ADD_DROPSHIP - iPurchase System Setting

**Category:** Purchase Orders

Controls whether drop ship address is automatically added to requisitions based on certain conditions.

### How It Works

When enabled, the system automatically populates the drop ship address field based on requisition type, user, or other criteria.

### Valid Values

| Value | Behavior |
|-------|----------|
| `TRUE` | Auto-add drop ship address |
| `FALSE` | Manual drop ship entry |

### Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | AUTO_ADD_DROPSHIP |
| **Category** | Purchase Orders |
| **Owner** | Admin |
| **Default Value** | (none) |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'AUTO_ADD_DROPSHIP'
```

### Related Settings

- [AUTO_COMMENTS_BUYER](AUTO_COMMENTS_BUYER.md)
- [AUTO_COMMENTS_CO](AUTO_COMMENTS_CO.md)
- [AUTO_COMMENTS_LINE_SITE](AUTO_COMMENTS_LINE_SITE.md)
