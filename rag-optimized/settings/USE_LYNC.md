# USE_LYNC - iPurchase System Setting

**Category:** Uncategorized

This setting allows the administrator to allow the use of Lync within the iPurchase solution. Requirements: Office 2010+ with Lync installed on desktop. iPurchase website must be in the "TRUSTED SITES" security zone in the Internet Options or Security tab. Does not work with office for Mac Does not work with mobile devices Does not work with certain browsers. Not all trading partners that use Lync will allow you to see the presence of employees. Works with IE9+. Not supported for other PC browsers, however it does work. On requisition workbench, the following fields will show Lync Presence status icons: Supplier Email Buyer Originator OBO Deliver To All Approvers in approval history tab.

### How It Works

See the description above for valid values and usage.

### Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | USE_LYNC |
| **Category** | Uncategorized |
| **Owner** | Admin |
| **Default Value** | FALSE |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'USE_LYNC'
```
