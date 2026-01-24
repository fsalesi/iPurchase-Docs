# BATCH_APPROVE_GROUPS - iPurchase System Setting

**Category:** Approval Workflow

Comma Separated list of User ID's or Group ID's that will allow an approver to approve multiple requisitions simultaneously from the Requisition Inquiry screen.  If the user is a member of the specified groups then the user does not need to go into each requisition in order to approve. A checkbox is displayed on the inquiry screen next to each requisition where the approver for the requisition is the logged in user. If the requisition has been delegated to the logged in user, then the checkbox will not be displayed and the user must go into the requisition in order to approve. The approver will check all the requisitions that they want to approve and then click the Batch Approve button. Asterisk indicates everyone, a blank indicates no one.

### How It Works

This setting uses [Can-Do list format](../../reference/can-do-list-format.md) for specifying users and groups.

### Valid Values

| Value | Behavior |
|-------|----------|
| `*` (asterisk) | Everyone/all users |
| Blank/empty | No one/disabled |
| User/Group list | Only specified users/groups |

### Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | BATCH_APPROVE_GROUPS |
| **Category** | Approval Workflow |
| **Owner** | Admin |
| **Default Value** | (none) |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'BATCH_APPROVE_GROUPS'
```
