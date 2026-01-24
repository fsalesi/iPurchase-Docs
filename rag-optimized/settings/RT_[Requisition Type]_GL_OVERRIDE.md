# RT_[Requisition Type]_GL_OVERRIDE - iPurchase System Setting

**Category:** Requisitions

True or False If you set this setting to TRUE, then all items entered in the line entry screen for the specified requisition type will have the account, sub-account, and cost center set to the values which QAD would dictate based on the vendor and item. This setting will override all other account, sub-account, and cost center settings. This setting can also be at the system level ' see GL_Override.

### How It Works

See the description above for details on how this setting affects system behavior.

### Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | RT_[Requisition Type]_GL_OVERRIDE |
| **Category** | Requisitions |
| **Owner** | Finance |
| **Default Value** | False  |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'RT_[Requisition Type]_GL_OVERRIDE'
```