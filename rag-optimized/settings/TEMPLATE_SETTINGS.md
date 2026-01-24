# Template Settings Reference - iPurchase System Settings

This document covers **dynamic/template settings** - settings where the name includes placeholders like `[Requisition Type]`, `[Site]`, or `[Supplier]`. These are not single settings but patterns that create multiple settings based on your configuration.

## Requisition Type Settings (RT_*)

These settings are created for each requisition type defined in REQUISITION_TYPES. Replace `[Type]` with your actual type name (e.g., EXPENSE, CAPITAL, INVENTORY).

### Account Control
| Pattern | Purpose |
|---------|---------|
| `RT_[Type]_ACCOUNT_DEFAULT` | Default GL account for this type |
| `RT_[Type]_ACCOUNT_RANGE` | Valid accounts (Can-Do list) |
| `RT_[Type]_ACCOUNT_READONLY` | Lock account field (TRUE/FALSE) |
| `RT_[Type]_[Site]_ACCOUNT_DEFAULT` | Site-specific account default |
| `RT_[Type]_[Site]_ACCOUNT_RANGE` | Site-specific account range |
| `RT_[Type]_[Site]_ACCOUNT_READONLY` | Site-specific readonly |

### Department Control
| Pattern | Purpose |
|---------|---------|
| `RT_[Type]_DEPT_DEFAULT` | Default department for this type |
| `RT_[Type]_DEPT_RANGE` | Valid departments (Can-Do list) |
| `RT_[Type]_DEPT_READONLY` | Lock department field |
| `RT_[Type]_[Site]_DEPT_DEFAULT` | Site-specific department default |
| `RT_[Type]_[Site]_DEPT_RANGE` | Site-specific department range |
| `RT_[Type]_[Site]_DEPT_READONLY` | Site-specific readonly |

### Sub-Account Control
| Pattern | Purpose |
|---------|---------|
| `RT_[Type]_SUB_ACCOUNT_DEFAULT` | Default sub-account |
| `RT_[Type]_SUB_ACCOUNT_RANGE` | Valid sub-accounts (Can-Do list) |
| `RT_[Type]_SUB_ACCOUNT_READONLY` | Lock sub-account field |
| `RT_[Type]_[Site]_SUB_ACCOUNT_*` | Site-specific overrides |

### Other Type Settings
| Pattern | Purpose |
|---------|---------|
| `RT_[Type]_ACCESS` | Who can use this req type (Can-Do list) |
| `RT_[Type]_DEFAULT_BUYER` | Default buyer for this type |
| `RT_[Type]_GL_OVERRIDE` | Allow GL override for this type |
| `RT_[Type]_INVENTORY_ITEM_ONLY` | Require inventory items only |
| `RT_[Type]_REQUIRE_PROJECT` | Require project code |
| `RT_[Type]_[Site]_DEFAULT_BUYER` | Site-specific buyer |
| `RT_[Type]_[Site]_GL_OVERRIDE` | Site-specific GL override |

### Example
For an "EXPENSE" requisition type at site "10000":
```
RT_EXPENSE_ACCOUNT_DEFAULT = 8100
RT_EXPENSE_ACCOUNT_RANGE = 8*,rent
RT_EXPENSE_10000_ACCOUNT_DEFAULT = 8200  (overrides for site 10000)
RT_EXPENSE_DEFAULT_BUYER = mike
```

## PO Signature Settings

| Pattern | Purpose |
|---------|---------|
| `PO_SIGNATURE_[SITE]` | Signature image for site |
| `PO_SIGNATURE_BUYER_[buyercode]` | Buyer-specific signature |
| `PO_SIGNATURE_BUYER_[domain]` | Domain-specific buyer signature |
| `PO_SIGNATURE_BUYER_[domain]_[site]` | Domain+site buyer signature |

## Catalog/Punchout Settings

| Pattern | Purpose |
|---------|---------|
| `CATALOG_ACCESS_[Supplier NBR]` | Restrict catalog access by supplier |
| `PUNCHOUT_REQ_TYPE_[supplier]` | Force req type for punchout supplier |
| `CODE_LIST_H_SHIPVIA_XREF_[VENDOR]` | Vendor-specific ship via mapping |

## Other Template Settings

| Pattern | Purpose |
|---------|---------|
| `DEFAULT_BUYER_[SITE]` | Site-specific default buyer |
| `PO_LOGO_[po_bill]` | Bill-to specific PO logo |
| `ESTIMATED_TAX_PERCENT_[ship_to]` | Ship-to specific tax rate |
| `AUDIT_TRAIL_[XXX]` | Table-specific audit settings |

## How to Query

```sql
-- Find all RT_EXPENSE settings
SELECT pf_attr, pf_chr1 
FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT'
  AND pf_attr LIKE 'RT_EXPENSE%'
ORDER BY pf_attr

-- Find all site-specific settings for site 10000
SELECT pf_attr, pf_chr1
FROM PUB.pf_mstr  
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT'
  AND pf_attr LIKE '%_10000_%'
ORDER BY pf_attr
```
