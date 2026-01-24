# INQUIRY_SIMPLE_MODE - iPurchase System Setting

**Category:** Reporting & Inquiry

Comma separated list of User ID's or Group ID's who only gets to see "Views" on inquiry screen and does not see all the filter fields. This can be used as requisition security. Asterisk indicates e...

**Common questions this answers:**
- What is INQUIRY_SIMPLE_MODE?
- What does INQUIRY_SIMPLE_MODE do?
- What is the default value for INQUIRY_SIMPLE_MODE?
- How do I configure INQUIRY_SIMPLE_MODE?

## Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | INQUIRY_SIMPLE_MODE |
| **Category** | Reporting & Inquiry |
| **Owner** | Admin |
| **Default Value** | (none) |

## How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'INQUIRY_SIMPLE_MODE'
```
