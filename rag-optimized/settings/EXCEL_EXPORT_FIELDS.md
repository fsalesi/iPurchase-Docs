# EXCEL_EXPORT_FIELDS - iPurchase System Setting

**Category:** Reporting & Inquiry

This is the list of fields that will be exported from the requisition workbench.

### How It Works

This setting configures reporting & inquiry behavior in iPurchase.

### Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | EXCEL_EXPORT_FIELDS |
| **Category** | Reporting & Inquiry |
| **Owner** | IT |
| **Default Value** | xxreq_domain,xxreq_vendor,xxreq_entry_date,xxreq_nbr,xxreq_userid,xxreq_buyer,xxreq_type,xxreq_site,xxreqd_item,xxreqd_desc,xxreqd_qty,xxreqd_cost,xxreqd_po_nbr,xxreqd_po_line |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'EXCEL_EXPORT_FIELDS'
```

### Related Settings

- [EXCEL_EXPORT_ONE_TAB](EXCEL_EXPORT_ONE_TAB.md)