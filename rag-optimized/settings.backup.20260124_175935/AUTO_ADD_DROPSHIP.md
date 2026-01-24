# AUTO_ADD_DROPSHIP - iPurchase System Setting

**Category:** Uncategorized

True or False - Default FALSE. Automatically adds "Dropship" as an option in the Ship To dropdown field in Requisition Workbench

**Common questions this answers:**
- What is AUTO_ADD_DROPSHIP?
- What does AUTO_ADD_DROPSHIP do?
- What is the default value for AUTO_ADD_DROPSHIP?
- How do I configure AUTO_ADD_DROPSHIP?

## Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | AUTO_ADD_DROPSHIP |
| **Category** | Uncategorized |
| **Owner** | Admin |
| **Default Value** | FALSE |

## How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'AUTO_ADD_DROPSHIP'
```
