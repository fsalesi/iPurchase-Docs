# AUTO_COMMENTS_CO - iPurchase System Setting

**Category:** Purchase Orders

Use this setting to automatically attach comments to every Purchase Order REVISION - CHANGE ORDER. This is a pointer to the code_mstr field name (code_fldname) value to be used. Example: List:Buyer...

**Common questions this answers:**
- What is AUTO_COMMENTS_CO?
- What does AUTO_COMMENTS_CO do?
- What is the default value for AUTO_COMMENTS_CO?
- How do I configure AUTO_COMMENTS_CO?

## Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | AUTO_COMMENTS_CO |
| **Category** | Purchase Orders |
| **Owner** | Power Users |
| **Default Value** | (none) |

## How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'AUTO_COMMENTS_CO'
```
