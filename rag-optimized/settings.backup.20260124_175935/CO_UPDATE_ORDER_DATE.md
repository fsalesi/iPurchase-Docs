# CO_UPDATE_ORDER_DATE - iPurchase System Setting

**Category:** Purchase Orders

Update the order date on the change order PO to today's date

**Common questions this answers:**
- What is CO_UPDATE_ORDER_DATE?
- What does CO_UPDATE_ORDER_DATE do?
- What is the default value for CO_UPDATE_ORDER_DATE?
- How do I configure CO_UPDATE_ORDER_DATE?

## Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | CO_UPDATE_ORDER_DATE |
| **Category** | Purchase Orders |
| **Owner** | Purchasing |
| **Default Value** | FALSE |

## How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'CO_UPDATE_ORDER_DATE'
```
