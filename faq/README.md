# iPurchase FAQ

Frequently asked questions organized by topic.

---

## Categories

- [Single Sign-On (SSO) Setup](sso-azure-setup.md) - Azure AD/Entra ID configuration
- [Requisition Rerouting](reroute-rules.md) - Why requisitions reroute and how to control it
- [Approvals](approvals.md) - Self-approval, escalation, delegation, emergency approvals
- [Change Orders](change-orders.md) - Change order behavior, tolerances, field monitoring
- [User Management](user-management.md) - Passwords, permissions, departments, groups
- [Purchase Orders](purchase-orders.md) - PO creation, printing, emailing, blankets
- [Requisition Entry](requisition-entry.md) - Types, defaults, accounts, required fields
- [System Settings](system-settings.md) - Domain-specific settings, value formats, naming patterns

---

## Quick Answers

### Why did my requisition reroute?
See [Requisition Rerouting](reroute-rules.md). Short answer: amount exceeded tolerance, approval simulation found different approvers, or a monitored field changed.

### How do I set up SSO with Azure?
See [SSO Azure Setup](sso-azure-setup.md) for step-by-step instructions.

### Can someone approve their own requisition?
Controlled by `USE_APP_AMOUNT_OWN_REQS` setting. See [Approvals FAQ](approvals.md#self-approval).

### Who can create change orders?
Controlled by `PO_UPDATE_GROUPS` setting (default: buyers). See [Change Orders FAQ](change-orders.md).

### How do I configure password policies?
See [User Management FAQ](user-management.md#passwords) for PASSWORD_RULES format.

### When is a PO created?
Immediately after buyer approval by default. See [Purchase Orders FAQ](purchase-orders.md).

### How do I restrict accounts by requisition type?
Use `RT_[TYPE]_ACCOUNT_RANGE` settings. See [Requisition Entry FAQ](requisition-entry.md#accountgl-configuration).

### What's the difference between req tolerances and change order tolerances?
- **Original Requisitions:** `ALLOWED_DOLLAR_INCREASE` / `ALLOWED_PERCENT_INCREASE`
- **Change Orders:** `PO_UPDATE_TOLERANCE_AMOUNT` / `PO_UPDATE_TOLERANCE_PCT`

See [Reroute Rules](reroute-rules.md) for details.

---

## See Also

- [Approval Strategy Guide](../reference/approval-strategy-guide.md) - Designing approval workflows
- [System Settings Reference](../reference/system-settings-reference.md) - Complete settings catalog
- [Can-Do List Format](../reference/can-do-list-format.md) - Pattern matching syntax

---

*Last Updated: January 2026*
