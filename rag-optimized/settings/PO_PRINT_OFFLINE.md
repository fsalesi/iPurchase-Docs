# PO_PRINT_OFFLINE - iPurchase System Setting

**Category:** Purchase Orders

This setting will control when the New PO Created email and original PO Print occur. A value of FALSE, the default, will print the PO and send the email as soon as the Purchase Order is created. Most of the time this happens when the final approver clicks the Approve button. However, a value of TRUE, will delay the printing of the PO and the email to the buyer or supplier by queuing up this request in the iPurchase jobs. You would set this to true when you want increased perceived performance so that the final approver doesn't need to wait for this action to be completed. YOU ARE REQUIRED TO SET THIS TO TRUE IF YOU ARE USING THE QAD REPORTING FRAMEWORK. *QAD EE Only

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
| **Setting Name** | PO_PRINT_OFFLINE |
| **Category** | Purchase Orders |
| **Owner** | Admin |
| **Default Value** | FALSE |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'PO_PRINT_OFFLINE'
```