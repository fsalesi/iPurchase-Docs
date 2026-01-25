# iPurchase Documentation

Comprehensive documentation for iPurchase and iApprove applications.

## Quick Links

**For AI Assistants:**
- [INDEX.md](INDEX.md) - Raw GitHub links for AI assistants

**Reference:**
- [System Settings Reference](reference/system-settings-reference.md) - 550+ settings by category
- [Database Schema](reference/database-schema.md) - 23 core tables
- [Approval Strategy Guide](reference/approval-strategy-guide.md) - Designing approval rules
- [Can-Do List Format](reference/can-do-list-format.md) - Pattern matching syntax

**FAQ:**
- [FAQ Index](faq/README.md) - All frequently asked questions

---

## Structure

```
├── admin/                      # Shared Administration (iPurchase + iApprove)
│   ├── screens/                # Admin screen documentation
│   ├── components/             # Reusable admin UI components
│   └── screenshots/            # Admin screen screenshots
│
├── reference/                  # Reference materials (human-readable indexes)
│   ├── system-settings-reference.md   # 550+ settings by category (links to RAG)
│   ├── database-schema.md             # 23 tables (links to RAG)
│   ├── approval-systems.md            # Approval workflow logic
│   ├── approval-strategy-guide.md     # Designing approval rules
│   ├── admin-guide.md                 # Administrative procedures
│   └── can-do-list-format.md          # Pattern matching syntax
│
├── rag-optimized/              # AI-optimized chunked documentation
│   ├── settings/               # 550 individual setting files
│   ├── schema/                 # 48 table field/index files
│   ├── approvals/              # 15 approval topic files
│   ├── admin/                  # 8 admin topic files
│   └── can-do-list-format.md   # Can-Do syntax reference
│
├── faq/                        # Frequently Asked Questions
│   ├── general/                # General (all iFramework apps)
│   └── ipurchase/              # iPurchase-specific
│
├── scripts/                    # Documentation maintenance scripts
│   ├── regenerate-rag-docs.sh  # Regenerate RAG from reference docs
│   └── add-setting-links.py    # Add links to settings reference
│
├── ipurchase/                  # iPurchase End User Documentation (planned)
├── iapprove/                   # iApprove Documentation (planned)
├── implementation/             # Implementation guides (planned)
└── functional/                 # Business process documentation (planned)
```

---

## Administration Screens (Shared)

| # | Screen | Description | Status |
|---|--------|-------------|--------|
| 01 | [Users and Groups](admin/screens/01-users-and-groups.md) | User accounts, groups, permissions, delegation | ✅ Complete |
| 02 | [System Settings](admin/screens/02-system-settings.md) | System-wide configuration (pf_mstr) | ✅ Complete |
| 03 | [Jobs](admin/screens/03-jobs.md) | Background job scheduling and monitoring | ✅ Complete |
| 04 | [Audit Trail](admin/screens/04-audit-trail.md) | Track database changes by user and date | ✅ Complete |
| 05 | [Requisition Audit Trail](admin/screens/05-requisition-audit-trail.md) | Requisition workflow history | 📝 Placeholder |
| 06 | [Group Report](admin/screens/06-group-report.md) | Export user/group membership for auditors | ✅ Complete |
| 07 | [eMail Queue](admin/screens/07-email-queue.md) | Outbound email queue and log | ✅ Complete |
| 08 | [Security](admin/screens/08-security.md) | Password policies and authentication | 📝 Placeholder |
| 09 | [AppSrvr Configuration](admin/screens/09-appsrvr-configuration.md) | QAD domain connections via ISS Connector | ✅ Complete |
| 10 | [AppSrvr Caching](admin/screens/10-appsrvr-caching.md) | Cache settings for QAD data (legacy) | ✅ Complete |

---

## iPurchase Configuration Screens

| # | Screen | Description | Status |
|---|--------|-------------|--------|
| 01 | [Approval Rules (Complex)](admin/screens/ipurchase-01-approval-rules.md) | AND/OR conditional approval routing | ✅ Complete |
| 02 | [Approval Rules - Simple](admin/screens/ipurchase-02-approval-rules-simple.md) | Straightforward AND-based approval rules | ✅ Complete |
| 03 | [User Roles](admin/screens/ipurchase-03-user-roles.md) | Role-based approvers (Manager, Director, VP, etc.) | ✅ Complete |
| 04 | [Supplier Maintenance](admin/screens/ipurchase-04-supplier-maintenance.md) | Vendor catalog and punchout configuration | ✅ Complete |
| 05 | [UNSPSC Maintenance](admin/screens/ipurchase-05-unspsc-maintenance.md) | Commodity code management | ✅ Complete |
| 06 | [UNSPSC Accounts](admin/screens/ipurchase-06-unspsc-accounts.md) | UNSPSC to GL account mapping | ✅ Complete |
| 07 | [Supplier Location Maintenance](admin/screens/ipurchase-07-supplier-location-maintenance.md) | Default receiving locations by supplier/site | ✅ Complete |
| 08 | [Supervisor Chart](admin/screens/ipurchase-08-supervisor-chart.md) | Org chart from supervisor relationships | ✅ Complete |
| 09 | [Approval Report](admin/screens/ipurchase-09-approval-report.md) | Audit report of all approval rules | ✅ Complete |
| 10 | [PO Number Prefix](admin/screens/ipurchase-10-po-number-prefix.md) | Enhanced PO numbering with multiple sequences | ✅ Complete |

---

## iFramework Configuration Screens

| # | Screen | Description | Status |
|---|--------|-------------|--------|
| 01 | [Workbench](admin/screens/iframework-01-workbench.md) | Full development/troubleshooting environment (ISS Only) | ✅ Complete |
| 02 | [Menu Maintenance](admin/screens/iframework-02-menu-maintenance.md) | Navigation menu configuration | ✅ Complete |
| 03 | [VST Locks](admin/screens/iframework-03-vst-locks.md) | View locked database records (Developer) | ✅ Complete |
| 04 | [Compiler](admin/screens/iframework-04-compiler.md) | Code compilation (Developer) | ✅ Complete |
| 05 | [Query Tester](admin/screens/iframework-05-query-tester.md) | getData.p tester (Developer) | ✅ Complete |
| 06 | [Languages](admin/screens/iframework-06-languages.md) | Language and locale configuration | ✅ Complete |
| 07 | Custom Data | Custom data management (Developer) | 🔜 Planned |
| 08 | [Translations](admin/screens/iframework-08-translations.md) | UI text translations by language | ✅ Complete |

---

## RAG-Optimized Documentation

The `rag-optimized/` folder contains AI-optimized documentation with single-chunk retrieval:

| Folder | Files | Content |
|--------|-------|---------|
| `settings/` | 550 | Individual system setting documentation |
| `schema/` | 48 | Database table fields and indexes |
| `approvals/` | 15 | Approval workflow topics |
| `admin/` | 8 | Administration topics |

**Maintenance:**
- Run `./scripts/regenerate-rag-docs.sh` when reference docs change
- Update `rag-optimized/schema/` when database schema changes
- Update `rag-optimized/settings/` when adding new settings

---

## Reference Documents

- [Database Schema](reference/database-schema.md) - Index of 23 tables (links to RAG files)
- [System Settings Reference](reference/system-settings-reference.md) - 550+ settings (links to RAG files)
- [Approval Systems](reference/approval-systems.md) - Technical approval workflow logic
- [Approval Strategy Guide](reference/approval-strategy-guide.md) - Practical implementation guide
- [Admin Guide](reference/admin-guide.md) - Administrative procedures
- [Can-Do List Format](reference/can-do-list-format.md) - Pattern matching syntax

---

## FAQ

- [FAQ Index](faq/README.md)

**General:**
- [SSO Azure Setup](faq/general/sso-azure-setup.md) - Azure AD/Entra ID configuration
- [System Settings](faq/general/system-settings.md) - Domain-specific settings
- [User Management](faq/general/user-management.md) - Passwords, permissions, groups

**iPurchase:**
- [Approvals](faq/ipurchase/approvals.md) - Self-approval, escalation, delegation
- [Change Orders](faq/ipurchase/change-orders.md) - Tolerances, field monitoring
- [Purchase Orders](faq/ipurchase/purchase-orders.md) - PO creation, printing, emailing
- [Requisition Entry](faq/ipurchase/requisition-entry.md) - Types, defaults, accounts
- [Requisition Rerouting](faq/ipurchase/reroute-rules.md) - Why requisitions reroute
