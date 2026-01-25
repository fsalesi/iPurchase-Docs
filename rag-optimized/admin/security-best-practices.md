# Security Best Practices - iPurchase Administration

**Purpose:** Security recommendations for user access, permissions, and audit controls.

### Permission Settings

**Restrict Dangerous Permissions:**
```sql
ALLOW_DELETE_PROCESSED = "admin_only" (very few users)
ALLOW_APPROVER_CHANGES = "TRUE" (but limit sub-settings)
ALLOW_APPROVER_CHANGES_REMOVE_APPROVER = "buyers,admins"
```

### Delegation Controls

**Prevent Unauthorized Delegation:**
```sql
OOF_LIMIT_BY_DOLLARS = "TRUE" (can't delegate to lower authority)
OOF_LIMIT_BY_DEPT = "TRUE" (can't delegate outside department)
OOF_LIMIT_TO_APPROVERS = "TRUE" (can only delegate to approvers)
USE_CHAINED_DELEGATES = "FALSE" (no delegation chains)
```

### Audit Trail

**Monitor:**
- Who approved what (xxreq_audit.xxreq_actual_approver)
- Delegation activity (who is delegating to whom)
- Manual routing changes (who is adding/removing approvers)
- Deleted requisitions (especially processed ones)

**Review:**
- Unusual approval patterns
- Approvers with very high volumes
- Frequent delegation by same people
- Overuse of supervisor override
