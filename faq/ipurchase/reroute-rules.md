# Requisition Rerouting FAQ

Understanding when and why requisitions reroute for approvals.

---

## Quick Answer

A requisition reroutes when:
1. The dollar amount changes beyond tolerance thresholds
2. The approval simulation finds different approvers than before
3. A monitored field is changed (on change orders)
4. An admin changes approval rules while requisitions are pending

---

## Original Requisitions (Not Change Orders)

### When Does an Original Req Reroute?

**Scenario 1: Amount Exceeds Tolerance**

If the requisition amount increases by more than EITHER:
- `ALLOWED_DOLLAR_INCREASE` (default: $100), OR
- `ALLOWED_PERCENT_INCREASE` (default: 10%)

...the requisition will reroute.

**Example:**
- Original req: $1,000
- Modified to: $1,200 (20% increase, $200 increase)
- With defaults ($100/10%): **Will reroute** (exceeds both thresholds)

**Tip:** To use only one threshold, set the other to a very high number:
- Use only percentage: Set `ALLOWED_DOLLAR_INCREASE = 999999999`
- Use only dollar: Set `ALLOWED_PERCENT_INCREASE = 999999999`

**Scenario 2: Approval Simulation Detects Different Approvers**

When an approver clicks "Approve", iPurchase runs a simulation to determine who should approve based on the current data. If the simulated approvers differ from the current routing (in sequence, group, or user), the system automatically reroutes.

**Exception:** If approvers were *removed* (e.g., amount decreased from $10,000 to $3), the requisition continues without rerouting—it just skips the approvers no longer needed.

**Scenario 3: Admin Changed Rules**

If an administrator modifies approval rules while requisitions are pending, Scenario 2 applies—the next approval triggers a simulation that may detect different approvers.

### What Does NOT Trigger a Reroute?

- Using the "Add Approver" function (manual additions don't trigger reroute)
- Decreasing the requisition amount
- Adding notes or attachments
- Changes that don't affect who needs to approve

### Controlling Reroute Behavior

| Setting | Description | Default |
|---------|-------------|---------|
| `ALLOWED_DOLLAR_INCREASE` | Max $ increase without reroute | 100 |
| `ALLOWED_PERCENT_INCREASE` | Max % increase without reroute | 10 |
| `ALLOW_AUTO_REROUTE` | Enable/disable simulation-based reroute | TRUE |

---

## Change Orders

Change orders have their own reroute rules, separate from original requisitions.

### When Does a Change Order Reroute?

**Scenario 1: Amount Exceeds Tolerance**

If the PO value increases by more than EITHER:
- `PO_UPDATE_TOLERANCE_AMOUNT` (default: $100), OR
- `PO_UPDATE_TOLERANCE_PCT` (default: 10%)

...the change order will reroute.

**Note:** A value equal to the threshold WILL reroute (e.g., exactly 10% triggers reroute).

**Scenario 2: Approval Simulation Detects Different Approvers**

Same as original requisitions—when an approver clicks "Approve", a simulation runs. If approvers differ, it reroutes.

Can be disabled with: `PO_UPDATE_CHECK_REROUTE = FALSE`

**Scenario 3: Monitored Field Changes**

Some customers want reroutes when specific fields change, regardless of amount. Configure these settings to monitor specific fields:

| Setting | Description | Example Values |
|---------|-------------|----------------|
| `CO_HEADER_REROUTE_FIELDS` | Header fields that trigger reroute | `xxreq_ship_to` |
| `CO_ITEM_REROUTE_FIELDS` | Line fields that trigger reroute | `xxreqd_item,xxreqd_cost,xxreqd_um,xxreqd_qty` |
| `CO_ITEM_REROUTE_NEW` | Reroute when new line added | TRUE/FALSE |

**Example Configuration:**
```
CO_HEADER_REROUTE_FIELDS = xxreq_ship_to
CO_ITEM_REROUTE_FIELDS = xxreqd_item,xxreqd_cost
CO_ITEM_REROUTE_NEW = TRUE
```

This configuration reroutes if:
- Ship-to address changes
- Item or unit cost changes on a line
- A new line is added to the change order

### What Does NOT Trigger a Change Order Reroute?

- Lower price (decrease)
- Due date changes
- Adding notes or attachments
- Fields not listed in the reroute field settings

### Change Order Tolerance Settings

| Setting | Description | Default |
|---------|-------------|---------|
| `PO_UPDATE_TOLERANCE_AMOUNT` | Max $ increase without reroute | 100 |
| `PO_UPDATE_TOLERANCE_PCT` | Max % increase without reroute | 10 |
| `PO_UPDATE_CHECK_REROUTE` | Enable simulation-based reroute | TRUE |
| `CO_HEADER_REROUTE_FIELDS` | Header fields to monitor | (empty) |
| `CO_ITEM_REROUTE_FIELDS` | Line fields to monitor | (empty) |
| `CO_ITEM_REROUTE_NEW` | Reroute on new line | FALSE |

---

## Common Questions

### Q: What's the difference between req tolerances and change order tolerances?

**Original Requisition Tolerances:**
- `ALLOWED_DOLLAR_INCREASE` / `ALLOWED_PERCENT_INCREASE`
- Apply when modifying a pending requisition that hasn't become a PO yet

**Change Order Tolerances:**
- `PO_UPDATE_TOLERANCE_AMOUNT` / `PO_UPDATE_TOLERANCE_PCT`
- Apply when modifying a requisition that's already a PO (change order)

These are completely separate settings with potentially different values.

### Q: Are these the same as QAD receiving tolerances?

**No.** iPurchase reroute tolerances are completely separate from QAD receiving tolerances. QAD tolerances control what can be received against a PO. iPurchase tolerances control when approval routing is recalculated.

### Q: Can I use percentage-only or dollar-only?

Yes. Set the threshold you don't want to use to a very high number:
- **Percentage only:** `PO_UPDATE_TOLERANCE_AMOUNT = 999999999`
- **Dollar only:** `PO_UPDATE_TOLERANCE_PCT = 999999999`

### Q: Who approves when a change order reroutes?

It depends on your approval rules. Options include:
- Full reroute through all original approvers
- Just the buyer (`$xxreq_buyer`)
- The originator (`$xxreq_userid`)
- The on-behalf-of person (`$xxreq_obo`)
- A dedicated change order approval group

Configure this in your approval rules with conditions for `xxreq_update_po = TRUE`.

### Q: How do I prevent any rerouting?

**For original requisitions:**
```
ALLOWED_DOLLAR_INCREASE = 999999999
ALLOWED_PERCENT_INCREASE = 999999999
ALLOW_AUTO_REROUTE = FALSE
```

**For change orders:**
```
PO_UPDATE_TOLERANCE_AMOUNT = 999999999
PO_UPDATE_TOLERANCE_PCT = 999999999
PO_UPDATE_CHECK_REROUTE = FALSE
```

**Warning:** This removes important controls. Most organizations want some level of rerouting for audit and compliance purposes.

---

## Flowchart: Will My Req Reroute?

```
                    ┌─────────────────────┐
                    │ Requisition Modified │
                    └──────────┬──────────┘
                               │
                    ┌──────────▼──────────┐
                    │ Is it a Change Order?│
                    └──────────┬──────────┘
                               │
              ┌────────────────┴────────────────┐
              │                                 │
        ┌─────▼─────┐                    ┌──────▼──────┐
        │    NO     │                    │     YES     │
        │ (Orig Req)│                    │(Change Order)│
        └─────┬─────┘                    └──────┬──────┘
              │                                 │
   ┌──────────▼──────────┐          ┌──────────▼──────────┐
   │ Amount increase >   │          │ Amount increase >   │
   │ ALLOWED_DOLLAR or   │          │ PO_UPDATE_TOLERANCE │
   │ ALLOWED_PERCENT?    │          │ _AMOUNT or _PCT?    │
   └──────────┬──────────┘          └──────────┬──────────┘
              │                                 │
       YES ───┼─── NO                    YES ───┼─── NO
              │     │                          │     │
              │     ▼                          │     ▼
              │  ┌──────────────┐              │  ┌──────────────┐
              │  │ Simulation   │              │  │ Reroute field│
              │  │ finds diff   │              │  │ changed?     │
              │  │ approvers?   │              │  └──────┬───────┘
              │  └──────┬───────┘              │         │
              │         │                      │   YES ──┼── NO
              │  YES ───┼─── NO                │         │    │
              │         │     │                │         │    ▼
              ▼         ▼     ▼                ▼         ▼  ┌─────────┐
         ┌────────┐ ┌────────┐ ┌──────┐  ┌────────┐ ┌────────┐│Continue │
         │REROUTE │ │REROUTE │ │CONT. │  │REROUTE │ │REROUTE ││No Route │
         └────────┘ └────────┘ └──────┘  └────────┘ └────────┘└─────────┘
```

---

## See Also

- [Approval Strategy Guide](../../reference/approval-strategy-guide.md) - Change order rules section
- [System Settings Reference](../../reference/system-settings-reference.md) - All tolerance settings
- [Change Orders FAQ](change-orders.md) - More change order questions
- [Approvals FAQ](approvals.md) - Approval workflow questions

---

*Last Updated: January 2026*
