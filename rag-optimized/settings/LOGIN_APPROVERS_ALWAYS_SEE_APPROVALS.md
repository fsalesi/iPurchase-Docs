# LOGIN_APPROVERS_ALWAYS_SEE_APPROVALS - iPurchase System Setting

**Category:** Approval Workflow

A comma separated list of User ID's or Group ID's that will always be logged into their pending queue, regardless of whether they do or do not have pending requisition to approve. Asterisk indicates everyone, a blank indicates no one.

### How It Works

This setting uses [Can-Do list format](../../reference/can-do-list-format.md) for specifying users and groups.

**Common patterns:**
- `*` - Everyone/all values allowed
- (blank) - No one/feature disabled
- `user1,user2` - Specific users only
- `group1,!user1` - Group members except specific user

### Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | LOGIN_APPROVERS_ALWAYS_SEE_APPROVALS |
| **Category** | Approval Workflow |
| **Owner** | Power Users |
| **Default Value** | * |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'LOGIN_APPROVERS_ALWAYS_SEE_APPROVALS'
```