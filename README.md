# iPurchase Documentation

User and administrator documentation for iPurchase procurement system.

## Structure

```
ipurchase-docs/
├── screens/          # Screen-by-screen documentation
├── components/       # Reusable UI component documentation
├── workflows/        # Business process workflows
├── technical/        # Technical reference (database, API, etc.)
└── screenshots/      # Screenshots organized by topic
    ├── users-and-groups/
    └── components/
```

## Screens

| Screen | Description | Status |
|--------|-------------|--------|
| [Users and Groups](screens/01-users-and-groups.md) | User account management, groups, permissions | ✅ Complete |

## Components

Reusable UI components that appear across multiple screens:

| Component | Description |
|-----------|-------------|
| [Admin Browse Grid](components/admin-browse.md) | Standard data grid with search, sort, export |

## Contributing

When documenting a new screen:

1. Create the markdown file in `screens/` with naming convention `NN-screen-name.md`
2. Add screenshots to `screenshots/screen-name/`
3. Reference shared components rather than duplicating documentation
4. Include database field mappings for all UI fields
5. Document business rules and common issues

## Database Reference

iPurchase uses OpenEdge/Progress databases:
- **wdm** - iPurchase application database
- **mfg** - QAD ERP database

See the [MCP technical schema](../mcp/docs/technical-schema.md) for complete database documentation.
