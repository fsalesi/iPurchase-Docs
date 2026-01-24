# EMAIL_SUPPLIER_PO_CC - iPurchase System Setting

**Category:** Email Configuration

This is a list of email address(s) of whom to carbon copy the supplier email to when the PO is created.  A value of "BUYER" will copy the associated buyer which is set on the requisition. If a user is included in this setting and has OOF turned on, their delegate will receive a carbon copy of the supplier email. The administrator can also add static email addresses to this setting or use these other values: $xxreq_buyer = Buyer $xxreq_User ID = Originator $xxreq_obo = On Behalf Of $xxreq_deliver_to = Deliver To

### How It Works

See the description above for details on how this setting affects system behavior.

### Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | EMAIL_SUPPLIER_PO_CC |
| **Category** | Email Configuration |
| **Owner** | Power Users |
| **Default Value** | $xxreq_buyer,$xxreq_obo,$xxreq_userid |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'EMAIL_SUPPLIER_PO_CC'
```