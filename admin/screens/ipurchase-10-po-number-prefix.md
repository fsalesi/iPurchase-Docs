---
screen_id: ipurchase_po_number_prefix
screen_name: PO Number Prefix
module: iPurchase
access_level: Administrator
database_tables:
  - pf_mstr
related_screens:
  - admin_system_settings
screenshot: ../screenshots/ipurchase-po-number-prefix/01-main-screen.png
last_updated: 2025-01-24
author: Frank Salesi
---

# PO Number Prefix

## Overview

The PO Number Prefix screen enhances QAD's standard PO numbering, which provides only a single sequence and prefix for all POs. This screen allows you to define multiple PO number sequences with different prefixes based on domain, site, or other criteria.

**Use case:** Different sites or entities need distinct PO number ranges (e.g., Site 10000 uses "A" prefix, Site 12000 uses "B" prefix).

## Access Path

iPurchase → PO Number Prefix

## Screenshot

![PO Number Prefix](../screenshots/ipurchase-po-number-prefix/01-main-screen.png)

**Note:** The screen displays a helpful message: "Currently using the next QAD Number. For a unique sequence for each prefix, setup PO_NBR_USE_QAD = false in system settings"

## Screen Layout

The screen consists of:
1. **Sequences** - Form for creating/editing prefix configurations
2. **PO Number Prefix Browse** - Grid listing all configured sequences

---

## Form Fields

### Field: Domain

- **Type**: Dropdown
- **Database**: `pf_attr`
- **Description**: Domain this sequence applies to. Select "All Domains" (`*`) or a specific domain.

### Field: [Dynamic Field Name] Value

- **Type**: Text
- **Database**: `pf_value`
- **Description**: The value that triggers this prefix. The field label is dynamic based on the `PO_PREFIX_FIELD` system setting (e.g., if set to `xxreq_domain`, label shows "xxreq_domain Value").

### Field: PO Prefix

- **Type**: Text
- **Database**: `pf_alt_value`
- **Description**: The prefix to prepend to PO numbers (e.g., "D", "A", "B")

---

## Browse Columns

| Column | Database Field | Description |
|--------|----------------|-------------|
| Domain | `pf_attr` | Domain or "All Domains" |
| [Dynamic] | `pf_value` | Value from PO_PREFIX_FIELD (e.g., xxreq_domain) |
| Prefix | `pf_alt_value` | PO number prefix |
| Next Nbr | `pf_seq` | Next number in sequence (read-only, auto-increments) |

---

## Action Buttons

| Button | Action |
|--------|--------|
| **Save** | Saves the prefix configuration |
| **New** | Clears form to create a new sequence |
| **Delete** | Deletes the selected sequence |
| **Copy** | Duplicates the sequence |

---

## Database Storage

PO prefix sequences are stored in `pf_mstr` with:

| Field | Value |
|-------|-------|
| `pf_us_id` | `SYSTEM` |
| `pf_group` | `POSEQ` |
| `pf_attr` | Domain (`*` = all) |
| `pf_value` | Value matching PO_PREFIX_FIELD |
| `pf_alt_value` | Prefix |
| `pf_seq` | Next number (auto-incremented) |

**Query Example:**
```sql
SELECT pf_attr AS domain, pf_value AS field_value, 
       pf_alt_value AS prefix, pf_seq AS next_nbr
FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'POSEQ'
ORDER BY pf_attr, pf_value
```

---

## Related System Settings

| Setting | Current Value | Description |
|---------|---------------|-------------|
| **PO_NBR_USE_QAD** | `false` | When `true`, uses QAD's single PO sequence. When `false`, uses iPurchase's enhanced prefix/sequence system. |
| **PO_PREFIX_FIELD** | `xxreq_domain` | The requisition field used to determine which prefix/sequence to use. This controls the dynamic field label and browse column header. |

---

## How It Works

1. Requisition is approved and ready for PO creation
2. System reads `PO_PREFIX_FIELD` setting to determine lookup key (e.g., `xxreq_domain`)
3. System looks up `pf_mstr` where `pf_group = 'POSEQ'` and matches domain + field value
4. If found, uses that prefix and increments that sequence
5. If not found, falls back to `*` (all domains) entry
6. PO number = Prefix + Next Number (e.g., "D133633")

## Examples

### Example 1: Single Prefix for All

| Domain | xxreq_domain | Prefix | Next Nbr |
|--------|--------------|--------|----------|
| All Domains | demo1 | D | 133633 |

All POs get "D" prefix: D133633, D133634, D133635...

### Example 2: Site-Specific Prefixes

If `PO_PREFIX_FIELD = xxreq_site`:

| Domain | xxreq_site | Prefix | Next Nbr |
|--------|------------|--------|----------|
| demo1 | 10000 | A | 50000 |
| demo1 | 12000 | B | 75000 |
| All Domains | * | X | 1000 |

- Site 10000 POs: A50000, A50001...
- Site 12000 POs: B75000, B75001...
- Other sites: X1000, X1001...

---

## Tips

1. **Always have a fallback** - Create an "All Domains" entry to handle cases that don't match specific rules
2. **Plan your ranges** - Ensure number ranges don't overlap between prefixes
3. **Test before go-live** - Verify the correct prefix is being applied in test environment
4. **Coordinate with QAD** - If `PO_NBR_USE_QAD = true`, this screen has no effect

---

## Related Screens

- [System Settings](./02-system-settings.md) - Configure PO_NBR_USE_QAD, PO_PREFIX_FIELD
