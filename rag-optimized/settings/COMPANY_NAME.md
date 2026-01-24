# COMPANY_NAME - iPurchase System Setting

**Category:** System Configuration

Company name displayed on reports, purchase orders, and printed documents.

### How It Works

This setting defines the company name that appears throughout the iPurchase system:
- Purchase order headers and footers
- Printed reports and documents
- Email communications
- System-generated PDFs

The value should match your organization's official legal or trading name as you want it to appear on external documents sent to suppliers.

### Valid Values

Any text string representing your company name.

**Examples:**
- `Acme Corporation`
- `ABC Manufacturing, Inc.`
- `Global Supply Co.`

### Common Questions

- How do I change the company name on purchase orders?
- Where does the company name appear in iPurchase?
- How do I update the company name displayed on reports?

### Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | COMPANY_NAME |
| **Category** | System Configuration |
| **Owner** | Admin |
| **Default Value** | (none) |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'COMPANY_NAME'
```
