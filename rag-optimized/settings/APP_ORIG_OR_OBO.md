# APP_ORIG_OR_OBO - iPurchase System Setting

**Category:** Approval Workflow

ORIGINATOR | OBO. Determines whether approval rule xxapp_orig field matches against the requisition originator (xxreq_userid) or the On Behalf Of person (xxreq_obo). Affects approval rule evaluation and reporting.

### How It Works

See the description above for details on how this setting affects system behavior.

### Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | APP_ORIG_OR_OBO |
| **Category** | Approval Workflow |
| **Owner** | Admin |
| **Default Value** | OBO |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'APP_ORIG_OR_OBO'
```