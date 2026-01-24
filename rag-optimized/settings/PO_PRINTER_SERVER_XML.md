# PO_PRINTER_SERVER_XML - iPurchase System Setting

**Category:** Purchase Orders

This setting points iPurchase to PO printer server configuration file. ex:  or apps or test or qdt or envs or test or configs or server.xml QAD EE 2012 and above allows the ability to print fancy purchase orders. Requirements: Names QAD user. Settings QAD_AUTHENTICATION_USER and QAD_AUTHENTICATION_PASSWORD must be set. The user specified in QAD_AUTHENTICATION_USER must be setup in QAD with a role of "rptAdmin"

### How It Works

See the description above for details on how this setting affects system behavior.

### Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | PO_PRINTER_SERVER_XML |
| **Category** | Purchase Orders |
| **Owner** | Admin |
| **Default Value** | (none) |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'PO_PRINTER_SERVER_XML'
```