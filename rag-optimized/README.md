# RAG-Optimized Documentation

This folder contains verbose, AI-friendly versions of reference documentation optimized for vector search (RAG - Retrieval Augmented Generation).

## Purpose

The main documentation files (e.g., `reference/database-schema.md`, `reference/system-settings-reference.md`) are designed for human readability with clean, scannable tables.

These RAG-optimized versions add verbose context around each item to improve semantic search matching. The extra context helps the AI assistant find the right information when users ask natural language questions.

## Files

- `database-schema-rag.md` - Verbose version of database table documentation
- `system-settings-rag.md` - Verbose version of system settings documentation

## Maintenance

**IMPORTANT:** When you modify the source files, regenerate the RAG versions:

| Source File | RAG Version | Regenerate Command |
|-------------|-------------|-------------------|
| `reference/database-schema.md` | `rag-optimized/database-schema-rag.md` | `python3 scripts/gen_schema_rag.py` |
| `reference/system-settings-reference.md` | `rag-optimized/system-settings-rag.md` | `python3 scripts/gen_settings_rag.py` |

After regenerating, rebuild the vector index:
```bash
cd /home/frank/iassist-vectordb
python3 build_index.py
```

## Do Not Edit Directly

These files are generated. Edit the source files instead and regenerate.
