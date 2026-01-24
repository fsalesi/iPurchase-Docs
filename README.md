# iPurchase Documentation

Comprehensive documentation for iPurchase and iApprove applications.

## Quick Links

- [INDEX.md](INDEX.md) - Raw GitHub links for AI assistants
- [System Settings Reference](reference/system-settings-reference.md#table-of-contents) - Complete catalog of 550+ settings by category

---

## Structure

```
├── admin/                  # Shared Administration (iPurchase + iApprove)
│   ├── screens/            # Admin screen documentation
│   ├── components/         # Reusable admin UI components
│   └── screenshots/        # Admin screen screenshots
│
├── reference/              # Reference materials
│   ├── system-settings-reference.md   # 550+ settings by category
│   └── system-settings-bible.csv      # Raw settings data
│
├── ipurchase/              # iPurchase End User Documentation (planned)
├── iapprove/               # iApprove Documentation (planned)
├── implementation/         # Implementation guides (planned)
├── functional/             # Business process documentation (planned)
└── technical/              # Database schemas, APIs (planned)
```

---

## Administration Screens (Shared)

Administration screens are shared between iPurchase and iApprove:

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
| 01 | [Workbench](admin/screens/iframework-01-workbench.md) | Development workbench | 🔜 Planned |
| 02 | [Menu Maintenance](admin/screens/iframework-02-menu-maintenance.md) | Navigation menu configuration | ✅ Complete |
| 03 | [VST Locks](admin/screens/iframework-03-vst-locks.md) | View locked database records (Developer) | ✅ Complete |
| 04 | [Compiler](admin/screens/iframework-04-compiler.md) | Code compilation (Developer) | ✅ Complete |
| 05 | [Query Tester](admin/screens/iframework-05-query-tester.md) | getData.p tester (Developer) | ✅ Complete |
| 06 | [Languages](admin/screens/iframework-06-languages.md) | Language and locale configuration | ✅ Complete |
| 07 | Custom Data | Custom data management (Developer) | 🔜 Planned |
| 08 | Translations | Translation management | 🔜 Planned |

---

## Admin Components

- [Admin Browse Grid](admin/components/admin-browse.md) - Standard data grid used across all admin screens

---

## Reference

### System Settings

- [System Settings Reference](reference/system-settings-reference.md#table-of-contents) - Complete catalog organized by category:
  - [Approval Workflow](reference/system-settings-reference.md#approval-workflow) (46 settings)
  - [Email Configuration](reference/system-settings-reference.md#email-configuration) (62 settings)
  - [Purchase Orders](reference/system-settings-reference.md#purchase-orders) (58 settings)
  - [Requisitions](reference/system-settings-reference.md#requisitions) (51 settings)
  - [User Management](reference/system-settings-reference.md#user-management) (45 settings)
  - [Security & Authentication](reference/system-settings-reference.md#security-and-authentication) (27 settings)
  - [Change Orders](reference/system-settings-reference.md#change-orders) (16 settings)
  - [And 18 more categories...](reference/system-settings-reference.md#table-of-contents)

### Quick Reference

- **Can-Do List Format**: See [Can-Do List Format](reference/can-do-list-format.md) - Pattern matching for permissions and filters
- **Setting Patterns**: `RT_[type]_*` for requisition type settings, `RT_[type][site]_*` for site-specific overrides
- **Environment Variables**: Set `TEST_SYSTEM=TRUE` on broker/PASOE for dev/test environments

---

## Database Tables

Key tables documented across screens:

| Table | Purpose | Primary Screen |
|-------|---------|----------------|
| `wus_mstr` | User master | Users and Groups |
| `wgr_mstr` | Group definitions | Users and Groups |
| `wugr_mstr` | User-group membership | Users and Groups |
| `pf_mstr` | System settings | System Settings |
| `efw_audit` | Audit trail | Audit Trail |
| `xxAppRule` | Complex approval rules | Approval Rules |
| `xxAppField` | Approval rule conditions | Approval Rules |
| `xxapp_mstr` | Simple approval rules | Approval Rules - Simple |

---

## Contributing

Documentation follows these conventions:

1. **Screen docs**: One markdown file per screen in `admin/screens/`
2. **Screenshots**: Stored in `admin/screenshots/{screen-name}/`
3. **Naming**: Use lowercase with hyphens, prefix iPurchase screens with `ipurchase-`
4. **Front matter**: Include screen_id, database_tables, related_screens
5. **Sections**: Overview, Access Path, Screenshots, Fields, Buttons, Business Rules, Related


