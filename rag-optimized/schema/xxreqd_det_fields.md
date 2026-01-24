# xxreqd_det - Requisition Detail/Line Items Table - Fields

Stores individual line items within requisitions. Each line has quantity, cost, GL coding (account, cost center, sub-account, project), and item details.

**Common questions this answers:**
- What fields are in the xxreqd_det table?
- What fields are in the requisition line items table?
- What is xxreqd_cc (cost center)?
- What is xxreqd_total_gl?

**Related tables:** xxreq_mstr (header), GL account coding

## Fields

| Field | Type | Flags | Description |
|-------|------|:-----:|-------------|
| `xxreqd_domain` | char | i | Domain code |
| `xxreqd_nbr` | char | i | Requisition number (FK) |
| `xxreqd_line` | inte | i | Line number |
| `xxreqd_desc` | char |  | Item description |
| `xxreqd_ship_to` | char |  |  |
| `xxreqd_cost` | deci-5 |  | Unit cost |
| `xxreqd_item` | char | i |  |
| `xxreqd_qty` | deci-2 |  | Quantity |
| `xxreqd_acct` | char | i | GL account |
| `xxreqd_cc` | char | i | Cost center |
| `xxreqd_sub` | char |  | Sub-account |
| `xxreqd_project` | char |  | Project code |
| `xxreqd_char1` | char |  |  |
| `xxreqd_char2` | char |  |  |
| `xxreqd_char3` | char |  |  |
| `xxreqd_char4` | char |  |  |
| `xxreqd_char5` | char |  |  |
| `xxreqd_char6` | char |  |  |
| `xxreqd_char7` | char |  |  |
| `xxreqd_char8` | char |  |  |
| `xxreqd_char9` | char |  |  |
| `xxreqd_char10` | char |  |  |
| `xxreqd_log1` | logi |  |  |
| `xxreqd_int_notes` | char | i |  |
| `xxreqd_ext_notes` | char | i |  |
| `xxreqd_uom` | char |  |  |
| `xxreqd_u_code` | char | i |  |
| `xxreqd_u_desc` | char |  |  |
| `xxreqd_taxable` | logi |  |  |
| `xxreqd_mro_type` | char |  |  |
| `xxreqd_po_nbr` | char | i |  |
| `xxreqd_line_type` | char |  |  |
| `xxreqd_vendor` | char | i |  |
| `xxreqd_word_idx` | char | i |  |
| `xxreqd_due_date` | date |  |  |
| `xxreqd_master_comments` | char |  |  |
| `xxreqd_std_cost` | deci-2 |  |  |
| `xxreqd_ulog1` | logi |  |  |
| `xxreqd_ulog2` | logi |  |  |
| `xxreqd_ulog3` | logi |  |  |
| `xxreqd_ulog4` | logi |  |  |
| `xxreqd_ulog5` | logi |  |  |
| `xxreqd_uchar1` | char |  |  |
| `xxreqd_uchar2` | char |  |  |
| `xxreqd_uchar3` | char |  |  |
| `xxreqd_uchar4` | char |  |  |
| `xxreqd_uchar5` | char |  |  |
| `xxreqd_po_line` | inte |  |  |
| `xxreqd_approved` | logi |  |  |
| `xxreqd_app_by` | char |  |  |
| `xxreqd_app_date` | date |  |  |
| `xxreqd_app_time` | inte |  |  |
| `xxreqd_manpart` | char |  |  |
| `xxreqd_man` | char |  |  |
| `xxreqd_total` | deci-2 |  | Extended total (req currency) |
| `xxreqd_supplierauxid` | char |  |  |
| `xxreqd_wo_nbr` | char |  |  |
| `xxreqd_wo_lot` | char |  |  |
| `xxreqd_wo_op` | char |  |  |
| `xxreqd_bud_code` | char |  |  |
| `xxreqd_bud_dept` | char |  |  |
| `xxreqd_tax_cost` | deci-2 |  |  |
| `xxreqd_freight_cost` | deci-2 |  |  |
| `xxreqd_other_cost` | deci-2 |  |  |
| `xxreqd_so_nbr` | char |  |  |
| `xxreqd_so_line` | inte |  |  |
| `xxreqd_uchar6` | char |  |  |
| `xxreqd_uchar7` | char |  |  |
| `xxreqd_uchar8` | char |  |  |
| `xxreqd_uchar9` | char |  |  |
| `xxreqd_uchar10` | char |  |  |
| `xxreqd_total_gl` | deci-5 |  | Extended total (base currency) |
| `xxreqd_job` | char |  |  |
| `xxreqd_blanket_nbr` | char |  |  |
| `xxreqd_blanket_line` | inte |  |  |
| `xxreqd_perf_date` | date |  |  |
| `xxreqd_loc` | char |  |  |
| `xxreqd_line_status` | char |  |  |
| `xxreqd_punch_item` | char |  |  |
| `xxreqd_punch_desc` | char |  |  |
| `xxreqd_punch_uom` | char |  |  |
| `xxreqd_supplier_conf_date` | date |  |  |
| `xxreqd_stock_uom` | char |  |  |
| `xxreqd_stock_qty` | deci-2 |  |  |
| `xxreqd_item_rev` | char |  |  |
| `xxreqd_tax_class` | char |  |  |
| `xxreqd_tax_usage` | char |  |  |
| `xxreqd_tax_env` | char |  |  |
| `xxreqd_sup_item` | char |  |  |