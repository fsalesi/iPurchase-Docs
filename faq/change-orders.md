# Change Orders FAQ

Common questions about change orders (PO modifications).

---

## Basics

### What is a change order?

A change order is a requisition that modifies an existing Purchase Order. It's identified by `xxreq_update_po = TRUE`.

**Common Change Order Scenarios:**
- Adding lines to an existing PO
- Increasing quantities or prices
- Extending delivery dates
- Modifying terms or ship-to address
- Canceling lines

### Who can create change orders?

Controlled by `PO_UPDATE_GROUPS` setting.

**Default:** Only the buyers group can create change orders.

**Common Configuration:**
```
PO_UPDATE_GROUPS = buyers
```

Some organizations also allow the original requestor to create change orders.

### Which requisition types allow change orders?

Controlled by `PO_UPDATE_REQ_TYPES` setting.

Leave blank to allow change orders on all requisition types, or list specific types that are NOT allowed.

---

## Rerouting

### When does a change order reroute?

See [Requisition Rerouting FAQ](reroute-rules.md) for complete details.

**Quick Summary - Change orders reroute when:**

1. **Amount exceeds tolerance:**
   - `PO_UPDATE_TOLERANCE_AMOUNT` (default: $100)
   - `PO_UPDATE_TOLERANCE_PCT` (default: 10%)

2. **Approval simulation finds different approvers:**
   - Can disable with `PO_UPDATE_CHECK_REROUTE = FALSE`

3. **Monitored field changes:**
   - `CO_HEADER_REROUTE_FIELDS` - Header fields to monitor
   - `CO_ITEM_REROUTE_FIELDS` - Line fields to monitor
   - `CO_ITEM_REROUTE_NEW` - Reroute when new line added

### What does NOT trigger a change order reroute?

- Lower price (decrease)
- Due date changes
- Adding notes or attachments
- Fields not in the monitored field settings

### Who approves change orders?

Depends on your approval rules. Create rules with condition `xxreq_update_po = TRUE`.

**Common Options:**
- Buyer only (`$xxreq_buyer`)
- Original submitter (`$xxreq_userid`)
- On-behalf-of person (`$xxreq_obo`)
- Full re-approval through original approvers
- Dedicated change order approval group

---

## Tolerance Settings

### What are the change order tolerance settings?

| Setting | Description | Default |
|---------|-------------|---------|
| `PO_UPDATE_TOLERANCE_AMOUNT` | Max $ increase without reroute | 100 |
| `PO_UPDATE_TOLERANCE_PCT` | Max % increase without reroute | 10 |

**Note:** If EITHER threshold is exceeded, the change order reroutes.

### How do I use only percentage (ignore dollar)?

Set `PO_UPDATE_TOLERANCE_AMOUNT = 999999999`

### How do I use only dollar (ignore percentage)?

Set `PO_UPDATE_TOLERANCE_PCT = 999999999`

### Are these the same as QAD receiving tolerances?

**No.** iPurchase change order tolerances are completely separate from QAD receiving tolerances.

- **iPurchase tolerances:** Control when approval routing is recalculated
- **QAD tolerances:** Control what can be received against a PO

---

## Field Monitoring

### Can I force reroute when specific fields change?

Yes. Use the CO_REROUTE settings:

| Setting | Description | Example |
|---------|-------------|---------|
| `CO_HEADER_REROUTE_FIELDS` | Header fields that trigger reroute | `xxreq_ship_to` |
| `CO_ITEM_REROUTE_FIELDS` | Line fields that trigger reroute | `xxreqd_item,xxreqd_cost,xxreqd_um` |
| `CO_ITEM_REROUTE_NEW` | Reroute when new line added | TRUE |

**Example:** Force reroute if Ship-To or item changes:
```
CO_HEADER_REROUTE_FIELDS = xxreq_ship_to
CO_ITEM_REROUTE_FIELDS = xxreqd_item
CO_ITEM_REROUTE_NEW = TRUE
```

---

## Order Date

### Does the PO order date update on change orders?

Controlled by `CO_UPDATE_ORDER_DATE` setting.

| Value | Behavior |
|-------|----------|
| TRUE | Order date updates to today's date |
| FALSE | Order date keeps the original date |

---

## Originator Approval

### Can the originator approve their own change order?

Controlled by `REMOVE_ORIG_CO` setting.

| Value | Behavior |
|-------|----------|
| TRUE | Originator is removed from change order routing |
| FALSE | Originator can be in the routing (may approve own CO) |

---

## Common Configurations

### Minimal change order approval (Buyer only)

```
PO_UPDATE_GROUPS = buyers
PO_UPDATE_TOLERANCE_AMOUNT = 999999999
PO_UPDATE_TOLERANCE_PCT = 999999999
PO_UPDATE_CHECK_REROUTE = FALSE
```
Buyer can make any changes without re-approval routing.

### Strict change order control

```
PO_UPDATE_GROUPS = buyers
PO_UPDATE_TOLERANCE_AMOUNT = 100
PO_UPDATE_TOLERANCE_PCT = 10
PO_UPDATE_CHECK_REROUTE = TRUE
CO_ITEM_REROUTE_NEW = TRUE
CO_HEADER_REROUTE_FIELDS = xxreq_ship_to
CO_ITEM_REROUTE_FIELDS = xxreqd_item,xxreqd_cost
```
Changes exceeding $100/10%, new lines, or field changes trigger full re-approval.

---

## See Also

- [Requisition Rerouting](reroute-rules.md) - Complete reroute logic
- [Approval Strategy Guide](../reference/approval-strategy-guide.md) - Change order rules
- [System Settings Reference](../reference/system-settings-reference.md) - All CO_ settings

---

*Last Updated: January 2026*
