# USER_PROFILE_FIELDS - iPurchase System Setting

**Category:** User Management

Specifies custom user profile fields to display and allow editing in the user management screens.

### How It Works

iPurchase user records contain standard fields (name, email, department, etc.) plus custom fields that can be organization-specific. This setting controls which custom fields appear in the user profile interface.

**Use cases:**
- Display employee ID or badge number
- Show cost center assignments
- Include department codes
- Add custom organizational attributes

### Valid Values

Comma-separated list of field names from the user table (wus_mstr).

**Example:**
```sql
USER_PROFILE_FIELDS = "wus_emp_id,wus_badge,wus_division"
```

### Common Questions

- How do I add custom fields to user profiles?
- What user fields can I display?
- How do I show employee ID on user screens?

### Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | USER_PROFILE_FIELDS |
| **Category** | User Management |
| **Owner** | Admin |
| **Default Value** | (none) |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'USER_PROFILE_FIELDS'
```

### Related Settings

- [USER_IMPORT_FOLDER](USER_IMPORT_FOLDER.md)
