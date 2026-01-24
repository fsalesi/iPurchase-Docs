# User Management FAQ

Common questions about users, passwords, permissions, and access control.

---

## Passwords

### How do I configure password policies?

**Key Settings:**

| Setting | Description | Example |
|---------|-------------|---------|
| `PASSWORD_EXPIRE_DAYS` | Days until password must be changed | 90 |
| `PASSWORD_REMINDER_DAYS` | Days before expiration to remind user | 14 |
| `PASSWORD_RULES` | Password complexity requirements | See below |

**Note:** Password settings don't apply when using SSO (Single Sign-On).

### What is the PASSWORD_RULES format?

`PASSWORD_RULES` is a comma-separated list of 7 values:

```
PASSWORD_RULES = 1,0,0,1,1,8,5
```

| Position | Description | Example Value |
|----------|-------------|---------------|
| 1 | Require a number | 1 = yes, 0 = no |
| 2 | Require non-alphanumeric character | 1 = yes, 0 = no |
| 3 | Require number OR non-alphanumeric | 1 = yes, 0 = no |
| 4 | Require capital letter | 1 = yes, 0 = no |
| 5 | Require lowercase letter | 1 = yes, 0 = no |
| 6 | Minimum password length | e.g., 8 |
| 7 | Cannot reuse last X passwords | e.g., 5 (0 = all) |

**Example:** `1,0,0,1,1,8,5` means:
- Must contain a number
- Must contain a capital letter
- Must contain a lowercase letter
- Minimum 8 characters
- Cannot reuse last 5 passwords

---

## Department/Cost Center Restrictions

### Can users be restricted to certain cost centers?

Yes. Controlled by `RESTRICT_USER_DEPARTMENTS` setting.

| Value | Behavior |
|-------|----------|
| TRUE | Users can only charge to departments listed in their profile |
| FALSE | Users can charge to any valid department |

The user's allowed departments are set in their User Profile "Dept" field.

### Can users only see requisitions in their department?

Controlled by several settings:

| Setting | Description |
|---------|-------------|
| `VIEW_REQS_RESTRICTED_MODE` | TRUE = Users can only see reqs in their workflow |
| `VIEW_REQS_DEPARTMENT` | Departments user can view reqs for (* = all) |

**Common Configuration:**
- Requisitioners: Can see their own department's reqs
- Buyers/Approvers: Can see all reqs (`*`) or specific departments they oversee
- Executives: See all (`*`)

---

## Requisition Type Access

### Can users be restricted to certain requisition types?

Yes. Use `RT_[TYPE]_ACCESS` settings.

**Example:**
```
RT_INVENTORY_ACCESS = buyers,inventory_users
RT_EXPENSE_ACCESS = *
RT_CAPITAL_ACCESS = capital_approvers,executives
```

If not set, everyone can access that requisition type.

---

## PO Access

### Who can view and print POs?

Controlled by:

| Setting | Description |
|---------|-------------|
| `ALLOW_PO_PRINT` | Groups that can print POs |
| `RT_[TYPE]_ACCESS` | Access by requisition type |

The PO print icon only appears for users in the allowed groups.

---

## Deleting Requisitions

### Who can delete requisitions?

Controlled by several settings based on requisition state:

| Setting | Description | Common Value |
|---------|-------------|--------------|
| `ALLOW_DELETE_NOT_SUBMITTED` | Delete draft reqs | admin |
| `ALLOW_DELETE_APPROVED` | Delete approved reqs | (blank = no one) |
| `ALLOW_DELETE_PROCESSED` | Delete reqs with PO | (blank = no one) |

**Notes:**
- Buyers can cancel lines (which closes the PO line)
- iPurchase deletes reqs; client is responsible for deleting QAD PO data
- System purges unsubmitted reqs after 90 days (originator notified 10 days prior)

---

## User Groups

### What groups should I create?

**Recommended Groups:**

| Group | Purpose |
|-------|---------|
| `admin` | System administrators |
| `buyers` | Purchasing staff |
| `approvers` | Anyone who approves (include buyers) |
| `cc[number]_supervisor` | Cost center supervisors |
| `cc[number]_manager` | Cost center managers |
| `cc[number]_director` | Cost center directors |

**Tip:** Use groups even for single users - makes personnel changes easier.

---

## Supervisors

### How is the supervisor hierarchy set up?

Each user has a `wus_supervisor` field pointing to their supervisor's user ID. This creates the org chart hierarchy used for:
- Supervisor chain approval routing
- Escalation emails
- $SUPERVISORS variables in approval rules

### What if someone has no supervisor?

The chain stops. If using supervisor-based approval, ensure everyone has a supervisor assigned (except the top executive).

---

## User Profile Fields

### What are the key user profile fields?

| Field | Description |
|-------|-------------|
| `wus_id` | User ID (login) |
| `wus_name` | Full name |
| `wus_email` | Email address (used for SSO matching) |
| `wus_supervisor` | Supervisor's user ID |
| `wus_app_amt` | Approval dollar limit |
| `wus_delegate` | Current delegate (for OOF) |
| `wus_domains` | Domains user can access |
| `wus_disable` | TRUE = account disabled |

---

## Domains

### How do I control which domains a user can access?

Set in the user's `wus_domains` field:

| Value | Access |
|-------|--------|
| `*` | All domains in ALLOWED_DOMAINS |
| `demo1,demo2` | Only listed domains |
| `demo1,*` | Listed domain plus all system domains |

---

## Disabling Users

### How do I disable a user account?

Set `wus_disable = TRUE` in their user profile.

**Effects:**
- User cannot log in
- User cannot be selected as approver or delegate
- Existing pending approvals should be reassigned

---

## See Also

- [Users and Groups Screen](../../admin/screens/01-users-and-groups.md) - Administration screen
- [Approvals FAQ](../ipurchase/approvals.md) - Delegation and escalation
- [SSO Azure Setup](sso-azure-setup.md) - Single Sign-On configuration

---

*Last Updated: January 2026*
