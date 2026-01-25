# Supervisor Override - iPurchase

**Purpose:** How supervisors can approve on behalf of their subordinates without explicit delegation.

### ALLOW_SUPERVISORS_TO_APPROVE Setting

Can-Do list of users/groups who can approve on behalf of their subordinates.

**Values:**
- `*`: All supervisors can override
- Blank: No supervisors can override
- `"manager1,exec_group"`: Specific users/groups only

**Behavior:**
- Supervisor can approve or reject requisitions for their direct reports
- Use case: "My employee is stuck, I'll just approve it for them"
- Separate from delegation (doesn't require delegate to be set)
- Creates audit trail similar to delegation
