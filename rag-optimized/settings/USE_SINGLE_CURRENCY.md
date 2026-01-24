# USE_SINGLE_CURRENCY - iPurchase System Setting

**Category:** EAM Integration

Forces single currency mode, disabling multi-currency functionality.

### Valid Values

| Value | Behavior |
|-------|----------|
| **TRUE** | Single currency only - multi-currency disabled |
| **FALSE** | Multi-currency enabled (DEFAULT) |

### How It Works

iPurchase supports multi-currency requisitions where different lines can use different currencies. This setting allows organizations to simplify the system by forcing all transactions to use a single currency.

**TRUE (Single currency):**
- Currency fields hidden or locked
- All transactions in base currency
- Simpler user experience
- No exchange rate management needed

**FALSE (Multi-currency):**
- Currency selection available on requisitions
- Exchange rates applied for GL currency conversion
- Required for international purchasing
- Uses `xxreq_cost_gl` for approval thresholds

### Common Questions

- How do I disable multi-currency in iPurchase?
- Can I force all requisitions to use one currency?
- Why can't I select a currency on my requisition?

### Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | USE_SINGLE_CURRENCY |
| **Category** | EAM Integration |
| **Owner** | Finance |
| **Default Value** | FALSE |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'USE_SINGLE_CURRENCY'
```
