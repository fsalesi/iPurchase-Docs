# USE_CHAINED_DELEGATES - iPurchase System Setting

**Category:** Out of Office / Delegation

Controls whether delegation chains are allowed - when a delegate can further delegate to another user.

### Valid Values

| Value | Behavior |
|-------|----------|
| **TRUE** | Allow unlimited delegation chains (DEFAULT) |
| **FALSE** | Only direct delegation allowed (recommended) |

### How It Works

When users set up Out of Office delegation, this setting determines if chains are permitted:

**TRUE (Chains allowed):**
- User A delegates to User B
- User B delegates to User C
- User C can approve on behalf of User A

**FALSE (No chains - recommended):**
- User A delegates to User B
- User B delegates to User C
- User C can only approve on behalf of User B, NOT User A

**Why FALSE is recommended:**
- Prevents confusion about approval authority
- Clearer audit trail
- Avoids unintended privilege escalation
- Easier to track who actually approved what

**Example problem with chains:**
```
Jane → Bob → Sue → Tom
Jane goes on vacation, delegates to Bob
Bob goes on vacation, delegates to Sue
Sue goes on vacation, delegates to Tom
Tom can now approve Jane's $1M requisitions!
```

### Common Questions

- Can my delegate's delegate approve for me?
- How do I prevent delegation chains?
- Why is my approval going to someone unexpected?
- What is chained delegation?

### Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | USE_CHAINED_DELEGATES |
| **Category** | Out of Office / Delegation |
| **Owner** | Power Users |
| **Default Value** | TRUE |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'USE_CHAINED_DELEGATES'
```

### Related Settings

- [ALLOW_OOF](ALLOW_OOF.md) - Enable/disable Out of Office feature
- [OOF_LIMIT_TO](OOF_LIMIT_TO.md) - Restrict who can be a delegate
- [OOF_LIMIT_BY_DEPT](OOF_LIMIT_BY_DEPT.md) - Require same department
- [OOF_LIMIT_BY_DOLLARS](OOF_LIMIT_BY_DOLLARS.md) - Require sufficient approval limit
