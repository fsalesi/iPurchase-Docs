# pf_mstr - Parameter/Settings Master Table - Fields

Stores all system settings, user preferences, and configuration parameters. The central configuration table for iPurchase. Query with pf_us_id='SYSTEM' and pf_group='DEFAULT' for system settings.

**Common questions this answers:**
- What fields are in the pf_mstr table?
- What fields are in the settings table?
- What is pf_chr1?

**Related tables:** System Settings Reference documentation

## Fields

| Field | Type | Flags | Description |
|-------|------|:-----:|-------------|
| `pf_us_id` | char | im | User ID or "SYSTEM" for global |
| `pf_attr` | char | im | Setting name/attribute |
| `pf_value` | char | i |  |
| `pf_alt_value` | char | i |  |
| `pf_date1` | date |  |  |
| `pf_date2` | date |  |  |
| `pf_log1` | logi |  | Boolean value |
| `pf_log2` | logi |  |  |
| `pf_dec1` | deci-2 |  | Decimal value |
| `pf_dec2` | deci-2 |  |  |
| `pf_group` | char | i | Setting group (usually "DEFAULT") |
| `pf_seq` | deci-3 | i |  |
| `pf_chr1` | char |  | Setting value (string) |
| `pf_chr2` | char |  | Secondary value |
| `pf_data_version` | deci-2 |  |  |
| `pf_default` | char |  |  |
| `pf_help` | char |  | Help text / description |
| `pf_notes` | char |  |  |