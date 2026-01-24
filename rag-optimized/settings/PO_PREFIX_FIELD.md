# PO_PREFIX_FIELD - iPurchase System Setting

**Category:** Purchase Orders

Specifies which requisition field determines the PO number prefix, allowing different numbering schemes for different sites or entities.

### How It Works

This setting allows organizations to create distinct PO number sequences based on requisition data. Common uses include:
- Different PO prefixes for each site/location
- Separate sequences for different business entities
- Custom prefixes based on requisition type

**Example configurations:**

```sql
PO_PREFIX_FIELD = "Entity"     -- Use entity code as prefix
PO_PREFIX_FIELD = "xxreq_site" -- Use site field from req header
```

**Result:**
- Site 100 reqs → PO numbers: 100-00001, 100-00002, ...
- Site 200 reqs → PO numbers: 200-00001, 200-00002, ...

### Valid Values

- `Entity` - Use the entity code
- Any field name from the requisition header table (xxreq_mstr)

### Common Questions

- How do I have different PO number sequences per site?
- How do I add a prefix to PO numbers?
- Can different locations have separate PO numbering?

### Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | PO_PREFIX_FIELD |
| **Category** | Purchase Orders |
| **Owner** | Purchasing |
| **Default Value** | (none) |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'PO_PREFIX_FIELD'
```

### Related Settings

- [PO_NBR_USE_QAD](PO_NBR_USE_QAD.md) - Use QAD for PO number generation
