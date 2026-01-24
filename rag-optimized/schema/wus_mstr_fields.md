# wus_mstr - User Master Table - Fields

Stores all user accounts, profiles, and settings for iPurchase. Contains login credentials, approval limits, supervisor relationships, delegates, and user preferences.

**Common questions this answers:**
- What fields are in the wus_mstr table?
- What fields are in the user master table?
- What is wus_delegate?
- What is the user ID field?

**Related tables:** wgr_mstr (groups), wugr_mstr (group membership), pf_mstr (user preferences)

## Fields

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