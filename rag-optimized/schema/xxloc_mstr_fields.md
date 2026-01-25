# xxloc_mstr - Location Master Table - Fields

Location/site master defining valid ship-to and bill-to locations for requisitions.

**Common questions this answers:**
- What fields are in the xxloc_mstr table?
- What fields are in the location table?

**Related tables:** xxreq_mstr (requisitions)

### Fields

| Field | Type | Flags | Description |
|-------|------|:-----:|-------------|
| `oid_xxloc_mstr` | deci | i |  |
| `xxloc_has_notes` | logi |  |  |
| `xxloc_has_attachments` | logi |  |  |
| `xxloc_domain` | char | i |  |
| `xxloc_supplier` | char | i |  |
| `xxloc_site` | char | i |  |
| `xxloc_location` | char |  |  |