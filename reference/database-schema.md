# iPurchase Database Schema Reference

This document contains the schema definitions for tables documented in the iPurchase admin screens.

**Database:** wdm (PROGRESS/OpenEdge)

---

## Table of Contents

### Core Tables
- [wus_mstr](#wus-mstr)
- [wgr_mstr](#wgr-mstr)
- [wugr_mstr](#wugr-mstr)
- [pf_mstr](#pf-mstr)

### Requisition Tables
- [xxreq_mstr](#xxreq-mstr)
- [xxreqd_det](#xxreqd-det)
- [xxreq_audit](#xxreq-audit)
- [xxreq_attach](#xxreq-attach)

### Approval Tables
- [xxapp_mstr](#xxapp-mstr)
- [xxAppRule](#xxapprule)
- [xxAppField](#xxappfield)

### Archive & Attachment Tables
- [xxpo_archive](#xxpo-archive)
- [xxnote_mstr](#xxnote-mstr)
- [xxmaild_det](#xxmaild-det)

### Location & Configuration Tables
- [xxloc_mstr](#xxloc-mstr)
- [xxrole_mstr](#xxrole-mstr)
- [xxlang_mstr](#xxlang-mstr)
- [xxlangd_det](#xxlangd-det)
- [xxmail_mstr](#xxmail-mstr)
- [xxlink_mstr](#xxlink-mstr)
- [xxshipd_det](#xxshipd-det)

### System Tables
- [appsrv_mstr](#appsrv-mstr)
- [efw_audit](#efw-audit)
- [iaach_mstr](#iaach-mstr)
- [iaqt_mstr](#iaqt-mstr)

---

## Core Tables

### wus_mstr

**Description:** Standard user master table.  Name, address, e-mail, etc.

#### Fields

| Order | Field Name | Data Type | Flags |
|-------|------------|-----------|-------|
| 10 | `wus_id` | char | im |
| 20 | `wus_name` | char | i |
| 30 | `wus_title` | char |  |
| 40 | `wus_company` | char | i |
| 60 | `wus_city` | char |  |
| 70 | `wus_state` | char |  |
| 80 | `wus_country` | char |  |
| 90 | `wus_post` | char |  |
| 100 | `wus_phone` | char |  |
| 110 | `wus_fax` | char |  |
| 120 | `wus_email` | char |  |
| 130 | `wus_type` | char | i |
| 140 | `wus_create_date` | date |  |
| 150 | `wus_create_by` | char |  |
| 160 | `wus_disable` | logi | i |
| 170 | `wus_expire_date` | date |  |
| 180 | `wus_password` | char |  |
| 190 | `wus_street1` | char |  |
| 200 | `wus_street2` | char |  |
| 210 | `wus_failed_logins` | inte |  |
| 220 | `wus_delegate` | char | i |
| 230 | `wus_erp_id` | char |  |
| 240 | `wus_erp_initials` | char | i |
| 250 | `wus_app_amt` | deci-2 |  |
| 260 | `wus_supervisor` | char | i |
| 270 | `wus_domains` | char |  |
| 280 | `wus_last_login` | date |  |
| 290 | `wus_carrier` | char |  |
| 300 | `wus_mobile` | logi |  |
| 310 | `wus_groups` | char | i |

#### Indexes

| Flags | Index Name | Fields |
|-------|------------|--------|
|  | `by_wus_company` | wus_company |
| pu | `by_wus_id` | wus_id |
|  | `by_wus_name` | wus_name |
|  | `by_wus_type` | wus_type |
|  | `wus_delegate` | wus_delegate |
|  | `wus_disable` | wus_disable |
|  | `wus_supervisor` | wus_supervisor |

---

### wgr_mstr

**Description:** Stores group level data.

#### Fields

| Order | Field Name | Data Type | Flags |
|-------|------------|-----------|-------|
| 10 | `wgr_id` | char | im |
| 20 | `wgr_name` | char | i |
| 30 | `wgr_desc` | char |  |
| 40 | `wgr_mgr` | char |  |
| 50 | `wgr_level` | char |  |
| 60 | `wgr_create_date` | date |  |
| 70 | `wgr_create_by` | char |  |
| 80 | `wgr_disable` | logi |  |
| 90 | `wgr_expire_date` | date |  |
| 100 | `wgr_type` | char | i |

#### Indexes

| Flags | Index Name | Fields |
|-------|------------|--------|
| pu | `by_wgr_id` | wgr_id |
|  | `by_wgr_name` | wgr_name |
|  | `by_wgr_type` | wgr_type |

---

### wugr_mstr

**Description:** Stores user-defined relationships between users and groups.                Which users belong to which groups?

#### Fields

| Order | Field Name | Data Type | Flags |
|-------|------------|-----------|-------|
| 10 | `wugr_gr_id` | char | im |
| 20 | `wugr_us_id` | char | im |
| 30 | `wugr_create_date` | date |  |
| 40 | `wugr_create_by` | char |  |
| 50 | `wugr_disable` | logi |  |
| 60 | `wugr_expire_date` | date |  |

#### Indexes

| Flags | Index Name | Fields |
|-------|------------|--------|
| pu | `by_wugr_id` | wugr_gr_id, wugr_us_id |
|  | `by_wugr_us_id` | wugr_us_id, wugr_gr_id |

---

### pf_mstr

**Description:** General purpose data driven application configuration                information.

#### Fields

| Order | Field Name | Data Type | Flags |
|-------|------------|-----------|-------|
| 10 | `pf_us_id` | char | im |
| 20 | `pf_attr` | char | im |
| 30 | `pf_value` | char | i |
| 40 | `pf_alt_value` | char | i |
| 50 | `pf_date1` | date |  |
| 60 | `pf_date2` | date |  |
| 70 | `pf_log1` | logi |  |
| 80 | `pf_log2` | logi |  |
| 90 | `pf_dec1` | deci-2 |  |
| 100 | `pf_dec2` | deci-2 |  |
| 110 | `pf_group` | char | i |
| 120 | `pf_seq` | deci-3 | i |
| 130 | `pf_chr1` | char |  |
| 140 | `pf_chr2` | char |  |
| 150 | `pf_data_version` | deci-2 |  |
| 160 | `pf_default` | char |  |
| 170 | `pf_help` | char |  |
| 180 | `pf_notes` | char |  |

#### Indexes

| Flags | Index Name | Fields |
|-------|------------|--------|
| p | `Main` | pf_us_id, pf_group, pf_attr, pf_value, pf_alt_value, pf_seq |

---

## Requisition Tables

### xxreq_mstr

#### Fields

| Order | Field Name | Data Type | Flags |
|-------|------------|-----------|-------|
| 10 | `xxreq_nbr` | char | i |
| 20 | `xxreq_date` | date | i |
| 30 | `xxreq_status` | char | i |
| 40 | `xxreq_submit_attempts` | inte |  |
| 50 | `xxreq_sort_field1` | char | i |
| 60 | `xxreq_sort_field2` | char | i |
| 70 | `xxreq_sort_field3` | char | i |
| 80 | `xxreq_sort_field4` | char | i |
| 90 | `xxreq_sort_field5` | char | i |
| 100 | `xxreq_sort_field6` | char | i |
| 110 | `xxreq_sort_field7` | char | i |
| 120 | `xxreq_sort_field8` | char |  |
| 130 | `xxreq_sort_field9` | char | i |
| 140 | `xxreq_sort_field10` | char | i |
| 150 | `xxreq_userid` | char | i |
| 160 | `xxreq_domain` | char | i |
| 170 | `xxreq_date1` | date |  |
| 180 | `xxreq_date2` | date |  |
| 190 | `xxreq_date3` | date |  |
| 200 | `xxreq_date4` | date |  |
| 210 | `xxreq_date5` | date |  |
| 220 | `xxreq_dec1` | deci-2 |  |
| 230 | `xxreq_dec2` | deci-2 |  |
| 240 | `xxreq_dec3` | deci-2 |  |
| 250 | `xxreq_dec4` | deci-2 |  |
| 260 | `xxreq_dec5` | deci-2 |  |
| 270 | `xxreq_log1` | logi |  |
| 280 | `xxreq_log2` | logi |  |
| 290 | `xxreq_log3` | logi |  |
| 300 | `xxreq_log4` | logi |  |
| 310 | `xxreq_log5` | logi |  |
| 320 | `xxreq_vendor` | char | i |
| 330 | `xxreq_need_date` | date |  |
| 340 | `xxreq_entry_date` | date |  |
| 350 | `xxreq_submit_date` | date |  |
| 360 | `xxreq_approved` | logi | i |
| 370 | `xxreq_app_by` | char |  |
| 380 | `xxreq_po_nbr` | char | i |
| 390 | `xxreq_ship_via` | char |  |
| 400 | `xxreq_freight_terms` | char |  |
| 410 | `xxreq_ship_to` | char |  |
| 420 | `xxreq_char1` | char |  |
| 430 | `xxreq_char2` | char |  |
| 440 | `xxreq_char3` | char |  |
| 450 | `xxreq_char4` | char |  |
| 460 | `xxreq_char5` | char |  |
| 470 | `xxreq_char6` | char |  |
| 480 | `xxreq_char7` | char |  |
| 490 | `xxreq_char8` | char |  |
| 500 | `xxreq_char9` | char |  |
| 510 | `xxreq_char10` | char |  |
| 520 | `xxreq_submitted` | logi | i |
| 530 | `xxreq_type` | char | i |
| 540 | `xxreq_int_notes` | char | i |
| 550 | `xxreq_ext_notes` | char | i |
| 560 | `xxreq_app_date` | date |  |
| 570 | `xxreq_app_time` | inte |  |
| 580 | `xxreq_bill_to` | char |  |
| 590 | `xxreq_word_idx` | char | i |
| 600 | `xxreq_word_idx2` | char | i |
| 610 | `xxreq_word_idx3` | char | i |
| 620 | `xxreq_cost` | deci-2 | i |
| 630 | `xxreq_obo` | char |  |
| 640 | `xxreq_deliver_to` | char |  |
| 650 | `xxreq_project` | char |  |
| 660 | `xxreq_taxable` | logi |  |
| 670 | `xxreq_po_required` | logi |  |
| 680 | `xxreq_site` | char |  |
| 690 | `xxreq_master_comments` | char |  |
| 700 | `xxreq_ulog1` | logi |  |
| 710 | `xxreq_ulog2` | logi |  |
| 720 | `xxreq_ulog3` | logi |  |
| 730 | `xxreq_ulog4` | logi |  |
| 740 | `xxreq_ulog5` | logi |  |
| 750 | `xxreq_uchar1` | char |  |
| 760 | `xxreq_uchar2` | char |  |
| 770 | `xxreq_uchar3` | char |  |
| 780 | `xxreq_uchar4` | char |  |
| 790 | `xxreq_uchar5` | char |  |
| 800 | `xxreq_buyer` | char | i |
| 810 | `xxreq_submit_total` | deci-2 |  |
| 820 | `xxreq_currency` | char |  |
| 830 | `xxreq_copied_from` | char | i |
| 840 | `xxreq_update_po` | logi |  |
| 850 | `xxreq_update_po_tolerance` | logi |  |
| 860 | `xxreq_dropship` | char |  |
| 870 | `xxreq_confirm_email` | char |  |
| 880 | `xxreq_confirm_date` | date |  |
| 890 | `xxreq_confirm_time` | inte |  |
| 900 | `xxreq_all_items` | logi |  |
| 910 | `xxreq_supplier_contact` | char |  |
| 920 | `xxreq_supplier_phone` | char |  |
| 930 | `xxreq_supplier_fax` | char |  |
| 940 | `xxreq_supplier_email` | char |  |
| 950 | `xxreq_po_sent` | logi |  |
| 960 | `xxreq_po_sent_by` | char |  |
| 970 | `xxreq_po_sent_datetime` | datetm |  |
| 980 | `xxreq_rfq` | logi |  |
| 990 | `xxreq_hold` | logi |  |
| 1000 | `xxreq_hold_user` | char |  |
| 1010 | `xxreq_hold_date` | datetm-tz |  |
| 1020 | `xxreq_full_catalog` | logi |  |
| 1030 | `xxreq_cartid` | inte | i |
| 1040 | `xxreq_hold_comment` | char |  |
| 1050 | `xxreq_confirm_nbr` | char |  |
| 1060 | `xxreq_po_sent_to` | char |  |
| 1070 | `xxreq_cost_gl` | deci-5 |  |
| 1080 | `xxreq_cons` | logi |  |
| 1090 | `xxreq_cons_nbr` | char | i |
| 1100 | `xxreq_blanket` | logi |  |
| 1110 | `xxreq_blanket_nbr` | char | i |
| 1120 | `xxreq_blanket_start` | date |  |
| 1130 | `xxreq_blanket_end` | date |  |
| 1140 | `xxreq_blanket_est` | deci-2 |  |
| 1150 | `xxreq_blanket_recurr` | logi |  |
| 1160 | `xxreq_blanket_cycle` | char |  |
| 1170 | `xxreq_no_archive` | logi |  |
| 1180 | `xxreq_perf_date` | date |  |
| 1190 | `xxreq_mat_change` | logi |  |
| 1200 | `xxreq_cr_terms` | char |  |
| 1210 | `xxreq_supplier_comments` | char |  |

#### Indexes

| Flags | Index Name | Fields |
|-------|------------|--------|
|  | `byblanket` | xxreq_blanket_nbr |
|  | `byconsnbr` | xxreq_cons_nbr |
|  | `cart_id` | xxreq_cartid |
|  | `entry_date` | xxreq_date |
|  | `field1` | xxreq_sort_field1 |
|  | `field10` | xxreq_sort_field10 |
|  | `field2` | xxreq_sort_field2 |
|  | `field3` | xxreq_sort_field3 |
|  | `field4` | xxreq_sort_field4 |
|  | `field5` | xxreq_sort_field5 |
|  | `field6` | xxreq_sort_field6 |
|  | `field7` | xxreq_sort_field7 |
|  | `field8` | xxreq_sort_field9 |
|  | `field9` | xxreq_sort_field9 |
| p | `nbr` | xxreq_nbr |
|  | `req-userid` | xxreq_userid |
|  | `req_stat` | xxreq_status |
|  | `submittedidx` | xxreq_submitted |
|  | `typeidx` | xxreq_type |
|  | `vend` | xxreq_vendor |
|  | `xxdomain` | xxreq_domain |
|  | `xxreq_buyer` | xxreq_buyer |
|  | `xxreq_copied_from` | xxreq_domain, xxreq_copied_from |
|  | `xxreq_cost` | xxreq_cost |
|  | `xxreq_po_nbr` | xxreq_domain, xxreq_po_nbr |

---

### xxreqd_det

**Description:** Catalog "C", Punchout "P", Other - blank

#### Fields

| Order | Field Name | Data Type | Flags |
|-------|------------|-----------|-------|
| 10 | `xxreqd_domain` | char | i |
| 20 | `xxreqd_nbr` | char | i |
| 30 | `xxreqd_line` | inte | i |
| 40 | `xxreqd_desc` | char |  |
| 50 | `xxreqd_ship_to` | char |  |
| 60 | `xxreqd_cost` | deci-5 |  |
| 70 | `xxreqd_item` | char | i |
| 80 | `xxreqd_qty` | deci-2 |  |
| 100 | `xxreqd_acct` | char | i |
| 110 | `xxreqd_cc` | char | i |
| 120 | `xxreqd_sub` | char |  |
| 130 | `xxreqd_project` | char |  |
| 140 | `xxreqd_char1` | char |  |
| 150 | `xxreqd_char2` | char |  |
| 160 | `xxreqd_char3` | char |  |
| 170 | `xxreqd_char4` | char |  |
| 180 | `xxreqd_char5` | char |  |
| 190 | `xxreqd_char6` | char |  |
| 200 | `xxreqd_char7` | char |  |
| 210 | `xxreqd_char8` | char |  |
| 220 | `xxreqd_char9` | char |  |
| 230 | `xxreqd_char10` | char |  |
| 240 | `xxreqd_log1` | logi |  |
| 250 | `xxreqd_int_notes` | char | i |
| 260 | `xxreqd_ext_notes` | char | i |
| 270 | `xxreqd_uom` | char |  |
| 280 | `xxreqd_u_code` | char | i |
| 290 | `xxreqd_u_desc` | char |  |
| 300 | `xxreqd_taxable` | logi |  |
| 310 | `xxreqd_mro_type` | char |  |
| 320 | `xxreqd_po_nbr` | char | i |
| 330 | `xxreqd_line_type` | char |  |
| 340 | `xxreqd_vendor` | char | i |
| 350 | `xxreqd_word_idx` | char | i |
| 360 | `xxreqd_due_date` | date |  |
| 370 | `xxreqd_master_comments` | char |  |
| 380 | `xxreqd_std_cost` | deci-2 |  |
| 390 | `xxreqd_ulog1` | logi |  |
| 400 | `xxreqd_ulog2` | logi |  |
| 410 | `xxreqd_ulog3` | logi |  |
| 420 | `xxreqd_ulog4` | logi |  |
| 430 | `xxreqd_ulog5` | logi |  |
| 440 | `xxreqd_uchar1` | char |  |
| 450 | `xxreqd_uchar2` | char |  |
| 460 | `xxreqd_uchar3` | char |  |
| 470 | `xxreqd_uchar4` | char |  |
| 480 | `xxreqd_uchar5` | char |  |
| 490 | `xxreqd_po_line` | inte |  |
| 500 | `xxreqd_approved` | logi |  |
| 510 | `xxreqd_app_by` | char |  |
| 520 | `xxreqd_app_date` | date |  |
| 530 | `xxreqd_app_time` | inte |  |
| 540 | `xxreqd_manpart` | char |  |
| 550 | `xxreqd_man` | char |  |
| 560 | `xxreqd_total` | deci-2 |  |
| 570 | `xxreqd_supplierauxid` | char |  |
| 580 | `xxreqd_wo_nbr` | char |  |
| 590 | `xxreqd_wo_lot` | char |  |
| 600 | `xxreqd_wo_op` | char |  |
| 610 | `xxreqd_bud_code` | char |  |
| 620 | `xxreqd_bud_dept` | char |  |
| 630 | `xxreqd_tax_cost` | deci-2 |  |
| 640 | `xxreqd_freight_cost` | deci-2 |  |
| 650 | `xxreqd_other_cost` | deci-2 |  |
| 660 | `xxreqd_so_nbr` | char |  |
| 670 | `xxreqd_so_line` | inte |  |
| 680 | `xxreqd_uchar6` | char |  |
| 690 | `xxreqd_uchar7` | char |  |
| 700 | `xxreqd_uchar8` | char |  |
| 710 | `xxreqd_uchar9` | char |  |
| 720 | `xxreqd_uchar10` | char |  |
| 730 | `xxreqd_total_gl` | deci-5 |  |
| 740 | `xxreqd_job` | char |  |
| 750 | `xxreqd_blanket_nbr` | char |  |
| 760 | `xxreqd_blanket_line` | inte |  |
| 770 | `xxreqd_perf_date` | date |  |
| 780 | `xxreqd_loc` | char |  |
| 790 | `xxreqd_line_status` | char |  |
| 800 | `xxreqd_punch_item` | char |  |
| 810 | `xxreqd_punch_desc` | char |  |
| 820 | `xxreqd_punch_uom` | char |  |
| 830 | `xxreqd_supplier_conf_date` | date |  |
| 840 | `xxreqd_stock_uom` | char |  |
| 850 | `xxreqd_stock_qty` | deci-2 |  |
| 860 | `xxreqd_item_rev` | char |  |
| 870 | `xxreqd_tax_class` | char |  |
| 880 | `xxreqd_tax_usage` | char |  |
| 890 | `xxreqd_tax_env` | char |  |
| 900 | `xxreqd_sup_item` | char |  |

#### Indexes

| Flags | Index Name | Fields |
|-------|------------|--------|
|  | `cc` | xxreqd_cc |
|  | `item` | xxreqd_item |
|  | `po` | xxreqd_domain, xxreqd_po_nbr |
| pu | `pri` | xxreqd_domain, xxreqd_nbr, xxreqd_line |
|  | `vendor` | xxreqd_domain, xxreqd_vendor |
|  | `xxreqd_u_code` | xxreqd_u_code |

---

### xxreq_audit

#### Fields

| Order | Field Name | Data Type | Flags |
|-------|------------|-----------|-------|
| 10 | `xxreq_nbr` | char | i |
| 20 | `xxreq_submit_date` | date |  |
| 30 | `xxreq_submit_time` | inte |  |
| 40 | `xxreq_submit_attempt` | inte | i |
| 50 | `xxreq_app_id` | char | i |
| 60 | `xxreq_decom_app_id` | char | i |
| 70 | `xxreq_app_seq` | deci-2 |  |
| 80 | `xxreq_last_notified_date` | date |  |
| 90 | `xxreq_last_notified_time` | inte |  |
| 110 | `xxreq_actual_approver` | char |  |
| 120 | `xxreq_app_date` | date |  |
| 130 | `xxreq_app_time` | inte |  |
| 140 | `xxreq_app_notes` | char |  |
| 150 | `xxreq_status` | char |  |
| 160 | `xxreq_unique` | inte | i |
| 170 | `xxreq_domain` | char | i |
| 180 | `xxreq_active` | logi |  |
| 190 | `xxreq_last_set` | logi |  |
| 200 | `xxreq_auditm_seq` | inte |  |
| 210 | `xxreq_active_date` | date | i |
| 220 | `xxreq_active_time` | inte | i |
| 230 | `xxreq_reject_code` | char | i |
| 240 | `xxreq_date1` | date |  |
| 250 | `xxreq_date2` | date |  |
| 260 | `xxreq_dec1` | deci-2 |  |
| 270 | `xxreq_dec2` | deci-2 |  |
| 280 | `xxreq_ulog1` | logi |  |
| 290 | `xxreq_ulog2` | logi |  |
| 300 | `xxreq_uchar1` | char |  |
| 310 | `xxreq_uchar2` | char |  |

#### Indexes

| Flags | Index Name | Fields |
|-------|------------|--------|
|  | `approver` | xxreq_domain, xxreq_nbr, xxreq_submit_attempt, xxreq_app_id |
| pu | `pri` | xxreq_unique |
|  | `xxreq_reject_code` | xxreq_reject_code |

---

### xxreq_attach

#### Fields

| Order | Field Name | Data Type | Flags |
|-------|------------|-----------|-------|
| 10 | `xxreq_domain` | char | i |
| 20 | `xxreq_nbr` | char | i |
| 30 | `xxreq_filename` | char | i |
| 40 | `xxreq_line` | inte | i |
| 50 | `xxreq_os_filename` | char |  |
| 60 | `xxreq_int_ext` | logi |  |
| 70 | `xxreq_security` | char |  |
| 80 | `xxreq_file` | blob |  |
| 90 | `xxreq_user` | char |  |
| 100 | `xxreq_date` | datetm-tz |  |

#### Indexes

| Flags | Index Name | Fields |
|-------|------------|--------|
| pu | `pri` | xxreq_domain, xxreq_nbr, xxreq_line, xxreq_filename |

---

## Approval Tables

### xxapp_mstr

#### Fields

| Order | Field Name | Data Type | Flags |
|-------|------------|-----------|-------|
| 20 | `xxapp_type` | char | i |
| 30 | `xxapp_po_site` | char | i |
| 40 | `xxapp_cc` | char | i |
| 50 | `xxapp_amount` | deci-2 | i |
| 60 | `xxapp_id` | char | i |
| 80 | `xxapp_seq` | inte | i |
| 90 | `xxapp_domain` | char | i |
| 100 | `xxapp_acct` | char | i |
| 110 | `xxapp_sub` | char | i |
| 120 | `xxapp_project` | char | i |
| 130 | `oid_xxapp_mstr` | deci-2 | i |
| 140 | `xxapp_has_notes` | logi |  |
| 150 | `xxapp_has_attachments` | logi |  |
| 160 | `xxapp_max_amount` | deci-2 | i |
| 170 | `xxapp_description` | char | i |
| 180 | `xxapp_active` | logi | i |
| 190 | `xxapp_orig` | char |  |
| 200 | `xxapp_notify` | logi | i |
| 210 | `xxapp_line_site` | char |  |
| 220 | `xxapp_stop` | logi |  |
| 230 | `xxapp_which_cost` | char |  |
| 240 | `xxapp_unspsc` | char | i |

#### Indexes

| Flags | Index Name | Fields |
|-------|------------|--------|
|  | `byactive` | xxapp_active |
|  | `bydept` | xxapp_cc |
|  | `bydesc` | xxapp_description |
|  | `bydomain` | xxapp_domain |
|  | `byid` | xxapp_id |
|  | `bymax` | xxapp_max_amount |
|  | `bymin` | xxapp_amount |
|  | `bynotify` | xxapp_notify |
|  | `byproj` | xxapp_project |
|  | `byseq` | xxapp_seq |
|  | `bysite` | xxapp_po_site |
|  | `bysub` | xxapp_sub |
|  | `bytype` | xxapp_type |
|  | `byunspsc` | xxapp_unspsc |
| pu | `oid` | oid_xxapp_mstr |

---

### xxAppRule

#### Fields

| Order | Field Name | Data Type | Flags |
|-------|------------|-----------|-------|
| 10 | `xxAR_Domain` | char | i |
| 20 | `xxAR_RuleName` | char | i |
| 30 | `xxAR_AppLevel` | deci-2 |  |
| 40 | `xxAR_Approver` | char |  |
| 50 | `xxAR_AmtType` | char |  |
| 60 | `xxAR_MinAmt` | deci-2 |  |
| 70 | `xxAR_MaxAmt` | deci-2 |  |
| 80 | `xxAR_Active` | logi |  |
| 90 | `xxAR_stop` | logi |  |
| 100 | `xxAR_Eval_Lines` | logi |  |
| 110 | `xxAR_notify` | logi |  |

#### Indexes

| Flags | Index Name | Fields |
|-------|------------|--------|
| pu | `pri` | xxAR_Domain, xxAR_RuleName |

---

### xxAppField

#### Fields

| Order | Field Name | Data Type | Flags |
|-------|------------|-----------|-------|
| 10 | `xxAF_Domain` | char | i |
| 20 | `xxAF_RuleName` | char | i |
| 30 | `xxAF_Seq` | inte | i |
| 40 | `xxAF_Table` | char |  |
| 50 | `xxAF_Field` | char |  |
| 60 | `xxAF_Value` | char |  |
| 70 | `xxAF_Operand` | char |  |
| 80 | `xxAF_Group` | inte |  |
| 90 | `xxAF_Parent` | inte |  |

#### Indexes

| Flags | Index Name | Fields |
|-------|------------|--------|
| p | `pri` | xxAF_Domain, xxAF_RuleName, xxAF_Seq |

---

## Archive & Attachment Tables

### xxpo_archive

#### Fields

| Order | Field Name | Data Type | Flags |
|-------|------------|-----------|-------|
| 10 | `xxpoa_domain` | char | i |
| 20 | `xxpoa_nbr` | char | i |
| 30 | `xxpoa_datetime` | datetm-tz |  |
| 40 | `xxpoa_user` | char |  |
| 50 | `xxpoa_rev` | deci-2 | i |
| 60 | `xxpoa_pdf` | blob |  |
| 70 | `xxpoa_os_file` | char |  |

#### Indexes

| Flags | Index Name | Fields |
|-------|------------|--------|
| pu | `pri` | xxpoa_domain, xxpoa_nbr, xxpoa_rev |

---

### xxnote_mstr

#### Fields

| Order | Field Name | Data Type | Flags |
|-------|------------|-----------|-------|
| 10 | `oid_xxnote_mstr` | deci-2 |  |
| 20 | `xxnote_datetime` | datetm-tz | i |
| 30 | `xxnot_userid` | char |  |
| 40 | `xxnote_comment` | char |  |
| 50 | `xxnote_ref` | deci-2 | i |
| 60 | `xxnote_file` | blob |  |
| 70 | `xxnote_filename` | char |  |
| 80 | `xxnote_internal` | logi |  |
| 90 | `xxnote_security` | char |  |
| 100 | `xxnote_type` | char |  |
| 110 | `xxnote_field` | char |  |
| 120 | `xxnote_label` | char |  |

#### Indexes

| Flags | Index Name | Fields |
|-------|------------|--------|
| pu | `pri` | xxnote_ref, xxnote_datetime |

---

### xxmaild_det

#### Fields

| Order | Field Name | Data Type | Flags |
|-------|------------|-----------|-------|
| 10 | `xxmaild_seq` | inte | i |
| 20 | `xxmaild_name` | char | i |
| 30 | `xxmaild_mime` | char |  |
| 40 | `xxmaild_file` | blob |  |

#### Indexes

| Flags | Index Name | Fields |
|-------|------------|--------|
| p | `pri` | xxmaild_seq, xxmaild_name |

---

## Location & Configuration Tables

### xxloc_mstr

#### Fields

| Order | Field Name | Data Type | Flags |
|-------|------------|-----------|-------|
| 10 | `oid_xxloc_mstr` | deci | i |
| 20 | `xxloc_has_notes` | logi |  |
| 30 | `xxloc_has_attachments` | logi |  |
| 40 | `xxloc_domain` | char | i |
| 50 | `xxloc_supplier` | char | i |
| 60 | `xxloc_site` | char | i |
| 70 | `xxloc_location` | char |  |

#### Indexes

| Flags | Index Name | Fields |
|-------|------------|--------|
| u | `oid` | oid_xxloc_mstr |
| pu | `pri` | xxloc_domain, xxloc_supplier, xxloc_site |

---

### xxrole_mstr

#### Fields

| Order | Field Name | Data Type | Flags |
|-------|------------|-----------|-------|
| 10 | `oid_xxrole_mstr` | deci-2 | i |
| 20 | `xxrole_domain` | char | i |
| 40 | `xxrole_type` | char | i |
| 50 | `xxrole_value` | char | i |
| 60 | `xxrole_approver` | char | i |
| 70 | `xxrole_role` | char | i |

#### Indexes

| Flags | Index Name | Fields |
|-------|------------|--------|
|  | `byrole` | xxrole_domain, xxrole_role |
|  | `byvalue` | xxrole_domain, xxrole_value |
| u | `oid` | oid_xxrole_mstr |
| pu | `pri` | xxrole_domain, xxrole_type, xxrole_role, xxrole_value |

---

### xxlang_mstr

#### Fields

| Order | Field Name | Data Type | Flags |
|-------|------------|-----------|-------|
| 10 | `oid_xxlang_mstr` | deci-2 | i |
| 20 | `xxlang_has_notes` | logi |  |
| 30 | `xxlang_has_attachments` | logi |  |
| 40 | `xxlang_date_format` | char |  |
| 50 | `xxlang_separator` | char |  |
| 60 | `xxlang_decimal` | char |  |
| 70 | `xxlang_code` | char | i |
| 80 | `xxlang_erp_lang` | char |  |
| 90 | `xxlang_dp_code` | char |  |
| 100 | `xxlang_desc` | char |  |

#### Indexes

| Flags | Index Name | Fields |
|-------|------------|--------|
| pu | `bycode` | xxlang_code |
| u | `oid` | oid_xxlang_mstr |

---

### xxlangd_det

#### Fields

| Order | Field Name | Data Type | Flags |
|-------|------------|-----------|-------|
| 10 | `oid_xxlangd_det` | deci-2 | i |
| 20 | `xxlangd_has_notes` | logi |  |
| 30 | `xxlangd_has_attachments` | logi |  |
| 40 | `xxlangd_form` | char | i |
| 50 | `xxlangd_ref` | char | i |
| 60 | `xxlangd_text` | char | i |
| 70 | `xxlangd_lang` | char | i |
| 80 | `xxlangd_help` | char |  |

#### Indexes

| Flags | Index Name | Fields |
|-------|------------|--------|
| pu | `bylang` | xxlangd_lang, xxlangd_form, xxlangd_ref |
|  | `bylang2` | xxlangd_lang |
|  | `byref` | xxlangd_ref |
| u | `oid` | oid_xxlangd_det |

---

### xxmail_mstr

**Description:** 0 = New, 10 = Processing, 20 = Done, 30 = Error

#### Fields

| Order | Field Name | Data Type | Flags |
|-------|------------|-----------|-------|
| 10 | `xxmail_seq` | inte | i |
| 20 | `xxmail_to` | char |  |
| 30 | `xxmail_from` | char |  |
| 40 | `xxmail_cc` | char |  |
| 50 | `xxmail_subject` | char |  |
| 70 | `xxmail_mime` | char |  |
| 80 | `xxmail_importance` | inte |  |
| 90 | `xxmail_status` | inte | i |
| 100 | `xxmail_error` | char |  |
| 110 | `xxmail_body` | clob |  |
| 120 | `xxmail_user` | char | i |
| 130 | `xxmail_date` | datetm | i |

#### Indexes

| Flags | Index Name | Fields |
|-------|------------|--------|
|  | `byStatus` | xxmail_status, xxmail_seq |
|  | `byUser` | xxmail_user |
| pu | `pri` | xxmail_seq |

---

### xxlink_mstr

#### Fields

| Order | Field Name | Data Type | Flags |
|-------|------------|-----------|-------|
| 10 | `oid_xxlink_mstr` | deci-2 | i |
| 20 | `xxlink_type` | char | i |
| 30 | `xxlink_domain` | char | i |
| 40 | `xxlink_key` | char | i |
| 50 | `xxlink_url` | char |  |
| 60 | `xxlink_tooltip` | char |  |
| 70 | `xxlink_icon_url` | char |  |
| 80 | `xxlink_icon_file` | blob |  |
| 90 | `xxlink_seq` | inte | i |
| 100 | `xxlink_security` | char |  |

#### Indexes

| Flags | Index Name | Fields |
|-------|------------|--------|
| u | `oid` | oid_xxlink_mstr |
| pu | `pri` | xxlink_type, xxlink_domain, xxlink_key, xxlink_seq |

---

### xxshipd_det

#### Fields

| Order | Field Name | Data Type | Flags |
|-------|------------|-----------|-------|
| 10 | `xxshipd_transid` | char | i |
| 20 | `xxshipd_sequence` | inte | i |
| 40 | `xxshipd_weight_uom` | char |  |
| 80 | `xxshipd_dimension_uom` | char |  |
| 90 | `xxshipd_tracking` | char |  |
| 100 | `xxshipd_label` | blob |  |
| 110 | `xxshipd_weight` | char |  |
| 120 | `xxshipd_width` | char |  |
| 130 | `xxshipd_height` | char |  |
| 140 | `xxshipd_length` | char |  |

#### Indexes

| Flags | Index Name | Fields |
|-------|------------|--------|
| pu | `pri` | xxshipd_transid, xxshipd_sequence |

---

## System Tables

### appsrv_mstr

#### Fields

| Order | Field Name | Data Type | Flags |
|-------|------------|-----------|-------|
| 20 | `appsrv_domain` | char |  |
| 30 | `appsrv_connect` | char |  |
| 40 | `appsrv_cache` | logi |  |
| 60 | `oid_appsrv_mstr` | deci-2 | i |
| 70 | `appsrv_name` | char | i |
| 80 | `appsrv_proxy` | char |  |

#### Indexes

| Flags | Index Name | Fields |
|-------|------------|--------|
| u | `oid` | oid_appsrv_mstr |
| pu | `pri` | appsrv_name |

---

### efw_audit

#### Fields

| Order | Field Name | Data Type | Flags |
|-------|------------|-----------|-------|
| 10 | `efw_audit_sequence` | inte | i |
| 20 | `efw_audit_action` | char | i |
| 30 | `efw_audit_table` | char | i |
| 40 | `efw_audit_key_value` | char | i |
| 50 | `efw_audit_userid` | char | i |
| 60 | `efw_audit_date` | date |  |
| 70 | `efw_audit_time` | inte |  |
| 80 | `efw_audit_datetime` | datetm | i |
| 90 | `efw_audit_datetime_tz` | datetm-tz |  |
| 100 | `efw_audit_domain` | char | i |
| 110 | `efw_audit_before_xml` | blob |  |
| 120 | `efw_audit_after_xml` | blob |  |
| 130 | `efw_audit_fields` | char |  |

#### Indexes

| Flags | Index Name | Fields |
|-------|------------|--------|
|  | `by_datetime` | efw_audit_datetime |
|  | `by_keyvalue` | efw_audit_key_value |
|  | `by_table` | efw_audit_table |
|  | `by_userid` | efw_audit_userid |
| u | `dom-seq` | efw_audit_domain, efw_audit_sequence |
| u | `keyvalue` | efw_audit_domain, efw_audit_table, efw_audit_key_value, efw_audit_sequence |
| pu | `pri` | efw_audit_sequence |

---

### iaach_mstr

#### Fields

| Order | Field Name | Data Type | Flags |
|-------|------------|-----------|-------|
| 10 | `oid_iaach_mstr` | deci | i |
| 20 | `iaach_has_notes` | logi |  |
| 30 | `iaach_has_attachments` | logi |  |
| 40 | `iaach_req_userid` | char | i |
| 50 | `iaach_req_date` | datetm-tz | i |
| 60 | `iaach_req_status` | char | i |
| 70 | `iaach_has_approved` | char | i |
| 80 | `iaach_to_approve` | char | i |
| 90 | `iaach_domain` | char | i |
| 100 | `iaach_filename` | char |  |
| 110 | `iaach_filedatetime` | datetm |  |
| 120 | `iaach_total` | deci-0 |  |
| 130 | `iaach_details` | char |  |
| 140 | `iaach_file` | blob |  |

#### Indexes

| Flags | Index Name | Fields |
|-------|------------|--------|
|  | `bystatus` | iaach_req_status, iaach_req_date |
| pu | `oid` | oid_iaach_mstr |
|  | `req_date` | iaach_req_date |
|  | `req_userid` | iaach_req_userid |

---

### iaqt_mstr

#### Fields

| Order | Field Name | Data Type | Flags |
|-------|------------|-----------|-------|
| 10 | `oid_iaqt_mstr` | deci | i |
| 20 | `iaqt_has_notes` | logi |  |
| 30 | `iaqt_has_attachments` | logi |  |
| 40 | `iaqt_has_approved` | char | i |
| 50 | `iaqt_to_approve` | char | i |
| 60 | `iaqt_req_userid` | char | i |
| 70 | `iaqt_req_date` | datetm-tz | i |
| 80 | `iaqt_req_status` | char | i |
| 90 | `iaqt_orig_lead` | char |  |
| 100 | `iaqt_margin_pct` | deci |  |
| 110 | `iaqt_domain` | char | i |
| 120 | `iaqt_nbr` | char | i |
| 130 | `iaqt_desc` | char |  |
| 140 | `iaqt_cust` | char | i |
| 150 | `iaqt_slspsn` | char |  |
| 160 | `iaqt_tsm` | char |  |
| 170 | `iaqt_rsm` | char |  |
| 180 | `iaqt_site` | char |  |
| 190 | `iaqt_credit_terms` | char |  |
| 200 | `iaqt_currency` | char |  |
| 210 | `iaqt_delivered` | logi |  |
| 220 | `iaqt_closed` | logi |  |
| 230 | `iaqt_contact_name` | char |  |
| 240 | `iaqt_contact_title` | char |  |
| 250 | `iaqt_contact_addr1` | char |  |
| 260 | `iaqt_contact_addr2` | char |  |
| 270 | `iaqt_contact_addr3` | char |  |
| 280 | `iaqt_contact_city` | char |  |
| 290 | `iaqt_contact_state` | char |  |
| 300 | `iaqt_contact_zip` | char |  |
| 310 | `iaqt_contact_country` | char |  |
| 320 | `iaqt_contact_phone` | char |  |
| 330 | `iaqt_contact_mobile` | char |  |
| 340 | `iaqt_contact_fax` | char |  |
| 350 | `iaqt_contact_email1` | char |  |
| 360 | `iaqt_contact_email2` | char |  |
| 370 | `iaqt_date_rcvd` | date |  |
| 380 | `iaqt_date_delivered` | datetm-tz |  |
| 390 | `iaqt_date_expire` | date |  |
| 400 | `iaqt_uchar1` | char |  |
| 410 | `iaqt_uchar2` | char |  |
| 420 | `iaqt_uchar3` | char |  |
| 430 | `iaqt_uchar4` | char |  |
| 440 | `iaqt_uchar5` | char |  |
| 450 | `iaqt_uchar6` | char |  |
| 460 | `iaqt_uchar7` | char |  |
| 470 | `iaqt_uchar8` | char |  |
| 480 | `iaqt_uchar9` | char |  |
| 490 | `iaqt_uchar10` | char |  |
| 500 | `iaqt_uchar11` | char |  |
| 510 | `iaqt_uchar12` | char |  |
| 520 | `iaqt_uchar13` | char |  |
| 530 | `iaqt_uchar14` | char |  |
| 540 | `iaqt_uchar15` | char |  |
| 550 | `iaqt_udec1` | deci |  |
| 560 | `iaqt_udec2` | deci |  |
| 570 | `iaqt_udec3` | deci |  |
| 580 | `iaqt_udec4` | deci |  |
| 590 | `iaqt_udec5` | deci |  |
| 600 | `iaqt_udec6` | deci |  |
| 610 | `iaqt_udec7` | deci |  |
| 620 | `iaqt_udec8` | deci |  |
| 630 | `iaqt_udec9` | deci |  |
| 640 | `iaqt_udec10` | deci |  |
| 650 | `iaqt_udate1` | date |  |
| 660 | `iaqt_udate2` | date |  |
| 670 | `iaqt_udate3` | date |  |
| 680 | `iaqt_udate4` | date |  |
| 690 | `iaqt_udate5` | date |  |
| 700 | `iaqt_udate6` | date |  |
| 710 | `iaqt_udate7` | date |  |
| 720 | `iaqt_udate8` | date |  |
| 730 | `iaqt_udate9` | date |  |
| 740 | `iaqt_udate10` | date |  |
| 750 | `iaqt_ulog1` | logi |  |
| 760 | `iaqt_ulog2` | logi |  |
| 770 | `iaqt_ulog3` | logi |  |
| 780 | `iaqt_ulog4` | logi |  |
| 790 | `iaqt_ulog5` | logi |  |
| 800 | `iaqt_ulog6` | logi |  |
| 810 | `iaqt_ulog7` | logi |  |
| 820 | `iaqt_ulog8` | logi |  |
| 830 | `iaqt_ulog9` | logi |  |
| 840 | `iaqt_ulog10` | logi |  |
| 850 | `iaqt_date_closed` | date |  |
| 860 | `iaqt_stage` | char |  |
| 870 | `iaqt_disposition` | char | m |
| 880 | `iaqt_loss` | char |  |
| 890 | `iaqt_last_contact` | char |  |
| 900 | `iaqt_date_last` | date |  |
| 910 | `iaqt_follow` | date |  |
| 920 | `iaqt_next_steps` | char |  |
| 930 | `iaqt_lead_source` | char |  |
| 940 | `iaqt_industry` | char |  |
| 950 | `iaqt_sic` | char |  |
| 970 | `iaqt_ar_days_old` | inte |  |
| 980 | `iaqt_trl1_cd` | char |  |
| 990 | `iaqt_trl2_cd` | char |  |
| 1000 | `iaqt_trl3_cd` | char |  |
| 1010 | `iaqt_trl1_amt` | deci-2 |  |
| 1020 | `iaqt_trl2_amt` | deci-2 |  |
| 1030 | `iaqt_trl3_amt` | deci-2 |  |
| 1040 | `iaqt_total_tax` | deci-2 |  |
| 1050 | `iaqt_contact_nbr` | char |  |
| 1060 | `iaqt_total` | deci-2 |  |
| 1070 | `iaqt_total_ext` | deci-2 |  |
| 1080 | `wordidx` | char | i |
| 1090 | `iaqt_ship_via` | char |  |
| 1100 | `iaqt_fob_point` | char |  |
| 1110 | `iaqt_date_revised` | date |  |
| 1120 | `iaqt_signature` | blob |  |
| 1130 | `iaqt_last_so` | char |  |
| 1140 | `iaqt_channel` | char |  |

#### Indexes

| Flags | Index Name | Fields |
|-------|------------|--------|
|  | `bydate` | iaqt_domain, iaqt_req_date |
|  | `bydomain` | iaqt_domain |
|  | `bynbr` | iaqt_domain, iaqt_nbr |
|  | `bystatus` | iaqt_domain, iaqt_req_status |
|  | `bystatus2` | iaqt_req_status |
|  | `byuser` | iaqt_req_userid |
| pu | `oid` | oid_iaqt_mstr |

---

