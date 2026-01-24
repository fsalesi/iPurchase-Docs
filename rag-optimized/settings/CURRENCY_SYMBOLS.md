# CURRENCY_SYMBOLS - iPurchase System Setting

**Category:** Uncategorized

Comma-Separated List of Currency Codes and HTML symbol codes. For example the symbol for a Euro would be represented with the HTML code "&euro~;" Ensure to add a semi-colon before all semi-colons.

### How It Works

See the description above for details on how this setting affects system behavior.

### Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | CURRENCY_SYMBOLS |
| **Category** | Uncategorized |
| **Owner** | ISS |
| **Default Value** | US,$,USD,$,EUR,&euro;,GBP,&pound;,jpy,&yen;,YEN,&yen;,CHF,&#8355,ITL,&#8356,MXP,&#8369;,CAD, C$ |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'CURRENCY_SYMBOLS'
```