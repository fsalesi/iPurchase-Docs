# AUTO_RECEIVE - iPurchase System Setting

**Category:** Receiving

TRUE | FALSE.

### Valid Values

| Value | Behavior |
|-------|----------|
| **TRUE** | automatically creates receipt transactions when purchase order is created |
| **FALSE** | Disables this feature |

### How It Works

This setting configures receiving behavior in iPurchase.

### Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | AUTO_RECEIVE |
| **Category** | Receiving |
| **Owner** | Purchasing |
| **Default Value** | FALSE |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'AUTO_RECEIVE'
```

### Related Settings

- [AUTO_RECEIVE_TIME](AUTO_RECEIVE_TIME.md)