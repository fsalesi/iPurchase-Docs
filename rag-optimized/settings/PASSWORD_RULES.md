# PASSWORD_RULES - iPurchase System Setting

**Category:** Security & Authentication

Defines password complexity requirements as a comma-separated list of 7 values. Each position controls a specific requirement for user passwords.

### Format

The value is a comma-separated list with 7 positions (no spaces):
`position1,position2,position3,position4,position5,position6,position7`

| Position | Requirement | Values |
|----------|-------------|--------|
| 1 | Require a number | 0=no, 1=yes |
| 2 | Require a special character | 0=no, 1=yes |
| 3 | Require number OR special char | 0=no, 1=yes |
| 4 | Require uppercase letter | 0=no, 1=yes |
| 5 | Require lowercase letter | 0=no, 1=yes |
| 6 | Minimum password length | number |
| 7 | Cannot reuse last X passwords | number (0=no limit) |

### Examples

| Rule | Meaning |
|------|---------|
| `1,0,0,0,0,6,0` | Require number, min 6 chars (DEFAULT) |
| `0,1,0,0,0,5,0` | Require special char, min 5 chars |
| `1,1,0,0,0,8,0` | Require number AND special char, min 8 chars |
| `0,0,1,0,0,8,0` | Require number OR special char, min 8 chars |
| `0,0,0,1,1,6,0` | Require upper AND lower case, min 6 chars |
| `0,0,0,0,0,0,5` | Cannot reuse last 5 passwords |

### Common Questions

- What is PASSWORD_RULES?
- How do I set password requirements?
- How do I require special characters in passwords?
- How do I set minimum password length?
- How do I prevent password reuse?

### Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | PASSWORD_RULES |
| **Category** | Security & Authentication |
| **Owner** | Admin |
| **Default Value** | 1,0,0,0,0,6,0 |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'PASSWORD_RULES'
```

### Related Settings

- [PASSWORD_EXPIRE_DAYS](PASSWORD_EXPIRE_DAYS.md) - Days until password expires
- **PASSWORD_REMINDER_DAYS** - Days before expiration to warn user
- **FAILED_LOGIN_ATTEMPTS** - Lockout after X failed attempts
