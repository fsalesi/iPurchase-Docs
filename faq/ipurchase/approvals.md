# Approvals FAQ

Common questions about approval workflows, delegation, and escalation.

---

## Self-Approval

### Can someone approve their own requisition?

**Short Answer:** Controlled by `USE_APP_AMOUNT_OWN_REQS` setting.

| Setting Value | Behavior |
|---------------|----------|
| `YES` | User can approve their own req IF the amount is within their approval limit |
| `NO` | User can never approve their own req - must go to supervisor |

**Related Settings:**

| Setting | Description |
|---------|-------------|
| `REMOVE_ORIG` | Remove originator from approval routing |
| `REMOVE_ORIG_CO` | Remove originator from change order routing |
| `REMOVE_ORIGINATOR_FROM_GROUP` | Remove originator even if they're in an approval group |

---

## Supervisor Escalation

### How does supervisor escalation work?

When a requisition is pending approval for too long, it automatically escalates to the approver's supervisor.

**Key Settings:**

| Setting | Description | Recommended |
|---------|-------------|-------------|
| `SUPERVISOR_ESCALATION_DAYS` | Days before escalation | 5-8 days (skips weekends) |
| `SUPERVISOR_ESCALATION_LEVEL` | How many levels up to escalate | 99 (all levels) |
| `ALLOW_SUPERVISORS_TO_APPROVE` | Can escalated supervisor approve? | YES |
| `ESCALATION_EXCEPT_USERS` | Users who don't receive escalation emails | CEO, executives |

**How it works:**
1. Requisition sits pending for X days (SUPERVISOR_ESCALATION_DAYS)
2. System sends escalation email to approver's supervisor
3. Supervisor can click the req link and approve/reject
4. If supervisor approves, they're recorded as the approver and routing continues

**Tip:** Set 5-8 days so it doesn't escalate while someone is on vacation.

### Can I prevent certain people from getting escalation emails?

Yes. Add their user IDs to `ESCALATION_EXCEPT_USERS`. This is commonly used for executives like the CEO who shouldn't receive routine escalation emails.

---

## Out of Office / Delegation

### How does Out-of-Office delegation work?

Users can assign a delegate to handle their approvals while they're away.

**Key Settings:**

| Setting | Description |
|---------|-------------|
| `ALLOW_OOF` | Enable Out-of-Office functionality |
| `OOF_LIMIT_BY_DEPT` | Limit delegates to same department |
| `OOF_LIMIT_BY_DOLLARS` | Limit delegates to users with equal/higher approval amount |
| `OOF_LIMIT_TO_APPROVERS` | Limit delegates to users who are approvers |
| `OOF_NOTIFY_OLD` | Email pending reqs to new delegate |

**Important Notes:**
- Only ONE delegate per person at a time
- Delegate takes on the OOF person's approval authority
- Delegate's own approval limit doesn't matter - they're approving on behalf of the OOF person
- Administrators can assign delegates through User Administration

### Can a user delegate to anyone?

Depends on your settings:
- `OOF_LIMIT_BY_DEPT = TRUE` → Only users in same department
- `OOF_LIMIT_BY_DOLLARS = TRUE` → Only users with same or higher approval limit
- `OOF_LIMIT_TO_APPROVERS = TRUE` → Only users who are approvers
- All FALSE → User can delegate to any iPurchase user

---

## Emergency Approvals

### What is an emergency approval?

Emergency approval bypasses the entire approval workflow and immediately creates a PO.

**Key Points:**
- Auto-generates a PO immediately
- Bypasses ALL other approvals
- All would-be approvers receive notification email
- Fully tracked in audit trail
- NOT intended for out-of-office situations

**Setting:** `FORCE_APPROVAL_ROLE_LIST` = group of users allowed to emergency approve

**Example Use Case:** Production machine is down and needs emergency repair parts ordered immediately.

**Recommendation:** Most organizations disable this (`FORCE_APPROVAL_ROLE_LIST` = blank) or limit to a very small group.

---

## Password on Approval

### Do users need to re-enter their password when approving?

Controlled by `NO_PASSWORD_ON_APPROVE` setting.

| Setting Value | Behavior |
|---------------|----------|
| `*` (asterisk) | No one needs to re-enter password |
| blank | Everyone must re-enter password |
| `group1,group2` | Listed groups don't need to re-enter |

**Note:** Users are already authenticated at login. This is an *additional* authentication step during approval. All approvals are logged in the audit trail regardless of this setting.

---

## Approval Amounts

### How are approval amounts determined?

Each user has an approval limit set in their profile (`wus_app_amt` field).

**Supervisor Chain Approval:**
- Requisition routes up the supervisor hierarchy
- Each supervisor approves until reaching someone whose limit exceeds the req amount
- That person is the final approver in the chain

**Example:**
- Req amount: $15,000
- Supervisor 1 limit: $5,000 → Approves, routes up
- Supervisor 2 limit: $10,000 → Approves, routes up  
- Supervisor 3 limit: $25,000 → Approves, chain complete

### What amount is used for approval routing?

Always use the **GL/base currency amount** (`xxreq_cost_gl`), not the requisition currency amount. This ensures consistent approval thresholds regardless of what currency the requisition is entered in.

---

## Modifying Pending Requisitions

### Can approvers modify a requisition while it's pending?

Controlled by several settings:

| Setting | Description |
|---------|-------------|
| `ALWAYS_ALLOW_REQ_EDIT_ORIGINATOR` | Originator can always edit |
| `ALWAYS_ALLOW_REQ_EDITS` | Groups that can edit pending reqs |
| `EDIT_ANYTIME` | Groups that can edit at any stage |
| `ALWAYS_ALLOW_ATTACHMENTS` | Groups that can add attachments to approved reqs |

**Common Configuration:**
```
ALWAYS_ALLOW_REQ_EDITS = buyers
EDIT_ANYTIME = buyers
ALWAYS_ALLOW_ATTACHMENTS = buyers
```

**Important:** Edits are all-or-nothing. You cannot allow someone to edit only specific fields (like GL account) without allowing them to edit everything.

**Alternative Approach:** Require rejection with explanation, forcing originator to fix and resubmit.

---

## Adding Approvers

### Can I manually add an approver to a requisition?

Yes, using the "Add Approver" function. 

**Key Points:**
- Manually added approvers do NOT trigger rerouting
- Added approver is recorded in audit trail
- Does not affect the normal approval simulation

---

## See Also

- [Approval Strategy Guide](../../reference/approval-strategy-guide.md) - Rule configuration
- [Requisition Rerouting](reroute-rules.md) - When approvals reroute
- [User Management](../general/user-management.md) - User setup and permissions
- [System Settings FAQ](../general/system-settings.md) - Domain-specific settings

---

*Last Updated: January 2026*
