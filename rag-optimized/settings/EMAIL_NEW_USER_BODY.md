# EMAIL_NEW_USER_BODY - iPurchase System Setting

**Category:** Email Configuration

Email body template sent to newly created users with their login credentials and instructions.

### How It Works

When an administrator creates a new user account, iPurchase can automatically send a welcome email. This setting defines the email body content.

**Available tokens for substitution:**
- `$User ID` - The user's login ID
- `$PASSWORD` - The user's initial password
- `$URL` - Link to the iPurchase login page

**Example:**
```
Welcome to iPurchase!

Your account has been created:
User ID: $User ID
Password: $PASSWORD

Please log in at: $URL

Change your password after first login.
```

### Valid Values

Text or HTML content with optional token substitution.

### Common Questions

- How do I customize the new user welcome email?
- What information is sent to new users?
- Can I include HTML in the welcome email?

### Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | EMAIL_NEW_USER_BODY |
| **Category** | Email Configuration |
| **Owner** | Admin |
| **Default Value** | (none) |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'EMAIL_NEW_USER_BODY'
```

### Related Settings

- [EMAIL_NEW_USER_SUBJECT](EMAIL_NEW_USER_SUBJECT.md) - Subject line for new user email
