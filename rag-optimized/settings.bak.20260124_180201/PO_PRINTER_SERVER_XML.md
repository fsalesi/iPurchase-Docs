# PO_PRINTER_SERVER_XML - iPurchase System Setting

**Category:** Purchase Orders

This setting points iPurchase to PO printer server configuration file. ex:  or apps or test or qdt or envs or test or configs or server.xml QAD EE 2012 and above allows the ability to print fancy p...

**Common questions this answers:**
- What is PO_PRINTER_SERVER_XML?
- What does PO_PRINTER_SERVER_XML do?
- What is the default value for PO_PRINTER_SERVER_XML?
- How do I configure PO_PRINTER_SERVER_XML?

## Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | PO_PRINTER_SERVER_XML |
| **Category** | Purchase Orders |
| **Owner** | Admin |
| **Default Value** | (none) |

## How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'PO_PRINTER_SERVER_XML'
```
