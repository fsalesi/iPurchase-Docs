# BATCH_APPROVE_GROUPS_ALWAYS - iPurchase System Setting

**Category:** Approval Workflow

Comma-Separated list of User ID's or Group ID's. By default, the setting BATCH_APPROVE_GROUPS will only allow you to batch approve for requisitions that specifically include yourself. Batch approval is disabled for requisitions which are delegated to you. Any member of this group setting will be allowed to always batch approve, including delegated requisitions. Asterisk indicates everyone, a blank indicates no one. The Final Approver will not be allowed to batch approve a requisition.

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
| **Setting Name** | BATCH_APPROVE_GROUPS_ALWAYS |
| **Category** | Approval Workflow |
| **Owner** | Admin |
| **Default Value** | (none) |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'BATCH_APPROVE_GROUPS_ALWAYS'
```