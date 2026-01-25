# xxreq_mstr - Requisition Header Table - Fields

The main requisition table containing header-level information: status, dates, totals, vendor, buyer, and workflow state. Every requisition has one record here. Primary key is domain + requisition number.

**Common questions this answers:**
- What fields are in the xxreq_mstr table?
- What is xxreq_obo (on behalf of)?
- What is xxreq_status?
- What's the difference between xxreq_cost and xxreq_cost_gl?

**Related tables:** xxreqd_det (line items), xxreq_audit (approvals), xxreq_attach (attachments)

### Key Fields

| Field | Type | Flags | Description |
|-------|------|:-----:|-------------|
| `xxreq_nbr` | char | i | Requisition number (primary key with domain) |
| `xxreq_domain` | char | i | Domain/company code |
| `xxreq_status` | char | i | Status: blank=draft, CONFIRMED=submitted, APPROVED=approved |
| `xxreq_type` | char | i | Requisition type (Expense, Capital, Inventory, etc.) |
| `xxreq_userid` | char | i | Creator user ID (person at keyboard) |
| `xxreq_obo` | char |  | On Behalf Of - budget owner, drives approval routing |
| `xxreq_buyer` | char | i | Assigned buyer |
| `xxreq_vendor` | char | i | Vendor code |
| `xxreq_date` | date | i | Need-by date |
| `xxreq_entry_date` | date |  | Creation date |
| `xxreq_submit_date` | date |  | Submission date |
| `xxreq_app_date` | date |  | Approval date |
| `xxreq_app_time` | inte |  | Approval time (seconds after midnight) |
| `xxreq_cost` | deci-2 | i | Total in requisition currency |
| `xxreq_cost_gl` | deci-5 |  | Total in base currency (use for approval thresholds) |
| `xxreq_submit_total` | deci-2 |  | Total at time of submission |
| `xxreq_currency` | char |  | Requisition currency code |
| `xxreq_update_po` | logi |  | TRUE = this is a change order to existing PO |
| `xxreq_copied_from` | char | i | Source requisition (for copies/change orders) |
| `xxreq_mat_change` | logi |  | TRUE = material change requiring re-approval |
| `xxreq_po_nbr` | char | i | Generated PO number |
| `xxreq_site` | char |  | Site code |
| `xxreq_ship_to` | char |  | Ship-to location |
| `xxreq_bill_to` | char |  | Bill-to location |
| `xxreq_project` | char |  | Project code |
| `xxreq_int_notes` | char | i | Internal notes (searchable) |
| `xxreq_ext_notes` | char | i | External notes for vendor |

### Custom/Extension Fields

The table includes placeholder fields for customer-specific data:
- `xxreq_sort_field1` through `xxreq_sort_field10` (char, indexed)
- `xxreq_char1` through `xxreq_char10` (char)
- `xxreq_date1` through `xxreq_date5` (date)
- `xxreq_dec1` through `xxreq_dec5` (decimal)
- `xxreq_log1` through `xxreq_log5` (logical)
- `xxreq_uchar1` through `xxreq_uchar5` (char, user-defined)
- `xxreq_ulog1` through `xxreq_ulog5` (logical, user-defined)

### Blanket Order Fields

| Field | Type | Description |
|-------|------|-------------|
| `xxreq_blanket` | logi | TRUE = blanket order |
| `xxreq_blanket_nbr` | char | Blanket order number |
| `xxreq_blanket_start` | date | Blanket start date |
| `xxreq_blanket_end` | date | Blanket end date |
| `xxreq_blanket_est` | deci-2 | Estimated blanket total |
