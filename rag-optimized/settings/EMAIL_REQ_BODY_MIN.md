# EMAIL_REQ_BODY_MIN - iPurchase System Setting

**Category:** Email Configuration

When this is TRUE, only the supplier's number and name along with the cost of the requisition are embedded in the email. If the requisition is a change order, then the words "Change Order" will also appear. This requires NO_EMAIL_REQ_BODY set to false, otherwise EMAIL_REQ_BODY_MIN will have no affect.

### How It Works

### Valid Values

| Value | Behavior |
|-------|----------|
| `TRUE` | Enabled |
| `FALSE` | Disabled |

### Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | EMAIL_REQ_BODY_MIN |
| **Category** | Email Configuration |
| **Owner** | Admin |
| **Default Value** | FALSE |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'EMAIL_REQ_BODY_MIN'
```
