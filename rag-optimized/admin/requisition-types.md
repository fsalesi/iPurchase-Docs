# Requisition Types Configuration - iPurchase Administration

**Purpose:** Setting up different requisition types (Expense, Capital, Inventory) with type-specific settings.

### Standard Types

**Default Types Provided:**
- Expense - Operating expenses
- Capital - Capital expenditures
- Inventory - Stock/inventory items

**Customization:**
- Add types: Service, MRO, Consulting, Travel, etc.
- Rename types: "CapEx" instead of "Capital"
- Delete unused types
- Update REQUISITION_TYPES setting

### Account Restrictions

**Prevent GL Coding Errors:**

**Lock Capital to Asset Accounts:**
```sql
RT_CAPEX_ACCOUNT_RANGE = "1000-1999"
RT_CAPEX_ACCOUNT_DEFAULT = "1500"
RT_CAPEX_ACCOUNT_READONLY = "TRUE"
```

**Allow Expense Account Range:**
```sql
RT_EXPENSE_ACCOUNT_RANGE = "6000-7999,8*"
RT_EXPENSE_ACCOUNT_DEFAULT = "" (no default, user chooses)
RT_EXPENSE_ACCOUNT_READONLY = "FALSE"
```

**Site-Specific Override:**
```sql
RT_EXPENSE_ACCOUNT_RANGE = "8*" (global setting)
RT_EXPENSE_11000_ACCOUNT_RANGE = "8200,8300" (site 11000 more restrictive)
```

### Default Buyers by Type

Assign default buyers based on requisition type:
```sql
RT_EXPENSE_DEFAULT_BUYER = "frank"
RT_CAPITAL_DEFAULT_BUYER = "mary"
RT_INVENTORY_DEFAULT_BUYER = "john"
```

Site overrides:
```sql
RT_EXPENSE_10000_DEFAULT_BUYER = "mike" (site 10000 uses different buyer)
```
