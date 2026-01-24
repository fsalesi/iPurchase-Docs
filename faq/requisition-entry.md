# Requisition Entry FAQ

Common questions about creating requisitions.

---

## Requisition Types

### What requisition types are available?

Controlled by `REQUISITION_TYPES` setting.

**Common Types:**
- Expense - General purchases
- Capital - Capital expenditures
- Inventory - Stock/inventory items
- Service - Service contracts

**Format:** `List:Default:Type1,Type2,Type3`

**Example:** `List:Expense:Expense,Capital,Inventory,Service`

### Can I restrict who creates certain requisition types?

Yes. Use `RT_[TYPE]_ACCESS` settings.

**Example:**
```
RT_INVENTORY_ACCESS = buyers,inventory_users
RT_CAPITAL_ACCESS = capital_approvers
```

### Do all requisition types require a PO?

No. Set `RT_[TYPE]_PO_REQUIRED` for types that don't need POs.

**Example:** Credit card requisitions - approved but no PO created, Finance/AP notified instead.

### Can inventory requisitions only have inventory items?

Yes. Set `RT_INVENTORY_ITEM_ONLY = Inventory` to restrict.

---

## Defaults and Required Fields

### How do I set default values?

Use `DEFAULT_[FIELD]` settings:

| Setting | Description |
|---------|-------------|
| `DEFAULT_REQTYPE` | Default requisition type |
| `DEFAULT_SHIPTO` | Default ship-to address |
| `DEFAULT_SITE` | Default site |
| `DEFAULT_BILLTO` | Default bill-to address |
| `DEFAULT_SHIPVIA` | Default ship via code |
| `DEFAULT_FREIGHTTERMS` | Default freight terms |
| `DEFAULT_LEADTIME` | Default lead time (days) |

### How do I set defaults by requisition type?

Use `RT_[TYPE]_[FIELD]_DEFAULT` pattern:

```
RT_EXPENSE_ACCOUNT_DEFAULT = 8100
RT_CAPITAL_ACCOUNT_DEFAULT = 6100
RT_EXPENSE_DEFAULT_BUYER = john.smith
```

### How do I set defaults by site?

Add site code to setting name:

```
RT_EXPENSE_10000_DEFAULT_BUYER = mike
RT_EXPENSE_10000_ACCOUNT_DEFAULT = 8200
```

Site-specific settings override type-level defaults.

### Which requisition types require project codes?

Set `RT_REQUIRE_PROJECT` with list of types:

```
RT_REQUIRE_PROJECT = Capital
```

---

## Account/GL Configuration

### How do I restrict valid accounts by requisition type?

Use `RT_[TYPE]_ACCOUNT_RANGE` with Can-Do list:

```
RT_EXPENSE_ACCOUNT_RANGE = 8*,rent
RT_CAPITAL_ACCOUNT_RANGE = 6100,6200
```

### Can I lock accounts so users can't change them?

Yes. Set `RT_[TYPE]_ACCOUNT_READONLY = TRUE`

```
RT_CAPITAL_ACCOUNT_DEFAULT = 6100
RT_CAPITAL_ACCOUNT_READONLY = TRUE
```

### Are accounts restricted by site?

Can be. Use site-specific settings:

```
RT_EXPENSE_ACCOUNT_RANGE = 8*
RT_EXPENSE_11000_ACCOUNT_RANGE = 8200,8300
```

Site 11000 has more restrictive account range.

---

## Drop-Down Lists

### How do I control what appears in drop-down lists?

CODE_LIST settings control drop-down values. They support **three formats**:

#### Format 1: Blank (Use QAD Data)

Leave the setting blank to pull values from QAD tables automatically.

```
CODE_LIST_H_SHIPTO = 
```
This uses the `si_mstr` table from QAD for ship-to addresses.

#### Format 2: QAD Generalized Code Pointer

Point to a QAD generalized code field name (`code_fldname` in `code_mstr`):

```
CODE_LIST_H_SHIPVIA = po_shipvia
CODE_LIST_UM = pt_um
CODE_LIST_H_FOB = po_fob
```
This uses QAD's generalized codes maintenance for the values.

#### Format 3: Explicit LIST (Hardcoded Values)

Use `LIST:` prefix with comma-separated values:

**Simple format (code only):**
```
LIST:EA,BX,PK
```

**Code and description format:**
```
LIST:EA:Each,BX:Box,PK:Pack
```

**Example with rejection codes:**
```
CODE_LIST_REJECTION_CODES = LIST:001:Invalid Prices,002:Invalid Accounts,003:No Budget,004:Need Project Code
```

### Common CODE_LIST Settings

| Setting | Description | Default/Notes |
|---------|-------------|---------------|
| `CODE_LIST_H_SHIPTO` | Ship-to addresses | Blank = use si_mstr from QAD |
| `CODE_LIST_H_BILLTO` | Bill-to addresses | Blank = use si_mstr from QAD |
| `CODE_LIST_H_SITE` | Sites | Blank = use si_mstr from QAD |
| `CODE_LIST_H_SHIPVIA` | Ship via codes | Often `po_shipvia` |
| `CODE_LIST_H_FOB` | Freight terms (FOB) | Often `po_fob` |
| `CODE_LIST_H_CURRENCY` | Currencies | Blank = use cu_mstr from QAD |
| `CODE_LIST_UM` | Units of measure | Often `pt_um`, or blank = use um_mstr |
| `CODE_LIST_REJECTION_CODES` | Rejection reasons | LIST format recommended |
| `CODE_LIST_H_BLANKET_CYCLE` | Blanket PO cycle codes | e.g., `LIST:MO:Monthly,WK:Weekly,DA:Daily` |

### User-Defined Fields

For custom user fields on requisitions:

| Setting | Description |
|---------|-------------|
| `CODE_LIST_H_XXREQ_UCHAR1` | User Field 1 dropdown |
| `CODE_LIST_H_XXREQ_UCHAR2` | User Field 2 dropdown |
| `CODE_LIST_H_XXREQ_UCHAR3` | User Field 3 dropdown |
| `CODE_LIST_H_XXREQ_UCHAR4` | User Field 4 dropdown |
| `CODE_LIST_H_XXREQ_UCHAR5` | User Field 5 dropdown |

**Example:**
```
CODE_LIST_H_XXREQ_UCHAR1 = LIST:Yes:Yes,No:No
CODE_LIST_H_XXREQ_UCHAR3 = LIST:Apples:Apples,Bananas:Bananas,Oranges:Oranges
```

### Vendor-Specific Ship Via Cross-Reference

For punchout suppliers that need different ship via codes:

```
CODE_LIST_H_SHIPVIA_XREF = LIST:UPS:UPS Ground,FEDX:FedEx 3 Day
CODE_LIST_H_SHIPVIA_XREF_[VENDOR] = LIST:UPS:UPS Ground,FEDX:FedEx Express
```

Replace `[VENDOR]` with actual vendor number for vendor-specific mappings.


## Need Date / Lead Time

### How is the Need Date calculated?

`DEFAULT_LEADTIME` days are added to today's date.

**Setting:** `DEFAULT_LEADTIME = 0` means Need Date is mandatory entry (no default).

For punchout orders: `PUNCHOUT_LEADTIME`

For inventory: MRP drives the date from item master.

---

## Deliver To

### Can Deliver To be free-form text?

Controlled by `DELIVER_TO_FILL_IN` setting:

| Value | Behavior |
|-------|----------|
| TRUE | Free-form text entry |
| FALSE | Must select from user list |

---

## Tax

### How is tax handled?

iPurchase estimates tax for approval routing purposes. QAD calculates actual tax for the PO.

**Settings:**

| Setting | Description |
|---------|-------------|
| `ESTIMATED_TAX_PERCENT` | Default estimated tax rate |
| `ESTIMATED_TAX_PERCENT_[shipto]` | Rate by ship-to address |
| `ESTIMATED_TAX_PERCENT_[dept/acct]` | Rate by dept/account |

**Example:** `ESTIMATED_TAX_PERCENT = 10` adds 10% to taxable lines for routing.

---

## Requisition Numbers

### What format do requisition numbers use?

`REQUISITION_PREFIX` + sequential number (8 digits)

**Examples:**
- Production: `REQUISITION_PREFIX = R` → R00000001
- Test: `REQUISITION_PREFIX = TR` → TR00000001

Prefix can be changed at any time.

---

## Drop Ships

### Does iPurchase support drop ships?

Yes. Set `ALLOW_DROP_SHIP = TRUE`

**Setting:** `AUTO_ADD_DROPSHIP` controls automatic drop ship for specific domains.

---

## Rejection Codes

### How do I configure rejection codes?

Set `CODE_LIST_REJECTION_CODES` with comma-separated descriptions:

```
CODE_LIST_REJECTION_CODES = Invalid price,No budget,Invalid account,Over budget,Need project code,Need contract,Other
```

Approvers select from this list when rejecting.

---

## Memo Requisitions

### What is a memo-only requisition type?

A req type where lines are memo/notes only - no items, quantities, or costs.

**Setting:** `RT_MEMO_ONLY_LIST = Expense,Capital,Service`

---

## See Also

- [System Settings Reference](../reference/system-settings-reference.md) - All RT_ settings
- [Approvals FAQ](approvals.md) - Approval routing
- [User Management FAQ](user-management.md) - Department restrictions

---

*Last Updated: January 2026*
