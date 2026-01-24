# USER_IMPORT_FOLDER - iPurchase System Setting

**Category:** User Management

Directory path on application server. Folder where user import files are placed for processing.

**Common questions this answers:**
- What is USER_IMPORT_FOLDER?
- What does USER_IMPORT_FOLDER do?
- What is the default value for USER_IMPORT_FOLDER?
- How do I configure USER_IMPORT_FOLDER?

## Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | USER_IMPORT_FOLDER |
| **Category** | User Management |
| **Owner** | Admin |
| **Default Value** | (none) |

## How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'USER_IMPORT_FOLDER'
```
