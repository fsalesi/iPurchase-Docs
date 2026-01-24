# DEFAULT_SUB_ACCOUNT - iPurchase System Setting

**Category:** GL Accounts & Finance

The default sub account is used when creating requisition from catalogs and punchouts. The order in which iPurchase determines the sub account for a requisition created from a Punchout or Catalog is as follows: First it checks if an account or sub-account is setup for the UNSPSC code being ordered. If one is found then those are assigned. If none are found then it will use the Default_Account value (described above), and the setting in this Default_Sub_Account value. Lastly, if there are overrides at the requisition level (the codes which start "RT" below) then those are used and will override the UNSPSC settings.

### How It Works

See the description above for details on how this setting affects system behavior.

### Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | DEFAULT_SUB_ACCOUNT |
| **Category** | GL Accounts & Finance |
| **Owner** | Finance |
| **Default Value** | (none) |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'DEFAULT_SUB_ACCOUNT'
```