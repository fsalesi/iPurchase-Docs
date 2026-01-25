# ALLOW_TEMP_VENDORS - iPurchase System Setting

**Category:** Catalog & Vendors

TRUE | FALSE.

### Valid Values

| Value | Behavior |
|-------|----------|
| **TRUE** | allows use of temporary/unverified vendors on requisitions |
| **FALSE** | temporary vendors are rejected |

### How It Works

This permission setting controls whether users can perform specific actions within the system.

### Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | ALLOW_TEMP_VENDORS |
| **Category** | Catalog & Vendors |
| **Owner** | Purchasing |
| **Default Value** | FALSE |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'ALLOW_TEMP_VENDORS'
```