# Default Approval Rules - iPurchase Safety Nets

**Purpose:** Built-in rules that ensure compliance and catch configuration gaps.

iPurchase includes default rules that serve as safety nets to ensure no requisition bypasses proper approval.

### Buyer as Final Approver (Sequence ~900)

```
Description: "Buyer must approve"
Approver: $xxreq_buyer
Conditions: Requisition has a buyer assigned
```

**Why Buyer is Last:**
- Buyers work directly with suppliers and know vendor capabilities
- They verify pricing, lead times, and terms before PO creation
- Final quality check before requisition becomes a purchase order
- Catches issues that higher-level approvers might miss

### On Behalf Of (OBO) Rule

```
Description: "OBO must approve when different from creator"
Approver: $xxreq_obo
Conditions: xxreq_userid <> xxreq_obo
```

**Scenario:** Admin assistant (Jane) creates requisitions for manager (Bob). Bob is the "On Behalf Of" because it's his budget.

**Why This Matters:**
- Budget owner should always approve their own spending
- Prevents charging to another person's cost center without knowledge
- Creates accountability—Bob can't claim he didn't know
- Only triggers when creator ≠ OBO (no duplicate when same person)

### Originator Cannot Self-Approve (Sequence ~990)

```
Description: "Originator cannot be only approver"
Type: Validation Rule
Conditions: All approvers = originator
```

**Purpose:** Prevents someone from creating AND being the only approver of their own requisition. Ensures segregation of duties.

### Must Have At Least One Approver (Sequence ~999)

```
Description: "Requisition must have at least one approver"
Type: Validation Rule
Conditions: Approval routing is empty
```

**Purpose:** Catches requisitions that fell through the cracks—no rules matched. Prevents configuration gaps from allowing unapproved purchases.

### Change Order Rule

```
Description: "Change Order Approval"
Approver: change_order_approvers (or $xxreq_buyer)
Conditions: xxreq_update_po = TRUE
```

**Change Order Scenarios:**
- Adding lines to an existing PO
- Increasing quantities or prices
- Extending delivery dates
- Modifying terms

**Related Settings:**
- `CO_TOLERANCE_PCT` - Percentage change allowed without re-approval
- `CO_TOLERANCE_AMT` - Dollar amount change allowed without re-approval

### Common Questions

- Why does the buyer always appear in the approval chain?
- How do I prevent self-approval of requisitions?
- What happens if no approval rules match a requisition?
- How does On Behalf Of (OBO) approval work?
- When do change orders require re-approval?
