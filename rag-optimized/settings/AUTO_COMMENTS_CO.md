# AUTO_COMMENTS_CO - iPurchase System Setting

**Category:** Purchase Orders

Use this setting to automatically attach comments to every Purchase Order REVISION - CHANGE ORDER. This is a pointer to the code_mstr field name (code_fldname) value to be used. Example: List:Buyer1:MC1^REF1^Type1^Lang1^Page1| MC2^REF1^Type1^Lang1^Page2, Buyer2:MC2^REF1^Type1^Lang1^Page1 Ex: REF1^Type1^Lang1^Page1| REF1^Type1^Lang1^Page2| REF1^Type1^Lang1^Page1 The Type, Lang, and Page options are all optional.

### How It Works

See the description above for details on how this setting affects system behavior.

### Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | AUTO_COMMENTS_CO |
| **Category** | Purchase Orders |
| **Owner** | Power Users |
| **Default Value** | (none) |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'AUTO_COMMENTS_CO'
```