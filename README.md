# iPurchase Documentation

Comprehensive documentation for iPurchase and iApprove applications.

## Structure

```
├── admin/                  # Shared Administration (iPurchase + iApprove)
│   ├── screens/            # Admin screen documentation
│   ├── components/         # Reusable admin UI components
│   └── screenshots/        # Admin screen screenshots
│
├── ipurchase/              # iPurchase End User Documentation
│   ├── screens/            # User-facing screen documentation
│   ├── components/         # Reusable user UI components
│   └── screenshots/        # User screen screenshots
│
├── iapprove/               # iApprove Documentation (by module)
│
├── implementation/         # Implementation guides
│
├── functional/             # Business process documentation
│
├── technical/              # Database schemas, APIs
│
└── reference/              # Quick reference materials
```

## Admin Screens (Shared)

Administration screens are shared between iPurchase and iApprove:

- [Users and Groups](admin/screens/01-users-and-groups.md) - User account management, groups, permissions
- [System Settings](admin/screens/02-system-settings.md) - System-wide configuration (550+ settings)
- [Jobs](admin/screens/03-jobs.md) - Background job scheduling and monitoring
- [Audit Trail](admin/screens/04-audit-trail.md) - Track all database changes by user and date
- [Requisition Audit Trail](admin/screens/05-requisition-audit-trail.md) - Requisition workflow history (placeholder)

### Admin Components

- [Admin Browse Grid](admin/components/admin-browse.md) - Standard data grid used across all admin screens

## iPurchase User Screens

*(Documentation in progress)*

## iApprove Modules

*(Documentation in progress)*

## Quick Reference

- **Can-Do List Format**: Comma-separated values, `!` for exclusion, `*` for wildcard, left-to-right evaluation
- **Setting Patterns**: `RT_[type]_*` for requisition type settings, `RT_[type][site]_*` for site-specific
