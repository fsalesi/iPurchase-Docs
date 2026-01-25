# TEST_SETTINGS - iPurchase System Setting

**Category:** System Configuration

Comma-separated list of environment-specific settings that should be preserved when copying production database to dev/test.

### How It Works

This setting configures system configuration behavior in iPurchase.

### Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | TEST_SETTINGS |
| **Category** | System Configuration |
| **Owner** | Admin |
| **Default Value** | (none) |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'TEST_SETTINGS'
```

### Related Settings

- [TEST_SYSTEM](TEST_SYSTEM.md)
