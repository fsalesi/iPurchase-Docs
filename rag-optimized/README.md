# RAG-Optimized Documentation

This folder contains verbose, AI-friendly documentation optimized for vector search (RAG - Retrieval Augmented Generation).

## Purpose

The main documentation files (e.g., `reference/database-schema.md`, `reference/system-settings-reference.md`) are designed for human readability with clean, scannable tables.

These RAG-optimized versions split content into individual pages with added context to improve semantic search matching. Each page is designed to be a single chunk in the vector database.

## Structure

```
rag-optimized/
├── schema/                    # One file per database table
│   ├── xxapp_mstr_fields.md   # Table fields with context
│   ├── xxapp_mstr_indexes.md  # Table indexes
│   └── ...
├── settings/                  # One file per system setting
│   ├── MULTIPLE_APPROVALS.md
│   ├── AUTO_APPROVE_FORWARD.md
│   └── ...
└── README.md
```

## Maintenance

**IMPORTANT:** When you modify the source files, regenerate the RAG pages:

| Source File | RAG Folder | Regenerate Command |
|-------------|------------|-------------------|
| `reference/database-schema.md` | `rag-optimized/schema/` | `python3 scripts/gen_schema_pages.py` |
| `reference/system-settings-reference.md` | `rag-optimized/settings/` | `python3 scripts/gen_settings_pages.py` |

After regenerating, rebuild the vector index:
```bash
cd /home/frank/iassist-vectordb
python3 build_index.py
```

## File Counts

- Schema: 46 files (23 tables × 2: fields + indexes)
- Settings: 458 files (one per setting)

## Do Not Edit Directly

These files are generated. Edit the source files in `reference/` and regenerate.
