# EMAIL_NO_APPROVE_LINK - iPurchase System Setting

**Category:** Approval Workflow

True or False - Include link to Approve in email that goes out to approver. Default FALSE

### Valid Values

| Value | Behavior |
|-------|----------|
| **TRUE** | Enables this feature |
| **FALSE** | Disables this feature |

### How It Works

See the description above for details on how this setting affects system behavior.

### Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | EMAIL_NO_APPROVE_LINK |
| **Category** | Approval Workflow |
| **Owner** | Admin |
| **Default Value** | FALSE |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'EMAIL_NO_APPROVE_LINK'
```