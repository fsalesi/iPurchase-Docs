# CATALOG_ACCESS_[Supplier NBR] - iPurchase System Setting

**Category:** Catalog & Vendors

Comma separated list of User ID's or Group ID's that have access to the specified supplier catalog. If this setting does not exist for a supplier, then everyone will have access to that supplier's catalog. The logic will ensure that only Suppliers that a user has access to will be allowed to be chosen in the catalog as well as in Requisition Line Maintenance (If manually ordering a catalog item)

### How It Works

This setting uses [Can-Do list format](../../reference/can-do-list-format.md) for specifying users and groups.

**Common patterns:**
- `*` - Everyone/all values allowed
- (blank) - No one/feature disabled
- `user1,user2` - Specific users only
- `group1,!user1` - Group members except specific user

### Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | CATALOG_ACCESS_[Supplier NBR] |
| **Category** | Catalog & Vendors |
| **Owner** | Admin |
| **Default Value** | (none) |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'CATALOG_ACCESS_[Supplier NBR]'
```