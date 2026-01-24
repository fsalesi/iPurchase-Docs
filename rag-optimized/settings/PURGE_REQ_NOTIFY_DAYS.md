# PURGE_REQ_NOTIFY_DAYS - iPurchase System Setting

**Category:** Requisitions

This setting allows the administrator to set how many days in advanced the originator will get notified before a requisition is purged from the iPurchase system. The setting works in conjunction with PURGE_REQ_DAYS.

### How It Works

See the description above for details on how this setting affects system behavior.

### Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | PURGE_REQ_NOTIFY_DAYS |
| **Category** | Requisitions |
| **Owner** | Admin |
| **Default Value** | 10 |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'PURGE_REQ_NOTIFY_DAYS'
```