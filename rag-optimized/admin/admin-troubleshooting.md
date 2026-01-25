# Administrator Troubleshooting - iPurchase

**Purpose:** Common administrative issues and how to resolve them.

### Database Queries

**Find Pending Requisitions:**
```sql
SELECT xxreq_nbr, xxreq_userid, xxreq_obo, xxreq_entry_date, xxreq_cost_gl
FROM PUB.xxreq_mstr
WHERE xxreq_status = 'CONFIRMED'
ORDER BY xxreq_entry_date DESC
```

**Find Approval Bottlenecks:**
```sql
SELECT a.xxreq_app_id, COUNT(*) as pending_count
FROM PUB.xxreq_audit a
JOIN PUB.xxreq_mstr r ON a.xxreq_nbr = r.xxreq_nbr
WHERE r.xxreq_status = 'CONFIRMED'
  AND a.xxreq_status IS NULL
GROUP BY a.xxreq_app_id
ORDER BY pending_count DESC
```

**Find Change Orders:**
```sql
SELECT xxreq_nbr, xxreq_userid, xxreq_entry_date, xxreq_cost_gl, 
       xxreq_mat_change, xxreq_update_po_tolerance
FROM PUB.xxreq_mstr
WHERE xxreq_update_po = TRUE
ORDER BY xxreq_entry_date DESC
```

**Find Active Delegates:**
```sql
SELECT wus_id, wus_name, wus_delegate
FROM PUB.wus_mstr
WHERE wus_delegate IS NOT NULL
  AND wus_delegate != ''
```

### Common Problems

**Problem: Requisition not routing correctly**
**Solution:**
1. Check approval simulation - who SHOULD approve?
2. Check actual routing in xxreq_audit
3. Compare expected vs actual
4. Review rule conditions - do they all match?
5. Check for stop conditions blocking later rules

**Problem: Change order going to full approval when shouldn't**
**Solution:**
1. Check tolerance settings (amount and percentage)
2. Verify fields changed (CO_HEADER/ITEM_REROUTE_FIELDS)
3. Check if new lines added (CO_ITEM_REROUTE_NEW)
4. Verify approval hierarchy hasn't changed
5. Check material change flag in xxreq_mstr

**Problem: User can't submit requisition**
**Solution:**
1. Check ALLOW_REQ_ENTRY permission
2. Look for validation rule errors (MESSAGE: rules)
3. Verify required fields populated
4. Check for supervisor chain issues (no supervisor with sufficient limit)

**Problem: Delegation not working**
**Solution:**
1. Verify wus_delegate field is set
2. Check OOF settings (LIMIT_BY_DOLLARS, LIMIT_BY_DEPT, etc.)
3. Look for delegation chains (USE_CHAINED_DELEGATES)
4. Verify delegate has system access
