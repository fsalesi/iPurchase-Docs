# RT_[Requisition Type]_[Site]_DEPT_RANGE - iPurchase System Setting

**Category:** Requisitions

Substitute the requisition type for "[REQUISITION TYPE]" and site for "[SITE]". This setting allows specifying valid departments (cost centers) for a specific requisition type. The field uses the Progress "Can-Do" function. See Progress help if needed. A sample value can be  5521,!5622,56*,7*,!* This is interpreted as department 5521 is valid, department 5622 is not valid, any department that begin with 56 (except 5622) are valid, any departments that begin with a 7 are valid, and finally, all other departments are invalid.

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
| **Setting Name** | RT_[Requisition Type]_[Site]_DEPT_RANGE |
| **Category** | Requisitions |
| **Owner** | Finance |
| **Default Value** | (none) |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'RT_[Requisition Type]_[Site]_DEPT_RANGE'
```