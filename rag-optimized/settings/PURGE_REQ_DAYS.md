# PURGE_REQ_DAYS - iPurchase System Setting

**Category:** Requisitions

This setting allows the administrator to set how many days a requisition will be purged based on no activity from either the entry date, last audit record date(header or detail), or last approval record.  This setting works based on whichever has the last activity date.  When the system starts to purge requisitions, it will send the originator an email that this job is running.

### How It Works

See the description above for details on how this setting affects system behavior.

### Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | PURGE_REQ_DAYS |
| **Category** | Requisitions |
| **Owner** | Admin |
| **Default Value** | 90 |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'PURGE_REQ_DAYS'
```