# FAQ

Frequently asked questions organized by topic.

---

## General (All Apps)

These FAQs apply to all iFramework-based applications.

- [Single Sign-On (SSO) Setup](general/sso-azure-setup.md) - Azure AD/Entra ID configuration
- [System Settings](general/system-settings.md) - Domain-specific settings, value formats
- [User Management](general/user-management.md) - Passwords, permissions, departments, groups

---

## iPurchase

These FAQs are specific to iPurchase.

- [System Settings (iPurchase)](general/system-settings.md#ipurchase-specific) - CODE_LIST, RT_ settings, naming patterns
- [Approvals](ipurchase/approvals.md) - Self-approval, escalation, delegation, emergency approvals
- [Change Orders](ipurchase/change-orders.md) - Change order behavior, tolerances, field monitoring
- [Purchase Orders](ipurchase/purchase-orders.md) - PO creation, printing, emailing, blankets
- [Requisition Entry](ipurchase/requisition-entry.md) - Types, defaults, accounts, required fields
- [Requisition Rerouting](ipurchase/reroute-rules.md) - Why requisitions reroute and how to control it

---

## Quick Answers

### Why did my requisition reroute?
See [Requisition Rerouting](ipurchase/reroute-rules.md). Short answer: amount exceeded tolerance, approval simulation found different approvers, or a monitored field changed.

### How do I set up SSO with Azure?
See [SSO Azure Setup](general/sso-azure-setup.md) for step-by-step instructions.

### Can someone approve their own requisition?
Controlled by `USE_APP_AMOUNT_OWN_REQS` setting. See [Approvals FAQ](ipurchase/approvals.md#self-approval).

### How do I configure drop-down lists?
See [System Settings FAQ - CODE_LIST](general/system-settings.md#drop-down-list-settings-code_list).

### Can I have different settings per domain?
Yes! See [System Settings FAQ - Domain-Specific](general/system-settings.md#domain-specific-settings).

### How do I configure password policies?
See [User Management FAQ](general/user-management.md#passwords) for PASSWORD_RULES format.

---

## See Also

- [Approval Strategy Guide](../reference/approval-strategy-guide.md) - Designing approval workflows
- [System Settings Reference](../reference/system-settings-reference.md) - Complete settings catalog

---

*Last Updated: January 2026*
