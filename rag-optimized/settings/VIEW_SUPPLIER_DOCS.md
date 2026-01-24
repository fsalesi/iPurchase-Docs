# VIEW_SUPPLIER_DOCS - iPurchase System Setting

**Category:** User Management

True or False or list of users groups. Default value is blank. Will give the users access to the "Contacts" button in Requisition Workbench

### How It Works

See the description above for details on how this setting affects system behavior.

### Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | VIEW_SUPPLIER_DOCS |
| **Category** | User Management |
| **Owner** | Admin |
| **Default Value** | buyers,admin |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'VIEW_SUPPLIER_DOCS'
```