# Default Approval Rules - iPurchase Safety Nets

**Purpose:** Built-in rules that ensure compliance and catch configuration gaps.

iPurchase includes three default rules that serve as safety nets:

### 1. Buyer Approval (Sequence ~900)

```
Description: "Buyer must approve"
Approver: $xxreq_buyer
Conditions: Requisition has a buyer assigned
```

**Purpose:** Ensures the assigned buyer reviews and approves before PO creation.

### 2. Originator Cannot Self-Approve (Sequence ~990)

```
Description: "Originator cannot be only approver"
Type: Validation Rule
Conditions: All approvers = originator
```

**Purpose:** Prevents someone from creating and approving their own requisition without oversight.

### 3. Must Have At Least One Approver (Sequence ~999)

```
Description: "Requisition must have at least one approver"
Type: Validation Rule
Conditions: Approval routing is empty
```

**Purpose:** Catches requisitions that fell through the cracks—no rules matched.

**Why These Exist:**
- **Safety Net:** Catches configuration gaps
- **Compliance:** Ensures segregation of duties
- **Audit Requirements:** No requisition should bypass all approvals

---

### Buyer as Final Approver

The Buyer approval rule (typically at sequence ~900) ensures the assigned buyer is the **final approver** before the PO is created.

```
Description: "Buyer Final Approval"
Approver: $xxreq_buyer
Sequence: 900
```

**Why Buyer is Last:**
- Buyers work directly with suppliers and know vendor capabilities
- They can verify pricing, lead times, and terms before PO creation
- Final quality check on the requisition before it becomes a purchase order
- Catches any issues that approvers higher in the chain might miss

### On Behalf Of (OBO) Rule

When someone creates a requisition on behalf of another person, the OBO rule ensures the actual budget owner is aware and approves.

```
Description: "OBO must approve when different from creator"
Approver: $xxreq_obo
Conditions: xxreq_userid <> xxreq_obo
```

**Scenario:** An admin assistant (Jane) creates requisitions for their manager (Bob). Even though Jane enters the requisition, Bob is listed as the "On Behalf Of" person because it's his budget.

**Why This Matters:**
- The budget owner (OBO) should always approve their own spending
- Prevents someone from charging to another person's cost center without their knowledge
- Creates accountability—Bob can't claim he didn't know about the purchase
- The rule only triggers when creator ≠ OBO (no duplicate approval when they're the same person)

### Change Order Rule

When a requisition modifies an existing PO (change order), additional approval may be required.

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

**Why Separate Rules:**
- Change orders may need different approvers than original requisitions
- Some organizations require the original approvers to re-approve
- Others have a dedicated change order approval group
- Prevents unauthorized modifications to committed purchases

**Related Settings:**
- `CO_TOLERANCE_PCT` - Percentage change allowed without re-approval
- `CO_TOLERANCE_AMT` - Dollar amount change allowed without re-approval
- `CO_REQUIRE_REAPPROVAL` - Force full re-approval on any change

---

*Last Updated: January 2026*

*Last Updated: January 2026*
