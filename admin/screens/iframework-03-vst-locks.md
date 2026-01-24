---
screen_id: iframework_vst_locks
screen_name: VST Locks
module: iFramework
access_level: Developer
database_tables:
  - _Lock (VST)
screenshot: ../screenshots/iframework-vst-locks/01-main-screen.png
last_updated: 2025-01-24
author: Frank Salesi
---

# VST Locks

## Overview

VST Locks displays currently locked records in the OpenEdge database. This is a developer/troubleshooting tool used to identify record locking issues that may be causing user conflicts or performance problems.

**Note:** This is a developer tool. Most iFramework menu items are geared towards developers except for Menu Maintenance and Languages/Translations.

## Access Path

iFramework → VST Locks

## Screenshot

![VST Locks](../screenshots/iframework-vst-locks/01-main-screen.png)

---

## Search Criteria

| Field | Description |
|-------|-------------|
| **Database** | Select database to check (wdm, mfg, etc.) |

Click **Search** to query the `_Lock` virtual system table.

---

## Browse Columns

| Column | Description |
|--------|-------------|
| _Lock-Id | Unique lock identifier |
| Name | User/process name holding the lock |
| Usr | User number |
| Table | Table name with locked record |
| Flags | Lock type flags |
| RECID | Record ID of locked record |
| File-Name | Database file name |
| Pid | Process ID |

---

## Use Cases

- **Troubleshooting** - Identify why users are getting "record in use" errors
- **Performance issues** - Find long-running locks blocking other users
- **Deadlock analysis** - Investigate potential deadlock situations
- **Before maintenance** - Verify no active locks before database operations

---

## Tips

1. **No Data Available** is good - means no current locks
2. **Persistent locks** may indicate a hung process
3. **Check Pid** - Can help identify which server process holds the lock
