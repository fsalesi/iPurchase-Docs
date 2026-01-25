# efw_audit - efw_audit Table - Fields

Enterprise framework audit trail tracking all database changes with before/after values.

### Fields

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