# iPurchase Database Schema Reference

> Index of table definitions for iPurchase. Click any table to view detailed field and index documentation.
>
> See also: [System Settings Reference](system-settings-reference.md) for 550+ configuration parameters.

| | |
|--|--|
| **Database** | `wdm` (PROGRESS/OpenEdge) |
| **Tables Documented** | 23 |

---

## Core Tables

User management, groups, and system configuration.

| Table | Description | Documentation |
|-------|-------------|---------------|
| **wus_mstr** | User profiles, credentials, approval limits, supervisor relationships | [Fields](../rag-optimized/schema/wus_mstr_fields.md) ∙ [Indexes](../rag-optimized/schema/wus_mstr_indexes.md) |
| **wgr_mstr** | Group definitions for organizing users | [Fields](../rag-optimized/schema/wgr_mstr_fields.md) ∙ [Indexes](../rag-optimized/schema/wgr_mstr_indexes.md) |
| **wugr_mstr** | User-to-group membership mapping | [Fields](../rag-optimized/schema/wugr_mstr_fields.md) ∙ [Indexes](../rag-optimized/schema/wugr_mstr_indexes.md) |
| **pf_mstr** | System settings and configuration parameters | [Fields](../rag-optimized/schema/pf_mstr_fields.md) ∙ [Indexes](../rag-optimized/schema/pf_mstr_indexes.md) |

## Requisition Tables

Requisition headers, line items, approvals, and attachments.

| Table | Description | Documentation |
|-------|-------------|---------------|
| **xxreq_mstr** | Requisition header - status, dates, totals, vendor, buyer, workflow state | [Fields](../rag-optimized/schema/xxreq_mstr_fields.md) ∙ [Indexes](../rag-optimized/schema/xxreq_mstr_indexes.md) |
| **xxreqd_det** | Requisition line items - quantities, costs, GL coding, descriptions | [Fields](../rag-optimized/schema/xxreqd_det_fields.md) ∙ [Indexes](../rag-optimized/schema/xxreqd_det_indexes.md) |
| **xxreq_audit** | Approval audit trail - who approved/rejected, when, comments | [Fields](../rag-optimized/schema/xxreq_audit_fields.md) ∙ [Indexes](../rag-optimized/schema/xxreq_audit_indexes.md) |
| **xxreq_attach** | File attachments linked to requisitions | [Fields](../rag-optimized/schema/xxreq_attach_fields.md) ∙ [Indexes](../rag-optimized/schema/xxreq_attach_indexes.md) |

## Approval Tables

Approval rule definitions and conditions.

| Table | Description | Documentation |
|-------|-------------|---------------|
| **xxapp_mstr** | Simple approval rules (AND logic only) | [Fields](../rag-optimized/schema/xxapp_mstr_fields.md) ∙ [Indexes](../rag-optimized/schema/xxapp_mstr_indexes.md) |
| **xxAppRule** | Complex approval rule headers (AND/OR logic) | [Fields](../rag-optimized/schema/xxAppRule_fields.md) ∙ [Indexes](../rag-optimized/schema/xxAppRule_indexes.md) |
| **xxAppField** | Approval rule conditions (hierarchical tree) | [Fields](../rag-optimized/schema/xxAppField_fields.md) ∙ [Indexes](../rag-optimized/schema/xxAppField_indexes.md) |

## Archive & Attachment Tables

Document storage and email attachments.

| Table | Description | Documentation |
|-------|-------------|---------------|
| **xxpo_archive** | Archived PO PDF documents (BLOB storage) | [Fields](../rag-optimized/schema/xxpo_archive_fields.md) ∙ [Indexes](../rag-optimized/schema/xxpo_archive_indexes.md) |
| **xxnote_mstr** | Notes and comments with optional attachments | [Fields](../rag-optimized/schema/xxnote_mstr_fields.md) ∙ [Indexes](../rag-optimized/schema/xxnote_mstr_indexes.md) |
| **xxmaild_det** | Email detail records including attachments | [Fields](../rag-optimized/schema/xxmaild_det_fields.md) ∙ [Indexes](../rag-optimized/schema/xxmaild_det_indexes.md) |

## Configuration Tables

Locations, roles, languages, and interface settings.

| Table | Description | Documentation |
|-------|-------------|---------------|
| **xxloc_mstr** | Location/site master - ship-to and bill-to addresses | [Fields](../rag-optimized/schema/xxloc_mstr_fields.md) ∙ [Indexes](../rag-optimized/schema/xxloc_mstr_indexes.md) |
| **xxrole_mstr** | Role definitions (Manager, Director, VP, etc.) | [Fields](../rag-optimized/schema/xxrole_mstr_fields.md) ∙ [Indexes](../rag-optimized/schema/xxrole_mstr_indexes.md) |
| **xxlang_mstr** | Language definitions for multi-language support | [Fields](../rag-optimized/schema/xxlang_mstr_fields.md) ∙ [Indexes](../rag-optimized/schema/xxlang_mstr_indexes.md) |
| **xxlangd_det** | Language detail records - locale-specific settings | [Fields](../rag-optimized/schema/xxlangd_det_fields.md) ∙ [Indexes](../rag-optimized/schema/xxlangd_det_indexes.md) |
| **xxmail_mstr** | Email queue headers for outbound notifications | [Fields](../rag-optimized/schema/xxmail_mstr_fields.md) ∙ [Indexes](../rag-optimized/schema/xxmail_mstr_indexes.md) |
| **xxlink_mstr** | Configurable links in iPurchase interface | [Fields](../rag-optimized/schema/xxlink_mstr_fields.md) ∙ [Indexes](../rag-optimized/schema/xxlink_mstr_indexes.md) |
| **xxshipd_det** | Shipping detail for requisition delivery | [Fields](../rag-optimized/schema/xxshipd_det_fields.md) ∙ [Indexes](../rag-optimized/schema/xxshipd_det_indexes.md) |

## System Tables

Application server config and audit logging.

| Table | Description | Documentation |
|-------|-------------|---------------|
| **appsrv_mstr** | AppServer/PASOE connection configuration | [Fields](../rag-optimized/schema/appsrv_mstr_fields.md) ∙ [Indexes](../rag-optimized/schema/appsrv_mstr_indexes.md) |
| **efw_audit** | Enterprise framework audit trail - all DB changes | [Fields](../rag-optimized/schema/efw_audit_fields.md) ∙ [Indexes](../rag-optimized/schema/efw_audit_indexes.md) |

---

## Field Flags Reference

| Flag | Meaning |
|:----:|---------:|
| `i` | Indexed - field is part of an index |
| `m` | Mandatory - field requires a value |
| `c` | Case sensitive |

---

## Quick Links

- **User data**: [wus_mstr](../rag-optimized/schema/wus_mstr_fields.md) (users), [wgr_mstr](../rag-optimized/schema/wgr_mstr_fields.md) (groups), [wugr_mstr](../rag-optimized/schema/wugr_mstr_fields.md) (membership)
- **Requisitions**: [xxreq_mstr](../rag-optimized/schema/xxreq_mstr_fields.md) (header), [xxreqd_det](../rag-optimized/schema/xxreqd_det_fields.md) (lines), [xxreq_audit](../rag-optimized/schema/xxreq_audit_fields.md) (approvals)
- **Approval rules**: [xxapp_mstr](../rag-optimized/schema/xxapp_mstr_fields.md) (simple), [xxAppRule](../rag-optimized/schema/xxAppRule_fields.md) (complex)
- **Settings**: [pf_mstr](../rag-optimized/schema/pf_mstr_fields.md) or [System Settings Reference](system-settings-reference.md)
