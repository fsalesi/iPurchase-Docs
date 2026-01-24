# AUTO_CHANGE_GL - iPurchase System Setting

**Category:** Uncategorized

If your company's GL Account, Sub Account, and CC are set by having defaults at the Requisition or Requisition or Site level, then the GL information will change when you change Requisition Types. ...

**Common questions this answers:**
- What is AUTO_CHANGE_GL?
- What does AUTO_CHANGE_GL do?
- What is the default value for AUTO_CHANGE_GL?
- How do I configure AUTO_CHANGE_GL?

## Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | AUTO_CHANGE_GL |
| **Category** | Uncategorized |
| **Owner** | Power Users |
| **Default Value** | TRUE |

## How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'AUTO_CHANGE_GL'
```
