# INQUIRY_AFTER_REJECT - iPurchase System Setting

**Category:** Reporting & Inquiry

Comma separated list of User ID's or Group ID's that are re-directed to the pending queue once they have rejected a requisition. Asterisk indicates everyone, a blank indicates no one. This setting determines whether control goes back to the find screen after a requisition has been rejected, or whether it redisplays the requisition.

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
| **Setting Name** | INQUIRY_AFTER_REJECT |
| **Category** | Reporting & Inquiry |
| **Owner** | Power Users |
| **Default Value** | * |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'INQUIRY_AFTER_REJECT'
```
