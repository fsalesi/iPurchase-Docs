# AUTO_COMMENTS_LINE_SITE - iPurchase System Setting

**Category:** Purchase Orders

Use this setting to automatically attach comments to every Purchase Order when a particular buyer or bill to or ship to or site or line site is used. This is a pointer to the code_mstr field name (code_fldname) value to be used. You can also use the prefix "LIST:" followed by a comma-separated list of values. This will tell iPurchase that the specified list is to be used. Example: List:Buyer1:MC1^REF1^Type1^Lang1^Page1| MC2^REF1^Type1^Lang1^Page2, Buyer2:MC2^REF1^Type1^Lang1^Page1 The list is as follows; It must begin with the literal "LIST:". Next is a comma-separated list of buyer User IDs. Each User ID can have one or more associated master comment pointers. After the User ID add a colon (:) followed by the master comment reference. The reference is made up of four fields carat (^) delimited. Entry 1 is the reference, entry 2 is the type, entry 3 is the language, entry 4 is the page number. To add multiple master comment references for a given buyer, separate them by a pipe (|). When using AUTO_COMMENTS_OTHER, ignore the "LIST:BUYER1" parts of the field. Only add the pipe separated reference to the master comments. Ex: REF1^Type1^Lang1^Page1| REF1^Type1^Lang1^Page2| REF1^Type1^Lang1^Page1 The Type, Lang, and Page options are all optional. This is also valid. List:Buyer1:MC1 | MC2, Buyer2:MC2

### How It Works

See the description above for details on how this setting affects system behavior.

### Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | AUTO_COMMENTS_LINE_SITE |
| **Category** | Purchase Orders |
| **Owner** | Power Users |
| **Default Value** | (none) |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'AUTO_COMMENTS_LINE_SITE'
```