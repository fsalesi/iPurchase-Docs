# System Settings FAQ

Common questions about configuring iPurchase system settings.

---

## Domain-Specific Settings

### Can I have different settings for different domains?

Yes! Any setting can be configured for:
- **All Domains** - Select "All Domains" in the Domain field
- **Specific Domain** - Select a specific domain code

**How iPurchase resolves settings:**
1. First looks for a setting specific to the current domain
2. If not found, uses the "All Domains" setting
3. If neither exists, uses the system default

### Examples

**Example 1: Different default buyers per domain**

| Domain | Setting | Value |
|--------|---------|-------|
| All Domains | `RT_EXPENSE_DEFAULT_BUYER` | john.smith |
| USCO | `RT_EXPENSE_DEFAULT_BUYER` | mary.jones |
| EURO | `RT_EXPENSE_DEFAULT_BUYER` | hans.mueller |

Result:
- USCO domain → mary.jones
- EURO domain → hans.mueller
- Any other domain → john.smith

**Example 2: Different approval tolerances per domain**

| Domain | Setting | Value |
|--------|---------|-------|
| All Domains | `ALLOWED_DOLLAR_INCREASE` | 100 |
| CORP | `ALLOWED_DOLLAR_INCREASE` | 500 |

Result:
- CORP domain → $500 tolerance
- All other domains → $100 tolerance

**Example 3: Different ship-to lists per domain**

| Domain | Setting | Value |
|--------|---------|-------|
| All Domains | `CODE_LIST_H_SHIPTO` | (blank - uses QAD si_mstr) |
| MFGCO | `CODE_LIST_H_SHIPTO` | LIST:WH1:Warehouse 1,WH2:Warehouse 2 |

Result:
- MFGCO domain → Only two hardcoded ship-to options
- All other domains → Full list from QAD

### When should I use domain-specific settings?

- Different business units have different processes
- Regional requirements (tax rates, currencies, ship-to addresses)
- Subsidiaries with different approval hierarchies
- Testing new settings in one domain before rolling out

---

## Drop-Down List Settings (CODE_LIST)

### How do CODE_LIST settings work?

CODE_LIST settings control what appears in drop-down menus. You have two options:

#### Option 1: Hardcoded List

Use `LIST:` prefix with comma-separated values:

**Code only:**
```
LIST:EA,BX,PK
```

**Code and description:**
```
LIST:EA:Each,BX:Box,PK:Pack
```

**Example - Rejection codes:**
```
CODE_LIST_REJECTION_CODES = LIST:001:Invalid Prices,002:Invalid Accounts,003:No Budget
```

#### Option 2: QAD Generalized Code

Point to a QAD generalized code field name (from `code_mstr`):

```
CODE_LIST_H_SHIPVIA = po_shipvia
CODE_LIST_H_FOB = po_fob
CODE_LIST_UM = pt_um
```

This pulls values from QAD's Generalized Codes Maintenance.

#### Option 3: Blank (Some Settings Only)

Some CODE_LIST settings can be left blank to pull from QAD master data:

| Setting | If Blank, Uses |
|---------|----------------|
| `CODE_LIST_H_SHIPTO` | si_mstr (Ship-To Master) |
| `CODE_LIST_H_BILLTO` | si_mstr (Ship-To Master) |
| `CODE_LIST_H_SITE` | si_mstr (Site Master) |
| `CODE_LIST_H_CURRENCY` | cu_mstr (Currency Master) |
| `CODE_LIST_UM` | um_mstr (Unit of Measure Master) |

### Common CODE_LIST Settings

| Setting | Description | Options |
|---------|-------------|---------|
| `CODE_LIST_H_SHIPTO` | Ship-to addresses | Blank (si_mstr), generalized code, or LIST |
| `CODE_LIST_H_BILLTO` | Bill-to addresses | Blank (si_mstr), generalized code, or LIST |
| `CODE_LIST_H_SITE` | Sites | Blank (si_mstr), generalized code, or LIST |
| `CODE_LIST_H_SHIPVIA` | Ship via codes | Generalized code (e.g., `po_shipvia`) or LIST |
| `CODE_LIST_H_FOB` | Freight terms | Generalized code (e.g., `po_fob`) or LIST |
| `CODE_LIST_H_CURRENCY` | Currencies | Blank (cu_mstr), generalized code, or LIST |
| `CODE_LIST_UM` | Units of measure | Blank (um_mstr), generalized code (e.g., `pt_um`), or LIST |
| `CODE_LIST_REJECTION_CODES` | Rejection reasons | LIST format recommended |
| `CODE_LIST_H_BLANKET_CYCLE` | Blanket PO cycles | LIST (e.g., `LIST:MO:Monthly,WK:Weekly`) |

### User-Defined Field Drop-Downs

For custom user fields on requisition headers:

```
CODE_LIST_H_XXREQ_UCHAR1 = LIST:Yes:Yes,No:No
CODE_LIST_H_XXREQ_UCHAR2 = LIST:1:Option A,2:Option B,3:Option C
CODE_LIST_H_XXREQ_UCHAR3 = LIST:Apples:Apples,Bananas:Bananas,Oranges:Oranges
```

### Vendor-Specific Ship Via (Punchout)

For punchout suppliers that need different ship via codes than iPurchase/QAD:

```
# Default cross-reference for all vendors
CODE_LIST_H_SHIPVIA_XREF = LIST:UPS:UPS Ground,FEDX:FedEx 3 Day

# Specific vendor override (replace ACME123 with vendor number)
CODE_LIST_H_SHIPVIA_XREF_ACME123 = LIST:UPS:UPS Next Day,FEDX:FedEx Express
```

---

## Requisition Type Settings (RT_)

### How do RT_ settings work?

RT_ (Requisition Type) settings allow different configuration per requisition type.

**Pattern:** `RT_[TYPE]_[SETTING]`

**Examples:**
```
RT_EXPENSE_ACCOUNT_DEFAULT = 8100
RT_CAPITAL_ACCOUNT_DEFAULT = 6100
RT_INVENTORY_DEFAULT_BUYER = purchasing_dept
```

### Can RT_ settings be site-specific?

Yes! Add the site code after the type:

**Pattern:** `RT_[TYPE][SITE]_[SETTING]`

**Examples:**
```
RT_EXPENSE_ACCOUNT_DEFAULT = 8100           # Default for all sites
RT_EXPENSE_10000_ACCOUNT_DEFAULT = 8200     # Site 10000 override
RT_EXPENSE_10000_DEFAULT_BUYER = site10_buyer
```

**Resolution order:**
1. `RT_[TYPE][SITE]_[SETTING]` (type + site specific)
2. `RT_[TYPE]_[SETTING]` (type specific)
3. System default

---

## See Also

- [System Settings Reference](../reference/system-settings-reference.md) - Complete settings catalog
- [Requisition Entry FAQ](requisition-entry.md) - More on defaults and required fields

---

*Last Updated: January 2026*
