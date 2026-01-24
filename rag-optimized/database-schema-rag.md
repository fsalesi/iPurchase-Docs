# Database Schema Reference (RAG-Optimized)

> This file is auto-generated for AI/RAG vector search optimization.
> Do not edit directly. Edit `reference/database-schema.md` and regenerate.

This document describes the iPurchase database tables, fields, and relationships.

## Core

Tables

- [wus_mstr](#wus-mstr) - User master table containing user profiles, credentials, approval limits, supervisor relationships, and delegation settings
- [wgr_mstr](#wgr-mstr) - Group definitions for organizing users
- [wugr_mstr](#wugr-mstr) - User-to-group membership mapping
- [pf_mstr](#pf-mstr) - System settings and configuration parameters

---

## Requisition

Tables

- [xxreq_mstr](#xxreq-mstr) - Requisition header containing status, dates, totals, vendor, buyer assignment, and workflow state
- [xxreqd_det](#xxreqd-det) - Requisition line items with quantities, costs, GL coding (account, cost center, sub-account, project), and item descriptions
- [xxreq_audit](#xxreq-audit) - Complete approval audit trail tracking who approved/rejected requisitions, when, and any comments
- [xxreq_attach](#xxreq-attach) - File attachments linked to requisitions

---

## Approval

Tables

- [xxapp_mstr](#xxapp-mstr) - Simple approval rules using AND logic
- [xxAppRule](#xxapprule) - Complex approval rule headers supporting nested AND/OR conditional logic via linked xxAppField conditions
- [xxAppField](#xxappfield) - Approval rule conditions forming a hierarchical tree structure

---

## Archive

& Attachment Tables

- [xxpo_archive](#xxpo-archive) - Archived PO PDF documents stored as BLOBs
- [xxnote_mstr](#xxnote-mstr) - Notes and comments with optional file attachments
- [xxmaild_det](#xxmaild-det) - Email detail records including attachments

---

## Configuration

Tables

- [xxloc_mstr](#xxloc-mstr) - Location/site master defining valid ship-to and bill-to locations for requisitions
- [xxrole_mstr](#xxrole-mstr) - Role definitions (Manager, Director, VP, etc
- [xxlang_mstr](#xxlang-mstr) - Language definitions for multi-language support
- [xxlangd_det](#xxlangd-det) - Language detail records containing locale-specific settings
- [xxmail_mstr](#xxmail-mstr) - Email queue header records for outbound notifications
- [xxlink_mstr](#xxlink-mstr) - Configurable links displayed in the iPurchase interface
- [xxshipd_det](#xxshipd-det) - Shipping detail records for requisition delivery information

---

## System

Tables

- [appsrv_mstr](#appsrv-mstr) - Application server (AppServer/PASOE) connection configuration for QAD domain integration
- [efw_audit](#efw-audit) - Enterprise framework audit trail tracking all database changes with before/after values

---

## Field Flags Reference

| Flag | Meaning |
|:----:|---------|
| `i` | Indexed - field is part of an index |
| `m` | Mandatory - field requires a value |
| `c` | Case sensitive |

---

## Core Tables

*Foundation tables for user management, groups, and system configuration.*

---

## wus_mstr - User Master Table

Stores all user accounts, profiles, and settings for iPurchase. Contains login credentials, approval limits, supervisor relationships, delegates, and user preferences.


**Use this table when you need to:**
- Look up user information by ID or name
- Find a user's supervisor or delegate
- Check user approval limits
- Query user email addresses
- Find users by department or role

**Common questions this answers:**
- What fields are in the user table?
- How do I find a user's supervisor?
- Where is the approval limit stored?
- What is wus_delegate?
- How do I check if a user is disabled?

**Related tables:** wgr_mstr (groups), wugr_mstr (group membership), pf_mstr (user preferences)

User master table containing user profiles, credentials, approval limits, supervisor relationships, and delegation settings. Central to all iPurchase authentication and authorization.

#### Fields

| Field | Type | Flags | Description |
|-------|------|:-----:|-------------|
| `wus_id` | char | im | Unique user identifier (login ID) |
| `wus_name` | char | i | Full display name |
| `wus_title` | char |  |  |
| `wus_company` | char | i |  |
| `wus_city` | char |  |  |
| `wus_state` | char |  |  |
| `wus_country` | char |  |  |
| `wus_post` | char |  |  |
| `wus_phone` | char |  |  |
| `wus_fax` | char |  |  |
| `wus_email` | char |  | Email address for notifications |
| `wus_type` | char | i | User type classification |
| `wus_create_date` | date |  |  |
| `wus_create_by` | char |  |  |
| `wus_disable` | logi | i | TRUE = account disabled |
| `wus_expire_date` | date |  | Account expiration date |
| `wus_password` | char |  | Encrypted password |
| `wus_street1` | char |  |  |
| `wus_street2` | char |  |  |
| `wus_failed_logins` | inte |  | Failed login attempt count |
| `wus_delegate` | char | i | User ID who can act on behalf |
| `wus_erp_id` | char |  | Linked QAD user code |
| `wus_erp_initials` | char | i |  |
| `wus_app_amt` | deci-2 |  | Approval limit amount |
| `wus_supervisor` | char | i | Supervisor user ID (org chart) |
| `wus_domains` | char |  | Accessible domains (* = all) |
| `wus_last_login` | date |  | Last successful login date |
| `wus_carrier` | char |  |  |
| `wus_mobile` | logi |  |  |
| `wus_groups` | char | i | Comma-separated group list |

#### Indexes

| Index | Type | Fields |
|-------|------|--------|
| `by_erp_initials` | - | `wus_erp_initials` |
| `by_wus_company` | - | `wus_company` |
| `by_wus_id` | Primary + Unique | `wus_id` |
| `by_wus_name` | - | `wus_name` |
| `by_wus_type` | - | `wus_type` |
| `wus_delegate` | - | `wus_delegate` |
| `wus_disable` | - | `wus_disable` |
| `wus_groups` | Word | `wus_groups` |
| `wus_name_word` | Word | `wus_name` |
| `wus_supervisor` | - | `wus_supervisor` |

---

---

## wgr_mstr - Group Master Table

Defines groups used for approval routing, permissions, and organizational structure. Groups can be referenced in approval rules.


**Use this table when you need to:**
- List all groups in the system
- Find group descriptions
- Query groups for approval routing

**Common questions this answers:**
- What groups exist in the system?
- How are groups defined?
- What is wgr_id?

**Related tables:** wugr_mstr (membership), xxapp_mstr (approval rules)

Group definitions for organizing users. Groups can be used in approval rules, permission lists, and Can-Do patterns.

#### Fields

| Field | Type | Flags | Description |
|-------|------|:-----:|-------------|
| `wgr_id` | char | im | Unique group identifier |
| `wgr_name` | char | i | Group display name |
| `wgr_desc` | char |  | Group description |
| `wgr_mgr` | char |  | Group manager user ID |
| `wgr_level` | char |  |  |
| `wgr_create_date` | date |  |  |
| `wgr_create_by` | char |  |  |
| `wgr_disable` | logi |  | TRUE = group disabled |
| `wgr_expire_date` | date |  |  |
| `wgr_type` | char | i | Group type classification |

#### Indexes

| Index | Type | Fields |
|-------|------|--------|
| `by_wgr_id` | Primary + Unique | `wgr_id` |
| `by_wgr_name` | - | `wgr_name` |
| `by_wgr_type` | - | `wgr_type` |

---

---

## wugr_mstr - User-Group Membership Table

Links users to groups. Each record represents one user belonging to one group.


**Use this table when you need to:**
- Find all members of a group
- Find which groups a user belongs to
- Check group membership for approval routing

**Common questions this answers:**
- Who is in a specific group?
- What groups does a user belong to?
- How is group membership stored?

**Related tables:** wus_mstr (users), wgr_mstr (groups)

User-to-group membership mapping. Links users to their assigned groups.

#### Fields

| Field | Type | Flags | Description |
|-------|------|:-----:|-------------|
| `wugr_gr_id` | char | im | Group ID (FK to wgr_mstr) |
| `wugr_us_id` | char | im | User ID (FK to wus_mstr) |
| `wugr_create_date` | date |  |  |
| `wugr_create_by` | char |  |  |
| `wugr_disable` | logi |  | TRUE = membership disabled |
| `wugr_expire_date` | date |  |  |

#### Indexes

| Index | Type | Fields |
|-------|------|--------|
| `by_wugr_id` | Primary + Unique | `wugr_gr_id`, `wugr_us_id` |
| `by_wugr_us_id` | - | `wugr_us_id`, `wugr_gr_id` |

---

---

## pf_mstr - Parameter/Preferences Master Table

Stores all system settings, user preferences, and configuration parameters. The central configuration table for iPurchase.


**Use this table when you need to:**
- Query system settings
- Find user-specific preferences
- Check feature flags
- Look up requisition type settings

**Common questions this answers:**
- Where are system settings stored?
- How do I find a specific setting?
- What is pf_chr1?
- How do I query settings by attribute name?

**Related tables:** System Settings documentation

System settings and configuration parameters. The heart of iPurchase configuration with 550+ settings controlling all aspects of system behavior.

#### Fields

| Field | Type | Flags | Description |
|-------|------|:-----:|-------------|
| `pf_us_id` | char | im | User ID or "SYSTEM" for global |
| `pf_attr` | char | im | Setting name/attribute |
| `pf_value` | char | i |  |
| `pf_alt_value` | char | i |  |
| `pf_date1` | date |  |  |
| `pf_date2` | date |  |  |
| `pf_log1` | logi |  | Boolean value |
| `pf_log2` | logi |  |  |
| `pf_dec1` | deci-2 |  | Decimal value |
| `pf_dec2` | deci-2 |  |  |
| `pf_group` | char | i | Setting group (usually "DEFAULT") |
| `pf_seq` | deci-3 | i |  |
| `pf_chr1` | char |  | Setting value (string) |
| `pf_chr2` | char |  | Secondary value |
| `pf_data_version` | deci-2 |  |  |
| `pf_default` | char |  |  |
| `pf_help` | char |  | Help text / description |
| `pf_notes` | char |  |  |

#### Indexes

| Index | Type | Fields |
|-------|------|--------|
| `Main` | Primary | `pf_us_id`, `pf_group`, `pf_attr`, `pf_value`, `pf_alt_value`, `pf_seq` |

---

## Requisition Tables

*Purchase requisition headers, line items, approvals, and attachments.*

---

## xxreq_mstr - Requisition Header Table

The main requisition table containing header-level information: status, dates, totals, vendor, buyer, and workflow state. Every requisition has one record here.


**Use this table when you need to:**
- Query requisitions by status, date, or user
- Find requisition totals and vendors
- Track approval workflow state
- Look up change order information

**Common questions this answers:**
- What fields are in the requisition header?
- How do I find requisitions by status?
- What is xxreq_obo (on behalf of)?
- Where is the requisition total stored?
- How do I identify change orders?

**Related tables:** xxreqd_det (line items), xxreq_audit (approvals), xxreq_attach (attachments)

Requisition header containing status, dates, totals, vendor, buyer assignment, and workflow state. Primary key is domain + requisition number.

#### Fields

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

#### Indexes

| Index | Type | Fields |
|-------|------|--------|
| `approvedidc` | - | `xxreq_approved` |
| `byblanket` | - | `xxreq_blanket_nbr` |
| `byconsnbr` | - | `xxreq_cons_nbr` |
| `cart_id` | - | `xxreq_cartid` |
| `entry_date` | - | `xxreq_date` |
| `ext_notes` | Word | `xxreq_ext_notes` |
| `field1` | - | `xxreq_sort_field1` |
| `field10` | - | `xxreq_sort_field10` |
| `field2` | - | `xxreq_sort_field2` |
| `field3` | - | `xxreq_sort_field3` |
| `field4` | - | `xxreq_sort_field4` |
| `field5` | - | `xxreq_sort_field5` |
| `field6` | - | `xxreq_sort_field6` |
| `field7` | - | `xxreq_sort_field7` |
| `field8` | - | `xxreq_sort_field9` |
| `field9` | - | `xxreq_sort_field9` |
| `int_notes` | Word | `xxreq_int_notes` |
| `nbr` | Primary | `xxreq_nbr` |
| `req-userid` | - | `xxreq_userid` |
| `req_stat` | - | `xxreq_status` |
| `submittedidx` | - | `xxreq_submitted` |
| `typeidx` | - | `xxreq_type` |
| `vend` | - | `xxreq_vendor` |
| `word_idx2` | Word | `xxreq_word_idx2` |
| `word_idx3` | Word | `xxreq_word_idx3` |
| `word_idx_bucket` | Word | `xxreq_word_idx` |
| `xxdomain` | - | `xxreq_domain` |
| `xxreq_buyer` | - | `xxreq_buyer` |
| `xxreq_copied_from` | - | `xxreq_domain`, `xxreq_copied_from` |
| `xxreq_cost` | - | `xxreq_cost` |
| `xxreq_po_nbr` | - | `xxreq_domain`, `xxreq_po_nbr` |

---

---

## xxreqd_det - Requisition Detail/Line Items Table

Stores individual line items within requisitions. Each line has quantity, cost, GL coding, and item details.


**Use this table when you need to:**
- Query line items for a requisition
- Find line totals and quantities
- Look up GL account coding
- Analyze spending by cost center

**Common questions this answers:**
- What fields are in requisition line items?
- How do I find lines for a requisition?
- Where is the line total stored?
- What is xxreqd_cc (cost center)?

**Related tables:** xxreq_mstr (header), GL account structure

Requisition line items with quantities, costs, GL coding (account, cost center, sub-account, project), and item descriptions.

#### Fields

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

#### Indexes

| Index | Type | Fields |
|-------|------|--------|
| `account` | - | `xxreqd_acct` |
| `cc` | - | `xxreqd_cc` |
| `ext_notes` | Word | `xxreqd_ext_notes` |
| `int_notes` | Word | `xxreqd_int_notes` |
| `item` | - | `xxreqd_item` |
| `po` | - | `xxreqd_domain`, `xxreqd_po_nbr` |
| `pri` | Primary + Unique | `xxreqd_domain`, `xxreqd_nbr`, `xxreqd_line` |
| `vendor` | - | `xxreqd_domain`, `xxreqd_vendor` |
| `xxreqd_u_code` | - | `xxreqd_u_code` |
| `xxreqd_word_idx` | Word | `xxreqd_word_idx` |

---

---

## xxreq_audit - Requisition Approval Audit Trail Table

Records all approval actions taken on requisitions. Shows who approved/rejected, when, and any comments. Critical for audit and workflow analysis.


**Use this table when you need to:**
- Find who approved a requisition
- Track approval workflow history
- Calculate approval cycle times
- Audit approval actions

**Common questions this answers:**
- Who approved this requisition?
- What is the approval history?
- How long did approval take?
- What is xxreq_actual_approver vs xxreq_app_id?

**Related tables:** xxreq_mstr (requisition), xxapp_mstr (rules)

Complete approval audit trail tracking who approved/rejected requisitions, when, and any comments. Essential for compliance reporting.

#### Fields

| Field | Type | Flags | Description |
|-------|------|:-----:|-------------|
| `xxreq_nbr` | char | i | Requisition number |
| `xxreq_submit_date` | date |  |  |
| `xxreq_submit_time` | inte |  |  |
| `xxreq_submit_attempt` | inte | i |  |
| `xxreq_app_id` | char | i | Required approver (user/group) |
| `xxreq_decom_app_id` | char | i | Expanded approver (individuals) |
| `xxreq_app_seq` | deci-2 |  | Approval sequence number |
| `xxreq_last_notified_date` | date |  |  |
| `xxreq_last_notified_time` | inte |  |  |
| `xxreq_actual_approver` | char |  | Who actually approved |
| `xxreq_app_date` | date |  | Approval date |
| `xxreq_app_time` | inte |  | Approval time (seconds) |
| `xxreq_app_notes` | char |  | Approval comments |
| `xxreq_status` | char |  | Status: blank=draft, CONFIRMED=submitted, APPROVED=approved |
| `xxreq_unique` | inte | i |  |
| `xxreq_domain` | char | i | Domain/company code |
| `xxreq_active` | logi |  |  |
| `xxreq_last_set` | logi |  |  |
| `xxreq_auditm_seq` | inte |  |  |
| `xxreq_active_date` | date | i | Date entered queue |
| `xxreq_active_time` | inte | i |  |
| `xxreq_reject_code` | char | i |  |
| `xxreq_date1` | date |  |  |
| `xxreq_date2` | date |  |  |
| `xxreq_dec1` | deci-2 |  |  |
| `xxreq_dec2` | deci-2 |  |  |
| `xxreq_ulog1` | logi |  |  |
| `xxreq_ulog2` | logi |  |  |
| `xxreq_uchar1` | char |  |  |
| `xxreq_uchar2` | char |  |  |

#### Indexes

| Index | Type | Fields |
|-------|------|--------|
| `active_date` | - | `xxreq_domain`, `xxreq_active_date`, `xxreq_active_time` |
| `approver` | - | `xxreq_domain`, `xxreq_nbr`, `xxreq_submit_attempt`, `xxreq_app_id` |
| `decomposed` | Word | `xxreq_decom_app_id` |
| `pri` | Primary + Unique | `xxreq_unique` |
| `xxreq_reject_code` | - | `xxreq_reject_code` |

---

---

## xxreq_attach

File attachments linked to requisitions. Stores binary BLOB data for supporting documents.

#### Fields

| Field | Type | Flags | Description |
|-------|------|:-----:|-------------|
| `xxreq_domain` | char | i | Domain/company code |
| `xxreq_nbr` | char | i | Requisition number |
| `xxreq_filename` | char | i |  |
| `xxreq_line` | inte | i |  |
| `xxreq_os_filename` | char |  |  |
| `xxreq_int_ext` | logi |  |  |
| `xxreq_security` | char |  |  |
| `xxreq_file` | blob |  | BLOB file data |
| `xxreq_user` | char |  |  |
| `xxreq_date` | datetm-tz |  | Need-by date |

#### Indexes

| Index | Type | Fields |
|-------|------|--------|
| `pri` | Primary + Unique | `xxreq_domain`, `xxreq_nbr`, `xxreq_line`, `xxreq_filename` |

---

## Approval Tables

*Approval workflow rules - both simple (AND-based) and complex (AND/OR tree) configurations.*

---

## xxapp_mstr - Simple Approval Rules Table

Stores simple approval rules using AND logic. The primary table for configuring approval routing based on amount, cost center, account, and other criteria.


**Use this table when you need to:**
- Query approval rules
- Find who approves for specific criteria
- Check approval thresholds
- Debug approval routing

**Common questions this answers:**
- What fields are in the approval rules table?
- How do I find rules by cost center?
- What is xxapp_seq (sequence)?
- How do amount thresholds work?
- What does xxapp_which_cost mean?

**Related tables:** xxAppRule (complex rules), xxAppField (conditions), xxreq_audit (history)

Simple approval rules using AND logic. Recommended for most approval routing scenarios. Supports amount thresholds, GL filters, and originator matching.

#### Fields

| Field | Type | Flags | Description |
|-------|------|:-----:|-------------|
| `xxapp_type` | char | i | Req type filter (* = all) |
| `xxapp_po_site` | char | i |  |
| `xxapp_cc` | char | i | Cost center filter (Can-Do) |
| `xxapp_amount` | deci-2 | i | Minimum amount threshold |
| `xxapp_id` | char | i | Approver (user/group/variable) |
| `xxapp_seq` | inte | i | Approval sequence (routing order) |
| `xxapp_domain` | char | i | Domain filter (* = all) |
| `xxapp_acct` | char | i | Account filter (Can-Do) |
| `xxapp_sub` | char | i | Sub-account filter (Can-Do) |
| `xxapp_project` | char | i | Project filter (Can-Do) |
| `oid_xxapp_mstr` | deci-2 | i |  |
| `xxapp_has_notes` | logi |  |  |
| `xxapp_has_attachments` | logi |  |  |
| `xxapp_max_amount` | deci-2 | i | Maximum amount threshold |
| `xxapp_description` | char | i | Rule description |
| `xxapp_active` | logi | i | TRUE = rule active |
| `xxapp_orig` | char |  | Originator filter (Can-Do) |
| `xxapp_notify` | logi | i | TRUE = notification only |
| `xxapp_line_site` | char |  |  |
| `xxapp_stop` | logi |  | TRUE = stop after this rule |
| `xxapp_which_cost` | char |  | Header or Line cost |
| `xxapp_unspsc` | char | i |  |

#### Indexes

| Index | Type | Fields |
|-------|------|--------|
| `byacct` | - | `xxapp_acct` |
| `byactive` | - | `xxapp_active` |
| `bydept` | - | `xxapp_cc` |
| `bydesc` | - | `xxapp_description` |
| `bydomain` | - | `xxapp_domain` |
| `byid` | - | `xxapp_id` |
| `bymax` | - | `xxapp_max_amount` |
| `bymin` | - | `xxapp_amount` |
| `bynotify` | - | `xxapp_notify` |
| `byproj` | - | `xxapp_project` |
| `byseq` | - | `xxapp_seq` |
| `bysite` | - | `xxapp_po_site` |
| `bysub` | - | `xxapp_sub` |
| `bytype` | - | `xxapp_type` |
| `byunspsc` | - | `xxapp_unspsc` |
| `oid` | Primary + Unique | `oid_xxapp_mstr` |

---

---

## xxAppRule - Complex Approval Rules Table

Stores complex approval rules with nested AND/OR logic. Used for advanced routing scenarios that simple rules cannot handle.


**Use this table when you need to:**
- Query complex approval rules
- Find rules with OR conditions
- Debug advanced routing logic

**Common questions this answers:**
- When should I use complex vs simple rules?
- How do complex rules work?
- What is xxAR_Approver?
- How do I use $SUPERVISORS variable?

**Related tables:** xxAppField (conditions), xxapp_mstr (simple rules)

Complex approval rule headers supporting nested AND/OR conditional logic via linked xxAppField conditions.

#### Fields

| Field | Type | Flags | Description |
|-------|------|:-----:|-------------|
| `xxAR_Domain` | char | i | Domain filter |
| `xxAR_RuleName` | char | i | Rule name (primary key) |
| `xxAR_AppLevel` | deci-2 |  | Approval sequence number |
| `xxAR_Approver` | char |  | Approver (supports $variables) |
| `xxAR_AmtType` | char |  | Header or Line |
| `xxAR_MinAmt` | deci-2 |  | Minimum amount |
| `xxAR_MaxAmt` | deci-2 |  | Maximum amount |
| `xxAR_Active` | logi |  | TRUE = rule active |
| `xxAR_stop` | logi |  | TRUE = stop after match |
| `xxAR_Eval_Lines` | logi |  | TRUE = evaluate per line |
| `xxAR_notify` | logi |  | TRUE = notification only |

#### Indexes

| Index | Type | Fields |
|-------|------|--------|
| `pri` | Primary + Unique | `xxAR_Domain`, `xxAR_RuleName` |

---

---

## xxAppField - Complex Rule Conditions Table

Stores the conditions for complex approval rules. Forms a tree structure with AND/OR operators linking field comparisons.


**Use this table when you need to:**
- Query rule conditions
- Understand rule logic tree
- Debug why rules match or don't match

**Common questions this answers:**
- How are complex rule conditions structured?
- What is xxAF_Parent?
- How does the condition tree work?

**Related tables:** xxAppRule (rule header)

Approval rule conditions forming a hierarchical tree structure. Linked to xxAppRule for complex conditional evaluation.

#### Fields

| Field | Type | Flags | Description |
|-------|------|:-----:|-------------|
| `xxAF_Domain` | char | i |  |
| `xxAF_RuleName` | char | i | Rule name (FK to xxAppRule) |
| `xxAF_Seq` | inte | i | Condition sequence |
| `xxAF_Table` | char |  | Table name (empty for operator) |
| `xxAF_Field` | char |  | Field name (empty for operator) |
| `xxAF_Value` | char |  | Comparison value ($var supported) |
| `xxAF_Operand` | char |  | AND/OR or comparison operator |
| `xxAF_Group` | inte |  | This node group (0 = leaf) |
| `xxAF_Parent` | inte |  | Parent group number |

#### Indexes

| Index | Type | Fields |
|-------|------|--------|
| `pri` | Primary | `xxAF_Domain`, `xxAF_RuleName`, `xxAF_Seq` |

---

## Archive & Attachment Tables

*Document storage for PO archives, notes, and email attachments.*

---

## xxpo_archive

Archived PO PDF documents stored as BLOBs. Supports multiple revisions per PO number.

#### Fields

| Field | Type | Flags | Description |
|-------|------|:-----:|-------------|
| `xxpoa_domain` | char | i | Domain code |
| `xxpoa_nbr` | char | i | PO number |
| `xxpoa_datetime` | datetm-tz |  | Archive timestamp |
| `xxpoa_user` | char |  | User who archived |
| `xxpoa_rev` | deci-2 | i | Revision number |
| `xxpoa_pdf` | blob |  | BLOB PDF data |
| `xxpoa_os_file` | char |  |  |

#### Indexes

| Index | Type | Fields |
|-------|------|--------|
| `pri` | Primary + Unique | `xxpoa_domain`, `xxpoa_nbr`, `xxpoa_rev` |

---

---

## xxnote_mstr

Notes and comments with optional file attachments. Can be linked to requisitions, POs, or other entities.

#### Fields

| Field | Type | Flags | Description |
|-------|------|:-----:|-------------|
| `oid_xxnote_mstr` | deci-2 |  |  |
| `xxnote_datetime` | datetm-tz | i |  |
| `xxnot_userid` | char |  |  |
| `xxnote_comment` | char |  |  |
| `xxnote_ref` | deci-2 | i |  |
| `xxnote_file` | blob |  |  |
| `xxnote_filename` | char |  |  |
| `xxnote_internal` | logi |  |  |
| `xxnote_security` | char |  |  |
| `xxnote_type` | char |  |  |
| `xxnote_field` | char |  |  |
| `xxnote_label` | char |  |  |

#### Indexes

| Index | Type | Fields |
|-------|------|--------|
| `pri` | Primary + Unique | `xxnote_ref`, `xxnote_datetime` |

---

---

## xxmaild_det

Email detail records including attachments. Part of the email queue system.

#### Fields

| Field | Type | Flags | Description |
|-------|------|:-----:|-------------|
| `xxmaild_seq` | inte | i |  |
| `xxmaild_name` | char | i |  |
| `xxmaild_mime` | char |  |  |
| `xxmaild_file` | blob |  |  |

#### Indexes

| Index | Type | Fields |
|-------|------|--------|
| `pri` | Primary | `xxmaild_seq`, `xxmaild_name` |

---

## Configuration Tables

*Location, role, language, and link configuration for iPurchase customization.*

---

## xxloc_mstr

Location/site master defining valid ship-to and bill-to locations for requisitions.

#### Fields

| Field | Type | Flags | Description |
|-------|------|:-----:|-------------|
| `oid_xxloc_mstr` | deci | i |  |
| `xxloc_has_notes` | logi |  |  |
| `xxloc_has_attachments` | logi |  |  |
| `xxloc_domain` | char | i |  |
| `xxloc_supplier` | char | i |  |
| `xxloc_site` | char | i |  |
| `xxloc_location` | char |  |  |

#### Indexes

| Index | Type | Fields |
|-------|------|--------|
| `bydomain` | - | `xxloc_domain` |
| `oid` | Unique | `oid_xxloc_mstr` |
| `pri` | Primary + Unique | `xxloc_domain`, `xxloc_supplier`, `xxloc_site` |

---

---

## xxrole_mstr

Role definitions (Manager, Director, VP, etc.) for role-based approval routing.

#### Fields

| Field | Type | Flags | Description |
|-------|------|:-----:|-------------|
| `oid_xxrole_mstr` | deci-2 | i |  |
| `xxrole_domain` | char | i |  |
| `xxrole_type` | char | i |  |
| `xxrole_value` | char | i |  |
| `xxrole_approver` | char | i |  |
| `xxrole_role` | char | i |  |

#### Indexes

| Index | Type | Fields |
|-------|------|--------|
| `byapprover` | - | `xxrole_domain`, `xxrole_approver` |
| `byrole` | - | `xxrole_domain`, `xxrole_role` |
| `byvalue` | - | `xxrole_domain`, `xxrole_value` |
| `oid` | Unique | `oid_xxrole_mstr` |
| `pri` | Primary + Unique | `xxrole_domain`, `xxrole_type`, `xxrole_role`, `xxrole_value` |

---

---

## xxlang_mstr

Language definitions for multi-language support.

#### Fields

| Field | Type | Flags | Description |
|-------|------|:-----:|-------------|
| `oid_xxlang_mstr` | deci-2 | i |  |
| `xxlang_has_notes` | logi |  |  |
| `xxlang_has_attachments` | logi |  |  |
| `xxlang_date_format` | char |  |  |
| `xxlang_separator` | char |  |  |
| `xxlang_decimal` | char |  |  |
| `xxlang_code` | char | i |  |
| `xxlang_erp_lang` | char |  |  |
| `xxlang_dp_code` | char |  |  |
| `xxlang_desc` | char |  |  |

#### Indexes

| Index | Type | Fields |
|-------|------|--------|
| `bycode` | Primary + Unique | `xxlang_code` |
| `oid` | Unique | `oid_xxlang_mstr` |

---

---

## xxlangd_det

Language detail records containing locale-specific settings.

#### Fields

| Field | Type | Flags | Description |
|-------|------|:-----:|-------------|
| `oid_xxlangd_det` | deci-2 | i |  |
| `xxlangd_has_notes` | logi |  |  |
| `xxlangd_has_attachments` | logi |  |  |
| `xxlangd_form` | char | i |  |
| `xxlangd_ref` | char | i |  |
| `xxlangd_text` | char | i |  |
| `xxlangd_lang` | char | i |  |
| `xxlangd_help` | char |  |  |

#### Indexes

| Index | Type | Fields |
|-------|------|--------|
| `byform` | - | `xxlangd_form` |
| `bylang` | Primary + Unique | `xxlangd_lang`, `xxlangd_form`, `xxlangd_ref` |
| `bylang2` | - | `xxlangd_lang` |
| `byref` | - | `xxlangd_ref` |
| `bytext` | Word | `xxlangd_text` |
| `oid` | Unique | `oid_xxlangd_det` |

---

---

## xxmail_mstr

Email queue header records for outbound notifications.

#### Fields

| Field | Type | Flags | Description |
|-------|------|:-----:|-------------|
| `xxmail_seq` | inte | i |  |
| `xxmail_to` | char |  |  |
| `xxmail_from` | char |  |  |
| `xxmail_cc` | char |  |  |
| `xxmail_subject` | char |  |  |
| `xxmail_mime` | char |  |  |
| `xxmail_importance` | inte |  |  |
| `xxmail_status` | inte | i |  |
| `xxmail_error` | char |  |  |
| `xxmail_body` | clob |  |  |
| `xxmail_user` | char | i |  |
| `xxmail_date` | datetm | i |  |

#### Indexes

| Index | Type | Fields |
|-------|------|--------|
| `byDate` | - | `xxmail_date` |
| `byStatus` | - | `xxmail_status`, `xxmail_seq` |
| `byUser` | - | `xxmail_user` |
| `pri` | Primary + Unique | `xxmail_seq` |

---

---

## xxlink_mstr

Configurable links displayed in the iPurchase interface.

#### Fields

| Field | Type | Flags | Description |
|-------|------|:-----:|-------------|
| `oid_xxlink_mstr` | deci-2 | i |  |
| `xxlink_type` | char | i |  |
| `xxlink_domain` | char | i |  |
| `xxlink_key` | char | i |  |
| `xxlink_url` | char |  |  |
| `xxlink_tooltip` | char |  |  |
| `xxlink_icon_url` | char |  |  |
| `xxlink_icon_file` | blob |  |  |
| `xxlink_seq` | inte | i |  |
| `xxlink_security` | char |  |  |

#### Indexes

| Index | Type | Fields |
|-------|------|--------|
| `oid` | Unique | `oid_xxlink_mstr` |
| `pri` | Primary + Unique | `xxlink_type`, `xxlink_domain`, `xxlink_key`, `xxlink_seq` |

---

---

## xxshipd_det

Shipping detail records for requisition delivery information.

#### Fields

| Field | Type | Flags | Description |
|-------|------|:-----:|-------------|
| `xxshipd_transid` | char | i |  |
| `xxshipd_sequence` | inte | i |  |
| `xxshipd_weight_uom` | char |  |  |
| `xxshipd_dimension_uom` | char |  |  |
| `xxshipd_tracking` | char |  |  |
| `xxshipd_label` | blob |  |  |
| `xxshipd_weight` | char |  |  |
| `xxshipd_width` | char |  |  |
| `xxshipd_height` | char |  |  |
| `xxshipd_length` | char |  |  |

#### Indexes

| Index | Type | Fields |
|-------|------|--------|
| `pri` | Primary + Unique | `xxshipd_transid`, `xxshipd_sequence` |

---

## System Tables

*Application server configuration and audit logging.*

---

## appsrv_mstr

Application server (AppServer/PASOE) connection configuration for QAD domain integration.

#### Fields

| Field | Type | Flags | Description |
|-------|------|:-----:|-------------|
| `appsrv_domain` | char |  | Domain code |
| `appsrv_connect` | char |  | Connection string |
| `appsrv_cache` | logi |  | TRUE = cacheable |
| `oid_appsrv_mstr` | deci-2 | i |  |
| `appsrv_name` | char | i | AppServer name |
| `appsrv_proxy` | char |  |  |

#### Indexes

| Index | Type | Fields |
|-------|------|--------|
| `oid` | Unique | `oid_appsrv_mstr` |
| `pri` | Primary + Unique | `appsrv_name` |

---

---

## efw_audit

Enterprise framework audit trail tracking all database changes with before/after values.

#### Fields

| Field | Type | Flags | Description |
|-------|------|:-----:|-------------|
| `efw_audit_sequence` | inte | i |  |
| `efw_audit_action` | char | i |  |
| `efw_audit_table` | char | i |  |
| `efw_audit_key_value` | char | i |  |
| `efw_audit_userid` | char | i |  |
| `efw_audit_date` | date |  |  |
| `efw_audit_time` | inte |  |  |
| `efw_audit_datetime` | datetm | i |  |
| `efw_audit_datetime_tz` | datetm-tz |  |  |
| `efw_audit_domain` | char | i |  |
| `efw_audit_before_xml` | blob |  |  |
| `efw_audit_after_xml` | blob |  |  |
| `efw_audit_fields` | char |  |  |

#### Indexes

| Index | Type | Fields |
|-------|------|--------|
| `by_action` | - | `efw_audit_action` |
| `by_datetime` | - | `efw_audit_datetime` |
| `by_keyvalue` | - | `efw_audit_key_value` |
| `by_table` | - | `efw_audit_table` |
| `by_userid` | - | `efw_audit_userid` |
| `dom-seq` | Unique | `efw_audit_domain`, `efw_audit_sequence` |
| `keyvalue` | Unique | `efw_audit_domain`, `efw_audit_table`, `efw_audit_key_value`, `efw_audit_sequence` |
| `pri` | Primary + Unique | `efw_audit_sequence` |

---

## Related Documentation

| Document | Description |
|----------|-------------|
| [System Settings Reference](system-settings-reference.md) | 550+ `pf_mstr` configuration parameters |
| [Users and Groups](../admin/screens/01-users-and-groups.md) | User management screen documentation |
| [Approval Rules (Complex)](../admin/screens/ipurchase-01-approval-rules.md) | Complex AND/OR approval rule configuration |
| [Approval Rules (Simple)](../admin/screens/ipurchase-02-approval-rules-simple.md) | Simple AND-based approval rules |
| [Audit Trail](../admin/screens/04-audit-trail.md) | Database audit trail viewer |

---

*Generated from wdm.txt schema export*


---

> **Note for AI/RAG:** A verbose, AI-optimized version of this documentation exists at `rag-optimized/database-schema-rag.md`. If modifying this file, regenerate the RAG version using `python3 scripts/gen_schema_rag.py`.

---
