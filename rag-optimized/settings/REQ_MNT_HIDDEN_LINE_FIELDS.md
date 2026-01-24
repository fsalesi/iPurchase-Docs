# REQ_MNT_HIDDEN_LINE_FIELDS - iPurchase System Setting

**Category:** Requisitions

These are the list of fields that are hidden at the line level. These should not be changed unless you want to hide other line fields.

### How It Works

See the description above for details on how this setting affects system behavior.

### Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | REQ_MNT_HIDDEN_LINE_FIELDS |
| **Category** | Requisitions |
| **Owner** | Power Users |
| **Default Value** | h_line_xxreqd_tax_usage,h_line_xxreqd_tax_class,h_line_xxreqd_tax_env,h_xxreqd_uchar1,h_xxreqd_uchar2,h_xxreqd_uchar3,h_xxreqd_uchar4,h_xxreqd_uchar5,h_xxreqd_uchar6,h_xxreqd_uchar7,h_xxreqd_uchar8,h_xxreqd_uchar9,h_xxreqd_uchar10,h_xxreqd_ulog1,h_xxreqd_ulog2,h_xxreqd_ulog3,h_xxreqd_ulog4,h_xxreqd_ulog5,h_line_project,h_line_tool_id,h_line_ar,h_line_vendor,h_line_vendor_name,h_line_mro_type,h_line_po_nbr,h_line_perf_date,h_line_freight_cost,h_line_other_cost |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'REQ_MNT_HIDDEN_LINE_FIELDS'
```