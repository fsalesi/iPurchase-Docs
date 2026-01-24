# RESTRICT_USER_DEPARTMENTS - iPurchase System Setting

**Category:** User Management

Is the department selection limited to those departments defined in the user's profile?  If the value of this is True then in User Maintenance you should set up the "Default Dept" field as follows. The first comma-separated entry is the default department. The next set of comma-separated entries is a list of departments that are valid or invalid for the user. The logic works using the can-do Progress statement. A sample value can be 5521,!5622,56*,7*,!* This is interpreted as department 5521 is the default and is valid, department 5622 is not valid, any departments that begin with 56 (except 5622) are valid, any departments that begin with a 7 are valid, and finally, all other departments are invalid. You can also simply supply a list of valid departments. Ex: 2000,2010,2020 This would limit the choice to any of the three departments and uses 2000 as the default. If using the RT_[Requisition Type]_DEPT_RANGE setting to limit departments by requisition type, then in order for the department to be in the selection, it must be valid for both the user and the requisition type.

### Valid Values

| Value | Behavior |
|-------|----------|
| **TRUE** | Enables this feature |
| **FALSE** | Disables this feature |

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
| **Setting Name** | RESTRICT_USER_DEPARTMENTS |
| **Category** | User Management |
| **Owner** | Power Users |
| **Default Value** | FALSE |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'RESTRICT_USER_DEPARTMENTS'
```