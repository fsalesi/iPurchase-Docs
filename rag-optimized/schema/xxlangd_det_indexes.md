# xxlangd_det - xxlangd_det Table - Indexes

Database indexes for the xxlangd_det table. Use these indexes for efficient queries.

**Common questions this answers:**
- What indexes exist on xxlangd_det?
- How do I query xxlangd_det efficiently?
- What is the primary key of xxlangd_det?

### Indexes

| Index | Type | Fields |
|-------|------|--------|
| `byform` | - | `xxlangd_form` |
| `bylang` | Primary + Unique | `xxlangd_lang`, `xxlangd_form`, `xxlangd_ref` |
| `bylang2` | - | `xxlangd_lang` |
| `byref` | - | `xxlangd_ref` |
| `bytext` | Word | `xxlangd_text` |
| `oid` | Unique | `oid_xxlangd_det` |