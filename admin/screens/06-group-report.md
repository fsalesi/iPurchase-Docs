---
screen_id: group_report
screen_name: Group Report
module: Administration
access_level: Administrator
database_tables:
  - wgr_mstr
  - wugr_mstr
  - wus_mstr
related_screens:
  - users_and_groups
last_updated: 2025-01-23
author: Frank Salesi
---

# Group Report

## Overview

The Group Report exports a complete list of all users and their group memberships to Excel format. This report is commonly requested by auditors as part of quarterly access reviews and compliance procedures.

## Access Path

Administration → Group Report

## Output

Clicking Group Report immediately generates and downloads an Excel file. There is no screen or configuration options.

## Report Columns

| Column | Source | Description |
|--------|--------|-------------|
| Group Code | wgr_mstr.wgr_id | Group identifier |
| Group Name | wgr_mstr.wgr_desc | Group description |
| User Id | wus_mstr.wus_id | User identifier |
| User Name | wus_mstr.wus_name | Full name |
| Title | wus_mstr.wus_title | Job title |
| Company | wus_mstr.wus_company | Company name |
| Email | wus_mstr.wus_email | Email address |
| Created on | wus_mstr.wus_created_date | Account creation date |
| Created By | wus_mstr.wus_created_by | Who created the account |
| Disabled | wus_mstr.wus_disable | Whether account is disabled |
| Password Expire Date | wus_mstr.wus_pwd_expire | When password expires |
| Approval Amt | wus_mstr.wus_app_amt | Approval limit |
| Supervisor | wus_mstr.wus_supervisor | Supervisor's user ID |
| Domains | wus_mstr.wus_domains | Domains user can access |
| Last Login | wus_mstr.wus_last_login | Last login timestamp |
| Departments | wus_mstr.wus_depts | Departments user belongs to |

## Use Cases

- **Quarterly audits** - Provide auditors with complete user access list
- **Access reviews** - Review who has access to what groups
- **Compliance documentation** - SOX, SOC2, or other compliance requirements
- **User cleanup** - Identify disabled users still in groups

---

## Related Screens

- [Users and Groups](./01-users-and-groups.md) - Manage users and group membership
