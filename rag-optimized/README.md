# RAG-Optimized Documentation

This folder contains AI-friendly documentation optimized for vector search (RAG - Retrieval Augmented Generation).

## Purpose

The main documentation files in `reference/` are designed for human readability with tables and navigation.

These RAG-optimized versions use `###` headers (not `##`) so each file remains a single chunk in the vector database. Each page includes added context to improve semantic search matching.

## Structure

```
rag-optimized/
├── schema/                    # 48 files - Database tables
│   ├── xxapp_mstr_fields.md   # Table fields with descriptions
│   ├── xxapp_mstr_indexes.md  # Table indexes
│   └── ...
├── settings/                  # 550 files - System settings
│   ├── MULTIPLE_APPROVALS.md
│   ├── AUTO_APPROVE_FORWARD.md
│   └── ...
├── approvals/                 # 15 files - Approval workflow topics
│   ├── simple-rules.md
│   ├── complex-rules.md
│   ├── supervisor-chain.md
│   └── ...
├── admin/                     # 8 files - Administration topics
│   ├── user-management.md
│   ├── approval-rules-setup.md
│   └── ...
├── can-do-list-format.md      # Can-Do pattern matching syntax
└── README.md
```

## File Counts

| Folder | Files | Source |
|--------|-------|--------|
| `schema/` | 48 | Database schema export |
| `settings/` | 550 | System settings catalog |
| `approvals/` | 15 | approval-systems.md + approval-strategy-guide.md |
| `admin/` | 8 | admin-guide.md |

## Maintenance

### When Reference Docs Change

Run the regeneration script:
```bash
./scripts/regenerate-rag-docs.sh
```

This updates:
- `rag-optimized/approvals/` from `reference/approval-*.md`
- `rag-optimized/admin/` from `reference/admin-guide.md`
- `rag-optimized/can-do-list-format.md` from `reference/can-do-list-format.md`

### When Database Schema Changes

Manually update files in `rag-optimized/schema/`

### When System Settings Change

1. Manually update/add files in `rag-optimized/settings/`
2. Run `python3 scripts/add-setting-links.py` to update reference doc links

## Header Format

All files use `###` headers (not `##`) to ensure single-chunk retrieval:

```markdown
# Title - iPurchase

**Purpose:** Brief description

### Section 1
Content...

### Section 2
Content...
```

## Do Not Edit Schema/Settings Directly

The `schema/` and `settings/` files are generated. For approval and admin topics, source files are in `reference/` - edit those and regenerate.
