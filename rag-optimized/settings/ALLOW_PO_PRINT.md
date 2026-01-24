# ALLOW_PO_PRINT - iPurchase System Setting

**Category:** User Management

Controls which users can print or view purchase order documents. This is typically used to restrict PO visibility to purchasing staff and management.

### How It Works

When a user attempts to print or view a PO document, the system checks if they are in this list. Users not in the list cannot access PO print functionality.

### Valid Values

This setting uses [Can-Do list format](../../reference/can-do-list-format.md).

| Value | Behavior |
|-------|----------|
| `*` (asterisk) | Everyone can print POs (DEFAULT) |
| Blank/empty | No one can print POs |
| User/Group list | Only specified users or groups can print |

### Common Questions

- What is ALLOW_PO_PRINT?
- Who can print purchase orders?
- How do I restrict PO printing to buyers only?
- Can I allow specific groups to print POs?

### Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | ALLOW_PO_PRINT |
| **Category** | User Management |
| **Owner** | Power Users |
| **Default Value** | * |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'ALLOW_PO_PRINT'
```

### Related Settings

- [PO_PRINT_PDF_FORMAT](PO_PRINT_PDF_FORMAT.md) - PDF format for printed POs
- [EMAIL_SUPPLIER_PO](EMAIL_SUPPLIER_PO.md) - Auto-email POs to suppliers
