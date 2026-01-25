# Change Order Configuration - iPurchase Administration

**Purpose:** Configuring change order tolerance, re-approval requirements, and change order workflows.

### Tolerance Settings

**Balance efficiency vs control:**
- **Low tolerance** (e.g., $100, 5%) → More re-approvals, tighter control
- **High tolerance** (e.g., $1000, 15%) → Fewer re-approvals, more efficiency

**Recommended Starting Point:**
```sql
PO_UPDATE_TOLERANCE_AMOUNT = "500"
PO_UPDATE_TOLERANCE_PCT = "10"
```

**Review Quarterly:**
- Are too many change orders re-routing? (Tolerance too low)
- Are large changes bypassing approval? (Tolerance too high)
- Adjust based on business risk comfort level

### Material Change Fields

**Header Fields that Trigger Re-Route:**
```sql
CO_HEADER_REROUTE_FIELDS = "xxreq_buyer,xxreq_ship_to,xxreq_vendor"
```

**Line Fields that Trigger Re-Route:**
```sql
CO_ITEM_REROUTE_FIELDS = "xxreqd_cc,xxreqd_acct,xxreqd_sub,xxreqd_part"
```

**New Line Items:**
```sql
CO_ITEM_REROUTE_NEW = "TRUE"  (new lines always re-route)
CO_ITEM_REROUTE_NEW = "FALSE" (new lines OK if within tolerance)
```

**Guidelines:**
- Include fields that represent scope/responsibility changes
- Start conservative (more fields = more re-routes = tighter control)
- Relax based on business feedback
