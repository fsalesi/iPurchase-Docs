# TEST_SYSTEM - iPurchase System Setting

**Category:** System Configuration

⚠️ **DEPRECATED** - This database setting is no longer used. Set the TEST_SYSTEM environment variable on the application server instead.

### Current Recommendation

Configure TEST_SYSTEM as an operating system environment variable on your PASOE/AppServer instance:

```
TEST_SYSTEM=TRUE
```

This setting identifies the environment as a test/development system, which may affect:
- Email notifications (may be suppressed or redirected)
- System branding/indicators
- Integration behaviors

### Migration Note

If you have this setting configured in pf_mstr, it will be ignored. Remove it and configure the environment variable instead.

### Common Questions

- What is TEST_SYSTEM?
- How do I mark a system as test/development?
- Why isn't my TEST_SYSTEM setting working?

### Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | TEST_SYSTEM |
| **Category** | System Configuration |
| **Owner** | Admin |
| **Default Value** | FALSE |
| **Status** | ⚠️ DEPRECATED |

### How to Query

```sql
-- This setting is deprecated - check environment variable instead
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'TEST_SYSTEM'
```

### Related Settings

- [TEST_SETTINGS](TEST_SETTINGS.md)
