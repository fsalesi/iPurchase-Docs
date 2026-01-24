# APP_SUPERVISOR_SEQ - iPurchase System Setting

**Category:** Approval Workflow

This is the Approval Level or Sequence when adding supervisors to the approval routing.

### How It Works

See the description above for details on how this setting affects system behavior.

### Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | APP_SUPERVISOR_SEQ |
| **Category** | Approval Workflow |
| **Owner** | Admin |
| **Default Value** | 10 |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'APP_SUPERVISOR_SEQ'
```