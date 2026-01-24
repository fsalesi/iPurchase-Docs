# DEFAULT_BLANKET_CYCLE - iPurchase System Setting

**Category:** System Configuration

After the administrator has added values to the CODE_LIST_H_BLANKET_CYCLE setting, they can add one of the values in that setting to this setting, to be the default value for the cycle code drop do...

**Common questions this answers:**
- What is DEFAULT_BLANKET_CYCLE?
- What does DEFAULT_BLANKET_CYCLE do?
- What is the default value for DEFAULT_BLANKET_CYCLE?
- How do I configure DEFAULT_BLANKET_CYCLE?

## Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | DEFAULT_BLANKET_CYCLE |
| **Category** | System Configuration |
| **Owner** | Purchasing |
| **Default Value** | (none) |

## How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'DEFAULT_BLANKET_CYCLE'
```
