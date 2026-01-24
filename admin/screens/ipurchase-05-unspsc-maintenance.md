---
screen_id: ipurchase_unspsc_maintenance
screen_name: UNSPSC Maintenance
module: iPurchase
access_level: Administrator
database_tables:
  - u_code
related_screens:
  - ipurchase_unspsc_accounts
screenshot: ../screenshots/ipurchase-unspsc-maintenance/01-main-screen.png
last_updated: 2025-01-24
author: Frank Salesi
---

# UNSPSC Maintenance

## Overview

The UNSPSC Maintenance screen manages the United Nations Standard Products and Services Code (UNSPSC) lookup table. UNSPSC is a hierarchical commodity classification system used to categorize products and services.

UNSPSC codes are 8-digit numbers with a hierarchical structure:
- **Segment** (first 2 digits) - Broad category (e.g., 10 = Live Plant and Animal Material)
- **Family** (digits 3-4) - Sub-category
- **Class** (digits 5-6) - Product group
- **Commodity** (digits 7-8) - Specific item type

## Use Cases

- **Approval routing** - Route requisitions based on commodity type (e.g., IT equipment over $10K requires IT Director approval)
- **Spend analysis** - Categorize spending by commodity for reporting
- **Supplier catalogs** - Punchout items often include UNSPSC codes
- **Account defaulting** - Auto-assign GL accounts based on commodity (see [UNSPSC Accounts](./ipurchase-06-unspsc-accounts.md))

## Access Path

iPurchase → UNSPSC Maintenance

## Screenshot

![UNSPSC Maintenance Main Screen](../screenshots/ipurchase-unspsc-maintenance/01-main-screen.png)

## Screen Layout

The screen consists of:
1. **UNSPSC Info** - Form for viewing/editing codes
2. **UNSPSC Maintenance Browse** - Grid listing all codes

---

## UNSPSC Info Form

### Field: Language

- **Type**: Dropdown
- **Database**: `u_lang`
- **Description**: Language for the description (typically "English")
- **Note**: Supports multi-language descriptions for the same UNSPSC code

### Field: UNSPSC Code

- **Type**: Text
- **Required**: Yes
- **Database**: `ucode_id`
- **Description**: The 8-digit UNSPSC code
- **Example**: `10000000` (Segment level), `10101502` (Commodity level - Dogs)

### Field: Description

- **Type**: Text
- **Required**: Yes
- **Database**: `ucode_desc`
- **Description**: Human-readable description of the code
- **Example**: "Live Plant and Animal Material and Accessories and Supplies"

---

## Action Buttons

| Button | Action |
|--------|--------|
| **Save** | Saves the UNSPSC code |
| **New** | Clears form to create a new code |
| **Delete** | Deletes the selected code |
| **Copy** | Duplicates the code (useful for creating variations) |

---

## UNSPSC Maintenance Browse

### Browse Columns

| Column | Description |
|--------|-------------|
| Language | Language code (e.g., English) |
| UNSPSC | The 8-digit UNSPSC code |
| Description | Human-readable description |

---

## Database Table

**Table: `u_code`**

| Field | Type | Description |
|-------|------|-------------|
| `u_lang` | character | Language code |
| `ucode_id` | character | UNSPSC code (primary key with language) |
| `ucode_desc` | character | Description |

**Query Example:**
```sql
SELECT u_lang, ucode_id, ucode_desc
FROM PUB.u_code
WHERE ucode_id LIKE '43%'  -- IT/Computer equipment
ORDER BY ucode_id
```

---

## UNSPSC Code Structure

| Level | Digits | Example | Description |
|-------|--------|---------|-------------|
| Segment | 1-2 | `10000000` | Live Plant and Animal Material |
| Family | 3-4 | `10100000` | Live animals |
| Class | 5-6 | `10101500` | Livestock |
| Commodity | 7-8 | `10101502` | Dogs |

### Common Segments

| Segment | Description |
|---------|-------------|
| 10 | Live Plant and Animal Material |
| 14 | Paper Materials and Products |
| 23 | Industrial Manufacturing Equipment |
| 26 | Power Generation and Distribution |
| 27 | Tools and General Machinery |
| 31 | Manufacturing Components |
| 39 | Laboratory Equipment |
| 43 | Information Technology Equipment |
| 44 | Office Equipment and Supplies |
| 72 | Building and Construction Services |
| 80 | Management and Business Services |
| 86 | Education and Training Services |

---

## Tips

1. **Pre-loaded data** - iPurchase typically comes with a full UNSPSC code set pre-loaded
2. **Use in approval rules** - Filter rules by UNSPSC using Can-Do patterns (e.g., `43*` for all IT equipment)
3. **Punchout integration** - Suppliers often return UNSPSC codes with catalog items
4. **Account mapping** - Use [UNSPSC Accounts](./ipurchase-06-unspsc-accounts.md) to auto-default GL accounts

---

## Related Screens

- [UNSPSC Accounts](./ipurchase-06-unspsc-accounts.md) - Map UNSPSC codes to GL accounts
- [Approval Rules (Complex)](./ipurchase-01-approval-rules.md) - Filter by UNSPSC
- [Approval Rules - Simple](./ipurchase-02-approval-rules-simple.md) - UNSPSC filter field
