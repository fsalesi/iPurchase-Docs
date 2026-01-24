# GL_OVERRIDE - iPurchase System Setting

**Category:** GL Accounts & Finance

If you set this setting to true, then all items entered in the line entry screen will have the account, sub-account, and cost center set to the values which QAD would dictate based on the vendor and item.  This setting will override all other account, sub-account, and cost center settings. This setting can also be at the requisition type level � see RT_[Requisition Type]_GL_Override

### How It Works

See the description above for valid values and usage.

### Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | GL_OVERRIDE |
| **Category** | GL Accounts & Finance |
| **Owner** | Finance |
| **Default Value** | FALSE |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'GL_OVERRIDE'
```
