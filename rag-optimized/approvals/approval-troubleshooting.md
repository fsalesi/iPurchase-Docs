# Approval Troubleshooting - iPurchase

**Purpose:** Common approval issues and how to diagnose them using database queries.

### Rule Not Triggering

**Check:**
1. Is rule active? (`xxapp_active` or `xxAR_Active`)
2. Does amount fall within min/max range?
3. Do ALL conditions match (AND logic for simple rules)?
4. For complex rules, trace through tree evaluation
5. Was rule blocked by earlier stop condition?
6. Is it a notification rule being checked during approval? (Won't trigger)

### Wrong Approver

**Check:**
1. Variable substitution - is field populated correctly?
2. Group membership - is user actually in the group?
3. Delegation - is approver delegating to someone else?
4. MULTIPLE_APPROVALS setting - is correct instance being kept?

### Routing Takes Too Long

**Optimization:**
1. Reduce number of rules (consolidate where possible)
2. Use stop conditions appropriately
3. Order rules by frequency (most common first)
4. Avoid complex rules where simple rules suffice
5. Check for inefficient line-level evaluation

### Duplicate Approvals

**Check:**
1. MULTIPLE_APPROVALS setting - should be keep_last usually
2. Are multiple rules adding same approver?
3. Is AUTO_APPROVE_FORWARD enabled but not working?
4. Check group membership (user appearing both directly and via group)
