# PORTAL_CONFIRM_RECEIPT_URL - iPurchase System Setting

**Category:** Portal Integration

URL endpoint for portal receipt confirmation integration. Used for external portal systems.

### How It Works

See the description above for details on how this setting affects system behavior.

### Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | PORTAL_CONFIRM_RECEIPT_URL |
| **Category** | Portal Integration |
| **Owner** | ISS |
| **Default Value** | (none) |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'PORTAL_CONFIRM_RECEIPT_URL'
```