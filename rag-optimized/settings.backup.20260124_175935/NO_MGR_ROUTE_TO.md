# NO_MGR_ROUTE_TO - iPurchase System Setting

**Category:** Approval Workflow

User/group. Skip supervisor chain routing and route directly to this approver.

**Common questions this answers:**
- What is NO_MGR_ROUTE_TO?
- What does NO_MGR_ROUTE_TO do?
- What is the default value for NO_MGR_ROUTE_TO?
- How do I configure NO_MGR_ROUTE_TO?

## Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | NO_MGR_ROUTE_TO |
| **Category** | Approval Workflow |
| **Owner** | Admin |
| **Default Value** | (none) |

## How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'NO_MGR_ROUTE_TO'
```
