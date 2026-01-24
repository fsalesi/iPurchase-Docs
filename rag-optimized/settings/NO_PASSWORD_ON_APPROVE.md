# NO_PASSWORD_ON_APPROVE - iPurchase System Setting

**Category:** Security & Authentication

Controls which users are NOT prompted for password re-entry when approving or rejecting requisitions. Typically used with SSO environments or for streamlined approval workflows.

### How It Works

By default, iPurchase prompts users to re-enter their password when approving or rejecting. Users in this list bypass that prompt for faster approval processing.

### Valid Values

This setting uses [Can-Do list format](../../reference/can-do-list-format.md).

| Value | Behavior |
|-------|----------|
| `*` (asterisk) | No one prompted for password on approve |
| Blank/empty | Everyone prompted for password (DEFAULT) |
| User/Group list | Listed users skip password prompt |

### Security Consideration

Disabling password prompts reduces security. Consider using this setting only:
- In SSO environments where authentication is handled externally
- For high-volume approvers where productivity outweighs security concerns
- In combination with other security controls

### Common Questions

- What is NO_PASSWORD_ON_APPROVE?
- How do I disable password prompts for SSO users?
- Can I skip the password check when approving?

### Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | NO_PASSWORD_ON_APPROVE |
| **Category** | Security & Authentication |
| **Owner** | Admin |
| **Default Value** | (none) |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'NO_PASSWORD_ON_APPROVE'
```

### Related Settings

- [PASSWORD_RULES](PASSWORD_RULES.md) - Password complexity requirements
