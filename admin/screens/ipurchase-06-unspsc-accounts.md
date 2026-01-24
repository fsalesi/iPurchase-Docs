---
screen_id: ipurchase_unspsc_accounts
screen_name: UNSPSC Accounts
module: iPurchase
access_level: Administrator
database_tables:
  - pf_mstr
related_screens:
  - ipurchase_unspsc_maintenance
screenshot: ../screenshots/ipurchase-unspsc-accounts/01-main-screen.png
last_updated: 2025-01-24
author: Frank Salesi
---

# UNSPSC Accounts

## Overview

The UNSPSC Accounts screen maps UNSPSC commodity codes to GL accounts. When a requisition line item has a UNSPSC code, the system can automatically default the GL account based on this mapping.

This enables commodity-based accounting - for example:
- IT equipment (43*) → Account 8200 (Computer Equipment)
- Office supplies (44*) → Account 8100 (Office Supplies)
- Professional services (80*) → Account 8500 (Professional Fees)

## How It Works

1. User adds item to requisition (manually or via punchout)
2. Item has UNSPSC code (e.g., `14111507` - Writing instruments)
3. System looks up UNSPSC Accounts mapping
4. If mapping exists, GL Account is auto-populated (e.g., `8200`)
5. User can override if needed

## Access Path

iPurchase → UNSPSC Accounts

## Screenshot

![UNSPSC Accounts Main Screen](../screenshots/ipurchase-unspsc-accounts/01-main-screen.png)

## Screen Layout

The screen consists of:
1. **UNSPSC Info** - Form for creating/editing mappings
2. **UNSPSC Accounts Browse** - Grid listing all mappings

---

## UNSPSC Info Form

### Field: UNSPSC Code

- **Type**: Text
- **Required**: Yes
- **Database**: `pf_attr`
- **Description**: The UNSPSC code to map. Can be full 8-digit code or a prefix for broader matching.
- **Examples**: 
  - `14111507` - Specific commodity (Writing instruments)
  - `43000000` - Entire segment (all IT equipment)

### Field: GL Account:Sub Account

- **Type**: Text
- **Database**: `pf_chr2`
- **Description**: The GL account (and optionally sub-account) to default when this UNSPSC code is used
- **Format**: `account` or `account:subaccount`
- **Example**: `8200` or `8200:100`

---

## Action Buttons

| Button | Action |
|--------|--------|
| **Save** | Saves the UNSPSC-to-account mapping |
| **New** | Clears form to create a new mapping |
| **Delete** | Deletes the selected mapping |
| **Copy** | Duplicates the mapping |

---

## UNSPSC Accounts Browse

### Browse Columns

| Column | Description |
|--------|-------------|
| UNSPSC | The UNSPSC code |
| GL Account | The mapped GL account (and sub-account if specified) |

---

## Database Storage

UNSPSC Account mappings are stored in `pf_mstr` using a specific pattern:

| Field | Value |
|-------|-------|
| `pf_us_id` | `MRO*` |
| `pf_group` | `UNSPSC` |
| `pf_attr` | UNSPSC code |
| `pf_chr2` | GL Account:Sub Account |

**Query Example:**
```sql
SELECT pf_attr AS unspsc_code, pf_chr2 AS gl_account
FROM PUB.pf_mstr
WHERE pf_us_id = 'MRO*' 
  AND pf_group = 'UNSPSC'
ORDER BY pf_attr
```

---

## Matching Logic

When looking up a GL account for a UNSPSC code, the system uses hierarchical matching:

1. **Exact match** - Look for the full 8-digit code
2. **Class match** - Look for 6-digit prefix (digits 1-6 + 00)
3. **Family match** - Look for 4-digit prefix (digits 1-4 + 0000)
4. **Segment match** - Look for 2-digit prefix (digits 1-2 + 000000)

**Example:** Item has UNSPSC `43211503` (Notebook computers)
1. Check for `43211503` → Not found
2. Check for `43211500` → Not found
3. Check for `43210000` → Not found
4. Check for `43000000` → Found! Use account `8200`

This allows you to set broad defaults at the segment level and override with specific mappings as needed.

---

## Examples

### Example 1: IT Equipment Segment

Map all IT equipment to Computer Equipment account:

| UNSPSC | GL Account |
|--------|------------|
| 43000000 | 8200 |

Any item with UNSPSC starting with `43` will default to account 8200.

### Example 2: Specific Overrides

Set a broad default, then override specific commodities:

| UNSPSC | GL Account |
|--------|------------|
| 44000000 | 8100 | ← Default for all office equipment/supplies
| 44111500 | 8150 | ← Override: Printer supplies go to different account
| 44121600 | 8160 | ← Override: Desk accessories

### Example 3: With Sub-Accounts

Include sub-account in the mapping:

| UNSPSC | GL Account |
|--------|------------|
| 43000000 | 8200:100 |
| 80000000 | 8500:200 |

---

## Tips

1. **Start broad** - Set segment-level defaults first, then add specific overrides as needed
2. **Leave blank for no default** - If you don't want auto-defaulting for a code, don't create a mapping
3. **Review punchout items** - Check what UNSPSC codes your suppliers are returning
4. **Coordinate with approval rules** - If you're routing by UNSPSC, ensure account mappings align

---

## Related Screens

- [UNSPSC Maintenance](./ipurchase-05-unspsc-maintenance.md) - Manage UNSPSC code descriptions
- [Approval Rules (Complex)](./ipurchase-01-approval-rules.md) - Route by UNSPSC
- [Approval Rules - Simple](./ipurchase-02-approval-rules-simple.md) - UNSPSC filter field

---

## Related System Settings

See [System Settings Reference](../../reference/system-settings-reference.md) for UNSPSC-related settings.
