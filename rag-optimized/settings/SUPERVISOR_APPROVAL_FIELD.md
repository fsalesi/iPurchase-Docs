# SUPERVISOR_APPROVAL_FIELD - iPurchase System Setting

**Category:** Approval Workflow

Field name. Database field used to determine supervisor chain (default: wus_supervisor).

### How It Works

See the description above for valid values and usage.

### Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | SUPERVISOR_APPROVAL_FIELD |
| **Category** | Approval Workflow |
| **Owner** | Admin |
| **Default Value** | wus_supervisor |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'SUPERVISOR_APPROVAL_FIELD'
```
