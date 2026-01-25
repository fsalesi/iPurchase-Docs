# Delegation Configuration - iPurchase Administration

**Purpose:** Setting up delegation rules, out-of-office, and chained delegation options.

### Out of Office Settings

**Enable Delegation:**
```sql
ALLOW_OOF = "*" (everyone can delegate)
```

**Restrict Who Can Be Delegates:**
```sql
OOF_LIMIT_TO = "*" (anyone can be delegate)
OOF_LIMIT_TO = "approvers" (only approvers group)
OOF_LIMIT_TO = "" (no one can delegate - feature disabled)
```

**Require Same Department:**
```sql
OOF_LIMIT_BY_DEPT = "TRUE"
```

**Require Equal/Higher Approval Limit:**
```sql
OOF_LIMIT_BY_DOLLARS = "TRUE" (recommended for security)
```

**Delegation Chains:**
```sql
USE_CHAINED_DELEGATES = "FALSE" (recommended - prevents Jane→Bob→Sue chains)
USE_CHAINED_DELEGATES = "TRUE" (allow transitive delegation)
```

**Notification:**
```sql
OOF_NOTIFY_OLD = "TRUE" (email existing pending reqs to delegate immediately)
OOF_ASK_FREQUENCY = numeric value (prompt to remove delegate on login)
```

### Supervisor Override

**Allow Supervisors to Approve for Subordinates:**
```sql
ALLOW_SUPERVISORS_TO_APPROVE = "*" (all supervisors can override)
ALLOW_SUPERVISORS_TO_APPROVE = "managers,directors" (only specific groups)
ALLOW_SUPERVISORS_TO_APPROVE = "" (no supervisor overrides)
```

**Use Case:** Employee is out/stuck, supervisor approves on their behalf

**Security Note:** Audit trail shows both who was required to approve (employee) and who actually approved (supervisor)
