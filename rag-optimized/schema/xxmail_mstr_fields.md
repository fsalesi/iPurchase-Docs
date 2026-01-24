# xxmail_mstr - Email Queue Header Table - Fields

Email queue header records for outbound notifications. Tracks email status and delivery.

**Common questions this answers:**
- What fields are in the xxmail_mstr table?

**Related tables:** xxmaild_det (email details)

## Fields

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