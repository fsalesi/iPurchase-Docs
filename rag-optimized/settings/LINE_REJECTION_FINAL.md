# LINE_REJECTION_FINAL - iPurchase System Setting

**Category:** Uncategorized

If USE_LINE_APPROVALS = TRUE then you can also set whether or not any items which were previously rejected, can be re-approved by a subsequent approver. A value of TRUE will disallow anyone from approving a previously rejected line. A value of FALSE will allow any approver the option of re-approving a previously rejected line item. If the value is true, then iPurchase will recheck the approval routing after each approval. If the rejection of lines causes an approver to no longer be required, then this approver will be removed from the routing. An approver that has been removed can be added back by the system rules, if needed. If all items on a requisition have been rejected, then the approver will be forced to reject the requisition. If they try to approve, an error will be raised.

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
| **Setting Name** | LINE_REJECTION_FINAL |
| **Category** | Uncategorized |
| **Owner** | Power Users |
| **Default Value** | TRUE |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'LINE_REJECTION_FINAL'
```