# QAD_INTERFACE_USER - iPurchase System Setting

**Category:** User Management

Use this setting to set the User ID for integration to QAD. This user ID will be used in QAD to create PO's. This user must be enabled in iPurchase and QAD. This user would need to be created befor...

**Common questions this answers:**
- What is QAD_INTERFACE_USER?
- What does QAD_INTERFACE_USER do?
- What is the default value for QAD_INTERFACE_USER?
- How do I configure QAD_INTERFACE_USER?

## Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | QAD_INTERFACE_USER |
| **Category** | User Management |
| **Owner** | Admin |
| **Default Value** | (none) |

## How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'QAD_INTERFACE_USER'
```
