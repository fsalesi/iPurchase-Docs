# EMAIL_PO_INCLUDE_SIG - iPurchase System Setting

**Category:** Email Configuration

This setting includes the buyer's contact information for emails automatically sent to suppliers when PO is created. It also includes logged in user's contact information in emails which are manually sent through iPurchase.

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
| **Setting Name** | EMAIL_PO_INCLUDE_SIG |
| **Category** | Email Configuration |
| **Owner** | Purchasing |
| **Default Value** | TRUE |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'EMAIL_PO_INCLUDE_SIG'
```