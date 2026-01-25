# xxreq_audit - Requisition Approval Audit Trail Table - Fields

Records all approval actions taken on requisitions. Shows who approved/rejected, when, and any comments. Critical for audit compliance and workflow analysis.

**Common questions this answers:**
- What fields are in the xxreq_audit table?
- What fields are in the approval audit table?
- What is the approval history?
- What is xxreq_actual_approver vs xxreq_app_id?

**Related tables:** xxreq_mstr (requisition), xxapp_mstr (rules), wus_mstr (users)

### Fields

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