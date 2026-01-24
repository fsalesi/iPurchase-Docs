# DEFAULT_BUYER - iPurchase System Setting

**Category:** Purchase Orders

Specifies the default buyer assigned to new requisitions. Can be overridden at multiple levels including by site, requisition type, or vendor.

### How It Works

When a new requisition is created, this buyer is automatically assigned. The assignment can be overridden by more specific settings in this order:
1. Vendor buyer (vd_buyer)
2. RT_[TYPE]_[SITE]_DEFAULT_BUYER
3. RT_[TYPE]_DEFAULT_BUYER
4. DEFAULT_BUYER_[SITE]
5. DEFAULT_BUYER (this setting)

### Valid Values

| Value | Behavior |
|-------|----------|
| User ID | Buyer's user ID to assign |
| Blank | No default buyer assigned |

### Common Questions

- What is DEFAULT_BUYER?
- How do I set the default buyer?
- Why is a different buyer being assigned?
- How do site-specific buyers work?

### Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | DEFAULT_BUYER |
| **Category** | Purchase Orders |
| **Owner** | Purchasing |
| **Default Value** | (none) |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'DEFAULT_BUYER'
```

### Related Settings

- DEFAULT_BUYER_[SITE] - Site-specific default buyer
- RT_[TYPE]_DEFAULT_BUYER - Type-specific default buyer
