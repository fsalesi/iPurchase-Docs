# xxreq_mstr - Requisition Header Table - Fields

The main requisition table containing header-level information: status, dates, totals, vendor, buyer, and workflow state. Every requisition has one record here. Primary key is domain + requisition number.

**Common questions this answers:**
- What fields are in the xxreq_mstr table?
- What fields are in the requisition header table?
- What is xxreq_obo (on behalf of)?
- What is xxreq_status?

**Related tables:** xxreqd_det (line items), xxreq_audit (approvals), xxreq_attach (attachments)

### Fields

| Field | Type | Flags | Description |
|-------|------|:-----:|-------------|
| `xxreq_nbr` | char | i | Requisition number |
| `xxreq_date` | date | i | Need-by date |
| `xxreq_status` | char | i | Status: blank=draft, CONFIRMED=submitted, APPROVED=approved |
| `xxreq_submit_attempts` | inte |  |  |
| `xxreq_sort_field1` | char | i |  |
| `xxreq_sort_field2` | char | i |  |
| `xxreq_sort_field3` | char | i |  |
| `xxreq_sort_field4` | char | i |  |
| `xxreq_sort_field5` | char | i |  |
| `xxreq_sort_field6` | char | i |  |
| `xxreq_sort_field7` | char | i |  |
| `xxreq_sort_field8` | char |  |  |
| `xxreq_sort_field9` | char | i |  |
| `xxreq_sort_field10` | char | i |  |
| `xxreq_userid` | char | i | Creator user ID (person at keyboard) |
| `xxreq_domain` | char | i | Domain/company code |
| `xxreq_date1` | date |  |  |
| `xxreq_date2` | date |  |  |
| `xxreq_date3` | date |  |  |
| `xxreq_date4` | date |  |  |
| `xxreq_date5` | date |  |  |
| `xxreq_dec1` | deci-2 |  |  |
| `xxreq_dec2` | deci-2 |  |  |
| `xxreq_dec3` | deci-2 |  |  |
| `xxreq_dec4` | deci-2 |  |  |
| `xxreq_dec5` | deci-2 |  |  |
| `xxreq_log1` | logi |  |  |
| `xxreq_log2` | logi |  |  |
| `xxreq_log3` | logi |  |  |
| `xxreq_log4` | logi |  |  |
| `xxreq_log5` | logi |  |  |
| `xxreq_vendor` | char | i | Vendor code |
| `xxreq_need_date` | date |  |  |
| `xxreq_entry_date` | date |  | Creation date |
| `xxreq_submit_date` | date |  |  |
| `xxreq_approved` | logi | i |  |
| `xxreq_app_by` | char |  |  |
| `xxreq_po_nbr` | char | i |  |
| `xxreq_ship_via` | char |  |  |
| `xxreq_freight_terms` | char |  |  |
| `xxreq_ship_to` | char |  |  |
| `xxreq_char1` | char |  |  |
| `xxreq_char2` | char |  |  |
| `xxreq_char3` | char |  |  |
| `xxreq_char4` | char |  |  |
| `xxreq_char5` | char |  |  |
| `xxreq_char6` | char |  |  |
| `xxreq_char7` | char |  |  |
| `xxreq_char8` | char |  |  |
| `xxreq_char9` | char |  |  |
| `xxreq_char10` | char |  |  |
| `xxreq_submitted` | logi | i |  |
| `xxreq_type` | char | i | Requisition type |
| `xxreq_int_notes` | char | i |  |
| `xxreq_ext_notes` | char | i |  |
| `xxreq_app_date` | date |  | Approval date |
| `xxreq_app_time` | inte |  | Approval time (seconds) |
| `xxreq_bill_to` | char |  |  |
| `xxreq_word_idx` | char | i |  |
| `xxreq_word_idx2` | char | i |  |
| `xxreq_word_idx3` | char | i |  |
| `xxreq_cost` | deci-2 | i | Total in req currency |
| `xxreq_obo` | char |  | On Behalf Of (budget owner) |
| `xxreq_deliver_to` | char |  |  |
| `xxreq_project` | char |  |  |
| `xxreq_taxable` | logi |  |  |
| `xxreq_po_required` | logi |  |  |
| `xxreq_site` | char |  |  |
| `xxreq_master_comments` | char |  |  |
| `xxreq_ulog1` | logi |  |  |
| `xxreq_ulog2` | logi |  |  |
| `xxreq_ulog3` | logi |  |  |
| `xxreq_ulog4` | logi |  |  |
| `xxreq_ulog5` | logi |  |  |
| `xxreq_uchar1` | char |  |  |
| `xxreq_uchar2` | char |  |  |
| `xxreq_uchar3` | char |  |  |
| `xxreq_uchar4` | char |  |  |
| `xxreq_uchar5` | char |  |  |
| `xxreq_buyer` | char | i | Assigned buyer |
| `xxreq_submit_total` | deci-2 |  | Total at submission |
| `xxreq_currency` | char |  |  |
| `xxreq_copied_from` | char | i | Source req (for copies/COs) |
| `xxreq_update_po` | logi |  | TRUE = change order |
| `xxreq_update_po_tolerance` | logi |  |  |
| `xxreq_dropship` | char |  |  |
| `xxreq_confirm_email` | char |  |  |
| `xxreq_confirm_date` | date |  |  |
| `xxreq_confirm_time` | inte |  |  |
| `xxreq_all_items` | logi |  |  |
| `xxreq_supplier_contact` | char |  |  |
| `xxreq_supplier_phone` | char |  |  |
| `xxreq_supplier_fax` | char |  |  |
| `xxreq_supplier_email` | char |  |  |
| `xxreq_po_sent` | logi |  |  |
| `xxreq_po_sent_by` | char |  |  |
| `xxreq_po_sent_datetime` | datetm |  |  |
| `xxreq_rfq` | logi |  |  |
| `xxreq_hold` | logi |  |  |
| `xxreq_hold_user` | char |  |  |
| `xxreq_hold_date` | datetm-tz |  |  |
| `xxreq_full_catalog` | logi |  |  |
| `xxreq_cartid` | inte | i |  |
| `xxreq_hold_comment` | char |  |  |
| `xxreq_confirm_nbr` | char |  |  |
| `xxreq_po_sent_to` | char |  |  |
| `xxreq_cost_gl` | deci-5 |  | Total in base currency (for approvals) |
| `xxreq_cons` | logi |  |  |
| `xxreq_cons_nbr` | char | i |  |
| `xxreq_blanket` | logi |  |  |
| `xxreq_blanket_nbr` | char | i |  |
| `xxreq_blanket_start` | date |  |  |
| `xxreq_blanket_end` | date |  |  |
| `xxreq_blanket_est` | deci-2 |  |  |
| `xxreq_blanket_recurr` | logi |  |  |
| `xxreq_blanket_cycle` | char |  |  |
| `xxreq_no_archive` | logi |  |  |
| `xxreq_perf_date` | date |  |  |
| `xxreq_mat_change` | logi |  | TRUE = material change (re-route) |
| `xxreq_cr_terms` | char |  |  |
| `xxreq_supplier_comments` | char |  |  |