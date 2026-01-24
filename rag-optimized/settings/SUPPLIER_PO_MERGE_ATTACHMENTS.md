# SUPPLIER_PO_MERGE_ATTACHMENTS - iPurchase System Setting

**Category:** Purchase Orders

This setting is where the filename, with the full path to the pdf file or a space delimited list of pdf files that are to be merged in to the PO PDF file which is printed. If you're on windows then make sure to install pdf toolkit if not already included in the wdm or agents or 3rdParty folder. If you're on unix, then a "ghostscript" is required. Examples of value; If the file is in the agents folder the all the administrator will have to do is place the filename in the value for this setting, example "attachme.pdf". If the file is not in the agents folder then you have to put the path to the file as well. On windows an example is "d:\myfiles\attachme.pdf" On unix,  or files or attachme.pdf"

### How It Works

See the description above for valid values and usage.

### Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | SUPPLIER_PO_MERGE_ATTACHMENTS |
| **Category** | Purchase Orders |
| **Owner** | Purchasing |
| **Default Value** | (none) |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'SUPPLIER_PO_MERGE_ATTACHMENTS'
```
