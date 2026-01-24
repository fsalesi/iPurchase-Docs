# ALLOW_MANUAL_EMAIL_PO - iPurchase System Setting

**Category:** Email Configuration

Controls which users see the "Email PO" button to manually email purchase orders to suppliers.

### How It Works

Users in this list can manually trigger PO emails to suppliers, even if automatic emailing is disabled or has already occurred.

### Valid Values

This setting uses [Can-Do list format](../../reference/can-do-list-format.md).

| Value | Behavior |
|-------|----------|
| User/Group list | Specified users/groups see Email PO button |
| `*` (asterisk) | Everyone can email POs |
| Blank/empty | No one can manually email POs (DEFAULT) |

### Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | ALLOW_MANUAL_EMAIL_PO |
| **Category** | Email Configuration |
| **Owner** | Admin |
| **Default Value** | (none) |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'ALLOW_MANUAL_EMAIL_PO'
```

### Related Settings

- [EMAIL_SUPPLIER_PO](EMAIL_SUPPLIER_PO.md) - Auto-email POs to suppliers
- [EMAILSERVER](EMAILSERVER.md) - SMTP server configuration
