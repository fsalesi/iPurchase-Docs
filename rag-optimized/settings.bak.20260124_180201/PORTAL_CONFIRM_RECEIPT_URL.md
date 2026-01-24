# PORTAL_CONFIRM_RECEIPT_URL - iPurchase System Setting

**Category:** Portal Integration

URL endpoint for portal receipt confirmation integration. Used for external portal systems.

**Common questions this answers:**
- What is PORTAL_CONFIRM_RECEIPT_URL?
- What does PORTAL_CONFIRM_RECEIPT_URL do?
- What is the default value for PORTAL_CONFIRM_RECEIPT_URL?
- How do I configure PORTAL_CONFIRM_RECEIPT_URL?

## Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | PORTAL_CONFIRM_RECEIPT_URL |
| **Category** | Portal Integration |
| **Owner** | ISS |
| **Default Value** | (none) |

## How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'PORTAL_CONFIRM_RECEIPT_URL'
```
