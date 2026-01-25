# Approval Rule Evaluation Algorithm - iPurchase Technical Reference

**Purpose:** How iPurchase evaluates approval rules in sequence order and builds the approval routing list.

### Phase 1: Complex Rules (xxAppRule)

1. Query xxAppRule rules WHERE (xxAR_Domain = '*' OR xxAR_Domain = [req_domain]) in ascending `xxAR_AppLevel` order
2. For each rule where conditions match:
   - Add approver(s) to approval chain
   - If `xxAR_Eval_Lines = true`, may create multiple approval records (one per matching line)
3. If rule has `xxAR_stop = true`:
   - Record stop sequence number
   - Skip remaining xxAppRule rules with higher sequence numbers
   - Proceed to Phase 2
4. If no stop encountered, set stop sequence to infinity

### Phase 2: Simple Rules (xxapp_mstr)

1. Query xxapp_mstr rules WHERE (xxapp_domain = '*' OR xxapp_domain = [req_domain]) AND xxapp_seq <= stop_sequence_from_phase1
2. Process in ascending `xxapp_seq` order
3. For each rule where conditions match:
   - Add approver(s) to approval chain
4. If rule has `xxapp_stop = true`:
   - Record new stop sequence
   - **Delete any xxAppRule approvers from temp table where `xxAR_AppLevel > xxapp_seq`**
   - Stop evaluation

### Phase 3: Notification Rules (After PO Creation)

1. After requisition is fully approved and converted to PO
2. Process ONLY rules where `xxAR_notify = true` OR `xxapp_notify = true`
3. These rules are completely ignored during approval evaluation (Phases 1 & 2)
4. Matching approvers are added as CC recipients on PO email notification
5. Use case: "Finance wants to see all POs over $50K but doesn't need to approve"

### Important Notes

- Both rule systems share the same sequence number space
- Complex rules are evaluated first, then simple rules (up to stop sequence)
- A stop in either system affects both systems
- Notification rules (`notify = true`) are completely separate - only evaluated after PO creation

### Example Execution

**Scenario: Change Order Rule Triggers**
```
xxAppRule:
  Seq 5: Change Order (stop=true) → Triggers, adds buyer
  Seq 450: CFO Rule → Skipped (beyond stop sequence)

xxapp_mstr:
  Seq 100: Cost Center Owner → Skipped (beyond stop sequence of 5)
  Seq 200: Manager → Skipped
  
Result: Only buyer approves (Change Order rule)
```

**Scenario: Change Order Doesn't Trigger**
```
xxAppRule:
  Seq 5: Change Order → Doesn't match
  Seq 450: CFO Rule (stop=false) → Matches, adds CFO
  No stop encountered, stop_seq = infinity

xxapp_mstr:
  Seq 100: Cost Center Owner → Matches, adds owner
  Seq 200: Manager (over $5K) → Matches, adds manager
  Seq 300: VP (over $50K) → Doesn't match (req is $10K)
  
Result: CFO (seq 450) + Cost Center Owner (seq 100) + Manager (seq 200)
```

**Scenario: Stop in xxapp_mstr**
```
xxAppRule:
  Seq 5: OBO Rule → Matches, adds OBO
  Seq 450: CFO Rule (stop=false) → Matches, adds CFO

xxapp_mstr:
  Seq 100: Cost Center Owner (stop=true) → Matches, adds owner, STOPS
  Seq 200: Manager → Skipped
  
System deletes CFO from temp approval table (seq 450 > 100)
Result: OBO (seq 5) + Cost Center Owner (seq 100)
```
