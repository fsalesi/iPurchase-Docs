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

Use `CODE_LIST_[FIELD]` settings:

| Setting | Values |
|---------|--------|
| `CODE_LIST_H_SHIPTO` | Ship-to addresses |
| `CODE_LIST_H_BILLTO` | Bill-to addresses |
| `CODE_LIST_H_SITE` | Sites |
| `CODE_LIST_H_SHIPVIA` | Ship via codes |
| `CODE_LIST_H_FOB` | Freight terms |
| `CODE_LIST_UM` | Units of measure |

Leave blank to use all valid values from QAD.

---

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
