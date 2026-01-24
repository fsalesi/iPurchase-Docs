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

## Screen Layout

The screen consists of:
1. **PO Number Prefix** - Form for creating/editing prefix configurations
2. **PO Number Prefix Browse** - Grid listing all configured sequences

---

## Form Fields

### Field: Domain

- **Type**: Text
- **Database**: `pf_attr`
- **Description**: Domain this sequence applies to. Use `*` for all domains.

### Field: Entity/Site

- **Type**: Text
- **Database**: `pf_value`
- **Description**: The site or entity value that triggers this prefix. What field this matches depends on the `PO_PREFIX_FIELD` system setting.

### Field: Prefix

- **Type**: Text
- **Database**: `pf_alt_value`
- **Description**: The prefix to prepend to PO numbers (e.g., "D", "A", "B")

### Field: Next Nbr

- **Type**: Integer
- **Database**: `pf_seq`
- **Description**: The next number in the sequence. Increments automatically when POs are created.

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
| `pf_value` | Entity/Site value |
| `pf_alt_value` | Prefix |
| `pf_seq` | Next number |

**Query Example:**
```sql
SELECT pf_attr AS domain, pf_value AS entity_site, 
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
| **PO_PREFIX** | `List:10000:bb` | Legacy setting - list format mapping values to prefixes |
| **PO_PREFIX_FIELD** | `xxreq_domain` | The requisition field used to determine which prefix/sequence to use (e.g., `xxreq_domain`, `xxreq_site`) |

---

## How It Works

1. Requisition is approved and ready for PO creation
2. System reads `PO_PREFIX_FIELD` setting to determine lookup key (e.g., domain)
3. System looks up `pf_mstr` where `pf_group = 'POSEQ'` and `pf_attr` matches domain
4. If found, uses that prefix and increments that sequence
5. If not found, falls back to `*` (all domains) entry
6. PO number = Prefix + Next Number (e.g., "D133633")

## Examples

### Example 1: Single Prefix for All

| Domain | Entity/Site | Prefix | Next Nbr |
|--------|-------------|--------|----------|
| * | demo1 | D | 133633 |

All POs get "D" prefix: D133633, D133634, D133635...

### Example 2: Site-Specific Prefixes

| Domain | Entity/Site | Prefix | Next Nbr |
|--------|-------------|--------|----------|
| demo1 | 10000 | A | 50000 |
| demo1 | 12000 | B | 75000 |
| demo1 | * | X | 1000 |

- Site 10000 POs: A50000, A50001...
- Site 12000 POs: B75000, B75001...
- Other sites: X1000, X1001...

### Example 3: Domain-Specific Prefixes

| Domain | Entity/Site | Prefix | Next Nbr |
|--------|-------------|--------|----------|
| demo1 | * | D1 | 100000 |
| demo2 | * | D2 | 200000 |

- Domain demo1 POs: D1100000, D1100001...
- Domain demo2 POs: D2200000, D2200001...

---

## Tips

1. **Always have a fallback** - Create a `*` entry to handle cases that don't match specific rules
2. **Plan your ranges** - Ensure number ranges don't overlap between prefixes
3. **Test before go-live** - Verify the correct prefix is being applied in test environment
4. **Coordinate with QAD** - If `PO_NBR_USE_QAD = true`, this screen has no effect

---

## Related Screens

- [System Settings](./02-system-settings.md) - Configure PO_NBR_USE_QAD, PO_PREFIX_FIELD
