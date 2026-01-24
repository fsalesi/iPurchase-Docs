# NEW_REROUTE_METHOD - iPurchase System Setting

**Category:** Approval Workflow

TRUE | FALSE. If TRUE, uses new rerouting algorithm for change orders.

### Valid Values

| Value | Behavior |
|-------|----------|
| **TRUE** | Enables this feature |
| **FALSE** | Disables this feature |

### How It Works

See the description above for details on how this setting affects system behavior.

### Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | NEW_REROUTE_METHOD |
| **Category** | Approval Workflow |
| **Owner** | Admin |
| **Default Value** | FALSE |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'NEW_REROUTE_METHOD'
```