# iPurchase System Settings Reference (RAG-Optimized)

> This file is auto-generated for AI/RAG vector search optimization.
> Do not edit directly. Edit `reference/system-settings-reference.md` and regenerate.

Complete catalog of iPurchase system settings organized by category. These settings are stored in the pf_mstr table and control all aspects of iPurchase behavior.

**To query a setting:**
```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'SETTING_NAME'
```

## ACH Integration

| Setting | Owner | Default | Description |
|---------|-------|---------|-------------|
| **ACH_ARCHIVE_FOLDER** | Admin |  | Directory path on application server. Archive folder where processed ACH files are moved after being polled and processed. Used in job_iaach_poller.p. Related: ACH_POLLING_FOLDER |
| **ACH_POLLING_FOLDER** | Admin |  | Directory path on application server. Folder where incoming ACH files (*.txt) are placed for processing by the ACH polling job. Processed files are moved to ACH_ARCHIVE_FOLDER. Used in job_iaach_po... |
| **ATTACH_IN_DB** | IT | `TRUE` | Store attachments in iPurchase database (True) or store attachments on disk (False). |
| **COPY_ATTACHMENTS** | Admin | `TRUE` | This setting indicates whether or not attachments are copied when a requisition is copied |

---

## Approval Workflow

Settings that control how requisitions are routed for approval, who can approve, approval thresholds, escalation rules, and delegation behavior.

**Configure these settings when you need to:**
- Configure approval routing behavior
- Set up supervisor chain approvals
- Control who can modify approvers
- Configure approval escalation and reminders
- Set up batch approval permissions

**Common questions this answers:**
- How do I configure approval routing?
- What settings control supervisor approvals?
- How do I enable batch approvals?
- How does approval escalation work?
- What is MULTIPLE_APPROVALS?
- How do I configure delegation/OOF?

### Settings

| Setting | Owner | Default | Description |
|---------|-------|---------|-------------|
| **ALLOWED_DOLLAR_INCREASE** | Finance | `100` | Specify the amount that an approver can increase the requisition by without having it re-routed. If the requisition amount is increased greater than the value specified here, then the requisition w... |
| **ALLOWED_PERCENT_INCREASE** | Finance | `10` | Specify the amount that an approver can increase the requisition by without having it re-routed. If the requisition amount is increased greater than the value specified here, then the requisition w... |
| **ALLOW_APPROVAL_SIMULATION** | Admin | `*` | Comma separated list of User ID's or Group ID's that are allowed to view an Approval Simulation. Asterisk indicates everyone, a blank indicates no one. |
| **ALLOW_APPROVER_CHANGES** | Admin | `TRUE` | This is the global setting which controls whether Approvers can be manually added or deleted from the approval routing. It also controls whether the Force Approval functionality is enabled. Also se... |
| **ALLOW_APPROVER_CHANGES_ORIGINATOR** | Power Users | `TRUE` | Indicates whether the originator is allowed to add or remove approvers. In order for this to be enabled, Allow_Approver_Changes must also be set to TRUE. |
| **ALLOW_APPROVER_CHANGES_REMOVE_APPROVER** | Admin | `admin` | Allow a user to remove an approver from the routing rules.  If this is enabled and Allow_Approver_Changes_Originator is enabled then the originator will also be allowed to remove approvers from the... |
| **ALLOW_APPROVER_CHANGES_ROLES** | Admin | `admin` | Any member of a group in this list will be allowed to add approvers.  If Allow_Approver_Changes_Remove_Approver is also enabled, then any member of these groups is also allowed to remove approvers.... |
| **ALLOW_DELETE_APPROVED** | Admin | `admin` | Comma separated list of User ID's or Group ID's who are allowed to delete an approved requisition.  Asterisk indicates everyone, a blank indicates no one. |
| **ALLOW_SUPERVISORS_TO_APPROVE** | Admin | `*` | Comma separated list of User ID's or Group ID's that are allowed to approve for a subordinate. Asterisk indicates everyone, a blank indicates no one. This setting allows a supervisor to Approve or ... |
| **APPROVAL_EMAIL_REPLY_TO** | Admin |  | Replies to approval email should go to who? Leave blank for originator. Set to 'OBO' for On behalf of. Set to any single email address. |
| **APPROVAL_INCLUDE_FIELDS** | ISS |  | Comma-Separated list of fields from xxreq_mstr and xxreqd_det tables. You can limit the fields which display in the approval rules screen to only those in this list. |
| **APPROVAL_METRICS_RED** | Admin | `90` | This setting allows the administrator to set how long the approval time should take before it will turn red on the approval metrics.  MINUTES |
| **APPROVAL_METRICS_YELLOW** | Admin | `30` | This setting allows the administrator to set how long the approval time should take before it will turn yellow on the approval metrics. MINUTES |
| **APP_ORIG_OR_OBO** | Admin | `OBO` | ORIGINATOR \| OBO. Determines whether approval rule xxapp_orig field matches against the requisition originator (xxreq_userid) or the On Behalf Of person (xxreq_obo). Affects approval rule evaluati... |
| **APP_SUPERVISOR_SEQ** | Admin | `10` | This is the Approval Level or Sequence when adding supervisors to the approval routing. |
| **AUTO_APPROVE_FORWARD** | Admin | `TRUE` | 1 if a user approves go through all other approvals where that user is listed in a group. If that user is the only member of the group, then automatically approve. 2 Last approval is never automati... |
| **BATCH_APPROVE_GROUPS** | Admin |  | Comma Separated list of User ID's or Group ID's that will allow an approver to approve multiple requisitions simultaneously from the Requisition Inquiry screen.  If the user is a member of the spec... |
| **BATCH_APPROVE_GROUPS_ALWAYS** | Admin |  | Comma-Separated list of User ID's or Group ID's. By default, the setting BATCH_APPROVE_GROUPS will only allow you to batch approve for requisitions that specifically include yourself. Batch approva... |
| **BATCH_APPROVE_GROUPS_FINAL** | Admin |  | Can-Do list. Groups allowed to perform batch approval as the final approver. Restricts batch approval to specific approval steps. |
| **DEFAULT_LINES_TO_APPROVED** | Power Users | `TRUE` | If using Line Approvals, then setting this to a value of TRUE will set each line to Approved (Green) as the default each time the requisition is submitted for approval. A value of FALSE will set ea... |
| **DEFAULT_LINES_TO_APPROVED_AUTO** | Admin |  | Comma-Separated List of User ID's or Group ID's. If setting DEFAULT_LINES_TO_APPROVED is set to false, then adding a user or group to this setting will automatically approve any line items which ar... |
| **EMAIL_NO_APPROVE_LINK** | Admin | `FALSE` | True or False - Include link to Approve in email that goes out to approver. Default FALSE |
| **EMAIL_SUPPLIER_PO_TO_FINAL_APPROVER** | Power Users | `FALSE` | A value of true will send a copy of the supplier email to the final approver when the PO is created. |
| **ESCALATION_EXCEPT_USERS** | Admin |  | Can-Do list. Users/groups exempt from approval escalation timeouts. Their pending approvals won't escalate. |
| **ESCALATION_NO_EMAILS_TO** | Admin |  | Can-Do list. Users/groups who do not receive approval escalation notification emails. |
| **FORCE_APPROVAL_ROLE_LIST** | Admin | `admin` | Comma Separated list of User ID's or Group ID's that are allowed to Force Approve any requisition.  Force Approval bypasses all open approvals and creates a PO. A history of this action is maintain... |
| **IGNORE_SPVSR_LOAD** | Admin |  | Can-Do list. Users to ignore when calculating supervisor approval workload in load balancing. |
| **INQUIRY_AFTER_APPROVAL** | Power Users | `*` | Comma separated list of User ID's or group id's that are re-directed to the pending queue once they have approved a requisition. Asterisk indicates everyone, a blank indicates no one. This setting ... |
| **LOGIN_APPROVERS_ALWAYS_SEE_APPROVALS** | Power Users | `*` | A comma separated list of User ID's or Group ID's that will always be logged into their pending queue, regardless of whether they do or do not have pending requisition to approve. Asterisk indicate... |
| **MULTIPLE_APPROVALS** | Admin | `KEEP_LAST` | When an approver or approval group appears in the approval routing more than once, which approval record is actually added to the routing. When KEEP_ALL is chosen then all approval records for the ... |
| **NEW_REROUTE_METHOD** | Admin | `FALSE` | TRUE \| FALSE. If TRUE, uses new rerouting algorithm for change orders. |
| **NO_APPROVAL_EMAILS** | Admin |  | Comma separated list of requisition types that will not send approval emails to approvers. |
| **NO_MGR_ROUTE_TO** | Admin |  | User/group. Skip supervisor chain routing and route directly to this approver. |
| **OOF_LIMIT_TO_APPROVERS** | Admin | `FALSE` | A setting of TRUE will allow a user to delegate only to other Approvers. A False value will allow a user to delegate to anyone. |
| **REMINDER_DAYS** | Admin | `3` | Numeric. Days before sending reminder emails to pending approvers. |
| **REMOVE_APPROVER_FROM_GROUPS** | Admin | `FALSE` | TRUE \| FALSE. If TRUE, removes approver from later groups if they already approved. |
| **REMOVE_APPROVER_ROLE_LIST** | Admin | `admin` | Comma separated list of User ID's or Group ID's that are allowed to remove an Approver from any requisition. Asterisk indicates everyone, a blank indicates no one. |
| **REMOVE_ORIGINATOR_FROM_GROUP_CO** | Admin | `FALSE` | TRUE \| FALSE. If TRUE, removes originator from approval routing on change orders. |
| **ROLES** | Admin |  | Comma-separated list of role names that can be assigned in the User Roles screen. These roles are combined with hard-coded Types (Account, Cost Center, Project, Site, Sub Account) to create approva... |
| **ROLE_MISSING_SKIP_LIST** | Admin |  | Comma-separated list of Types (Cost Center, Account, Project, Sub Account, Site). If a role mapping is missing for a Type in this list, the approval engine skips that approver silently. If a Type i... |
| **SHOW_APPROVER_METRICS** | Admin | `buyers,admin` | Comma separated list of User ID's or group id's that have access to view approval time metrics in the Requisition Inquiry. Asterisk indicates everyone, a blank indicates no one. |
| **SUPERVISOR_APPROVAL_FIELD** | Admin | `wus_supervisor` | Field name. Database field used to determine supervisor chain (default: wus_supervisor). |
| **SUPERVISOR_ESCALATION_ANYTIME** | Admin | `FALSE` | TRUE \| FALSE. If TRUE, supervisors can approve/reject anytime, not just when pending. |
| **SUPERVISOR_ESCALATION_DAYS** | Power Users | `3` | This is the number of days which must elapse before an approver can Approve or Reject a requisition on behalf of someone else who reports to this given supervisor. See SUPERVISOR_ESCALATION_LEVEL a... |
| **SUPERVISOR_ESCALATION_LEVEL** | Admin | `99` | This setting determines how many supervisors up the supervisor tree (organization chart) are allowed to approve or reject a requisition. A value of one will only allow the approver's immediate supe... |
| **USE_APP_AMOUNT_OWN_REQS** | Admin |  | Comma separated list of User ID's or Group ID's that indicates whether a user's requisition can be automatically converted to a PO if the user's approval amount exceeds the requisition amount. If t... |
| **USE_LINE_APPROVALS** | Power Users | `FALSE` | This setting determines whether supervisors can approve or reject individual line items. Only those line items which are approved will be added to the PO. If there are any items which are neither a... |
| **USE_SUPERVISORS_TO_APPROVE** | Admin | `FALSE` | TRUE \| FALSE. Use supervisor chain for approvals. |

---

## Catalog & Vendors

| Setting | Owner | Default | Description |
|---------|-------|---------|-------------|
| **ALLOW_TEMP_VENDORS** | Purchasing | `FALSE` | TRUE \| FALSE. If TRUE, allows use of temporary/unverified vendors on requisitions. If FALSE, temporary vendors are rejected. |
| **APPROVED_SUPPLIERS_ONLY** | Purchasing | `FALSE` | TRUE \| FALSE. If TRUE, only approved suppliers can be selected on requisitions. Enforces supplier approval workflow. |
| **AUTO_ADD_SUPPLIER_MC_TYPES** | Purchasing | `PO` | In QAD master comments, there is a reference number to identify a master comment, if this reference number equals the suppler then the master comment will be added to the requisition automatically ... |
| **AVL_REQ_TYPES** | Purchasing |  | Comma-separated requisition types. Requisition types that require Approved Vendor List validation. Related: SIG_AVL_REQ_TYPES, USE_SIG_AVL |
| **CART_SINGLE_SUPPLIER** | Purchasing | `FALSE` | TRUE \| FALSE. If TRUE, shopping cart is restricted to items from a single supplier. Mixed supplier carts are not allowed. |
| **CATALOG_ACCESS_[Supplier NBR]** | Admin |  | Comma separated list of User ID's or Group ID's that have access to the specified supplier catalog. If this setting does not exist for a supplier, then everyone will have access to that supplier's ... |
| **CATALOG_CAN_DELETE** | Admin | `admin` | Comma Separated list of User ID's or Group ID's that are allowed to delete catalogs.  Asterisk indicates everyone, a blank indicates no one. |
| **CATALOG_CAN_RATE** | Purchasing | `FALSE` | TRUE \| FALSE. If TRUE, users can rate catalog items. Related: CATALOG_SHOW_RATING |
| **CATALOG_CART_SHOW_DETAILS** | Admin | `TRUE` | This setting will show supplier, lead time, manufacturer, and UOM in the cart for a catalog if set to true. |
| **CATALOG_DISPLAY_ROWS** | Power Users | `25` | This setting will allow the administrator to decide how many rows of items to display on a catalog requisition. |
| **CATALOG_EXCEPTION_REQ_TYPE** | Admin |  | If left blank the catalog exception requisition type should be set to "Catalog Exception". The administrator can change the name of the requisition type assigned to 'Catalog Exception' in this sett... |
| **CATALOG_EXCEPTION_USER** | Purchasing |  | Can-Do list. Users/groups exempt from catalog-only purchasing restrictions. Can create requisitions outside catalog. |
| **CATALOG_ITEM_NBR_MATCH** | Power Users | `FALSE` | A user can search a catalog using either matches or contains criteria.  If set to True then the system will use the Match functionality. Matches:  If the item number is 12345 then you should be abl... |
| **CATALOG_REQUEST_REQ_TYPE** | ISS | `Catalog Request` | Technical - Do Not Modify |
| **CATALOG_SHOW_DETAILS** | Admin | `TRUE` | If true, the catalog screen will display supplier, lead time, minimum quantity. |
| **CATALOG_SHOW_PICTURES** | Admin | `TRUE` | If true, images of items will appear in catalogs. |
| **CATALOG_SHOW_RATING** | Purchasing | `FALSE` | TRUE \| FALSE. If TRUE, displays item ratings in catalog interface. Related: CATALOG_CAN_RATE |
| **CATALOG_SORT** | ISS | `List:by uCatalog.uDomain by uCatalog.SupplierPart:Part Number (Ascending),by uCatalog.uDomain by uCatalog.SupplierPart desc:Part Number (Descending),by uCatalog.UnitPrice:Price (Low to High),by uCatalog.UnitPrice desc:Price (High to Low)` | This setting gives the administrator the option to choose the sort by in a catalog requisition |
| **CATALOG_USE_CART** | Admin | `*` | Comma Separated list of User ID's or Group ID's that will use the catalog functionality in the "New Catalog Req" screen. Asterisk indicates everyone, a blank indicates no one. |
| **CAT_REJECT_TO_SUPPLIER** | Admin | `False ` | If a catalog exception requisition is rejected, the supplier will receive an email if set to true. |
| **CER_SECOND_SOURCE_AMOUNT** | Purchasing |  | Dollar amount. Threshold above which second source certification is required. Related to competitive bidding requirements. |
| **DROP_SHIP_EXCLUDE_SUPPLIER_TYPES** |  |  | Comma-Separated list of Supplier Types that should not show in the drop ship search. For example you may want to exclude employee addresses |
| **NEW_SUPPLIER_NBRS** |  |  | Comma separated list of supplier numbers which should not allow final approval. |
| **PUNCHOUT_DISABLE_USERS** | Purchasing |  | Can-Do list. Users/groups who are NOT allowed to use punchout functionality. |
| **PUNCHOUT_LEADTIME** | Admin | `3` | The number of days to add to today's date in order to calculate the Need Date for the requisition header. Can change by supplier in Supplier Maintenance (iPurchase) |
| **PUNCHOUT_NOFRAMES** | Admin |  | iPurchase uses an HTML FRAMESET to display the Punchout website as well as the Return to iPurchase button at the top left. Some suppliers, like Amazon, will not allow the Return to iPurchase button... |
| **PUNCHOUT_NO_ITEM_DESC** | Purchasing | `FALSE` | TRUE \| FALSE. If TRUE, excludes item descriptions from punchout requests. |
| **PUNCHOUT_REQ_TYPE** | Admin |  | This setting allows the administrator to globally set a default requisition type for punchout requisitions. |
| **PUNCHOUT_REQ_TYPE_[supplier]** | Admin |  | This setting allows the administrator to set a default requisition type by supplier for punchout requisitions. |
| **PUNCHOUT_RETRY** | Purchasing | `3` | Numeric. Number of retry attempts for failed punchout connections. |
| **RT_CATALOG EXCEPTION_PP** | ISS | `catexceptload.p` | Technical - Do Not Modify without consulting ISS |
| **RT_VENDOR_ITEM_ONLY** | Admin |  | Comma separated list of requisition types which will mandate that an item selected to a requisition must exist in the vendor part cross-reference table in QAD. |
| **SHOW_COST** | Purchasing |  | Can-Do list. Users allowed to see item costs. |
| **SHOW_MARGIN** | Purchasing |  | Can-Do list. Users allowed to see profit margins. |
| **SIG_AVL_REQ_TYPES** | Purchasing |  | Comma-separated types. Types using signature-based approved vendor list. Related: AVL_REQ_TYPES, USE_SIG_AVL |
| **SUPPLIER_CONFIRMATION** | Purchasing | `FALSE` | TRUE \| FALSE. Require supplier PO confirmation. |
| **SUPPLIER_PO_MERGE_ATTACHMENTS_EXCLUDE** | Purchasing |  | Comma-separated suppliers. Suppliers excluded from attachment merging. |
| **SUPPLIER_SEARCH_MATCHES** | Admin | `FALSE` | If set to True then a user can search for a supplier using any character in the suppliers name.  If set to True, the supplier lookup will run slower. |
| **USE_SIG_AVL** | Purchasing | `FALSE` | TRUE \| FALSE. Enable signature-based approved vendor list. Related: SIG_AVL_REQ_TYPES |
| **VALIDATE_SUP_ITEM** | Purchasing | `FALSE` | TRUE \| FALSE. Validate that supplier carries the requested item. |
| **VENDOR_ITEM_ONLY** | Purchasing | `FALSE` | TRUE \| FALSE. Restrict requisitions to items in vendor catalog only. |

---

## Change Orders

Settings that control change order behavior, tolerance thresholds, and re-routing rules when requisitions or POs are modified.

**Configure these settings when you need to:**
- Set change order tolerance amounts
- Configure when changes require re-approval
- Control change order routing behavior

**Common questions this answers:**
- How do change order tolerances work?
- When do changes require re-approval?
- What is CO_TOLERANCE_AMOUNT?

### Settings

| Setting | Owner | Default | Description |
|---------|-------|---------|-------------|
| **ALLOW_AUTO_REROUTE** | Admin | `TRUE` | If an approver makes a change to a requisition, iPurchase will re-check who the approvers should be in order for the changes made. If the new approver set is different from the current approver set... |
| **CHANGE_ORDER_CHANGE_ORIG** | Purchasing | `FALSE` | TRUE \| FALSE. If TRUE, allows changing the originator (xxreq_userid) field on purchase order change orders. |
| **CO_DELETE_CANCELLED_LINES** | Purchasing | `FALSE` | TRUE \| FALSE. If TRUE, permanently deletes cancelled lines on change orders. If FALSE, lines remain with cancelled status. |
| **CO_HEADER_REROUTE_FIELDS** | Admin |  | Comma Separated list of header fields which will force a change order to automatically re-route if they are changed. |
| **CO_IGNORE_COST** | Purchasing | `FALSE` | TRUE \| FALSE. If TRUE, cost changes are ignored when determining if change order is material (requires re-routing). |
| **CO_ITEM_REROUTE_FIELDS** | Admin |  | Comma Separated list of item fields which will force a change order to automatically re-route if they are changed. |
| **CO_ITEM_REROUTE_NEW** | Admin | `FALSE` | Automatically re-route a change order if a new line is added to the requisition. |
| **CO_REROUTE_EXCLUDE_TYPES** | Purchasing |  | Comma-separated requisition types. Types excluded from change order re-routing even when changes are material. |
| **PO_UPDATE_CHECK_REROUTE** | Admin | `TRUE` | As part of the approval process, do you want the system to compare the approvers from the original requisition to the new requisition? If there are any changes then the new requisition will be re-r... |
| **PO_UPDATE_CHECK_REROUTE_RELEASES** | Purchasing | `FALSE` | TRUE \| FALSE. If TRUE, checks blanket PO releases for material changes requiring reroute. |
| **PUNCHOUT_CHANGE_ORDER_SEND** | Admin | `*` | Send PO revisions automatically to punchout suppliers via cXML. List of Vendor Numbers or * for all. CAN-DO functionality !staples,* |
| **UPDATE_COST_ON_CO** | Purchasing | `FALSE` | TRUE \| FALSE. Update line costs when creating change order. |
| **UPDATE_COST_ON_COPY** | Purchasing | `FALSE` | TRUE \| FALSE. Update line costs when copying requisition. |
| **UP_ONLY_APP_LEVEL_EXCLUDED** | Admin |  | Comma-separated approval levels. Approval levels to exclude from UP_ONLY rule evaluation. |
| **UP_ONLY_REQ_TYPES** | Admin |  | Comma-separated requisition types. Types that use UP_ONLY (Update PO Only) routing rule. |
| **UP_ONLY_RULE** | Admin | `FALSE` | TRUE \| FALSE. Enable Update PO Only routing rule for change orders that don't require full re-routing. |

---

## Code Lists & Dropdowns

| Setting | Owner | Default | Description |
|---------|-------|---------|-------------|
| **CODE_LIST_H_BILLTO** | Finance |  | This is a pointer to the code_mstr field name (code_fldname) value to be used for the Header Bill To selection list and validation.  Leaving this value blank will tell iPurchase to use the si_mstr ... |
| **CODE_LIST_H_BLANKET_CYCLE** | ISS | `List:MO:Monthly,WK:Weekly,DA:Daily` | Enter a comma-separated list of cycle codes to be entered in the cycle code drop down menu on the blanket information tab on a requisition. |
| **CODE_LIST_H_CURRENCY** | Finance |  | Currency List same as other lists - blank will use all currencies from QAD - cu_mstr |
| **CODE_LIST_H_FOB** | Finance | `po_fob` | code_fldname This is a pointer to the code_mstr field name (code_fldname) value to be used for the Header FOB selection list and validation. You can also use the prefix "LIST:" followed by a comma-... |
| **CODE_LIST_H_SHIPTO** | Admin |  | code_fldname  or  blank This is a pointer to the code_mstr field name (code_fldname) value to be used for the Header Ship To selection list and validation.  Leaving this value blank will tell iPurc... |
| **CODE_LIST_H_SHIPVIA** | Finance | `po_shipvia` | code_fldname This is a pointer to the code_mstr field name (code_fldname) value to be used for the Header ShipVia selection list and validation. You can also use the prefix "LIST:" followed by a co... |
| **CODE_LIST_H_SITE** | Finance |  | code_fldname This is a pointer to the code_mstr field name (code_fldname) value to be used for the Header Site selection list and validation.  Leaving this value blank will tell iPurchase to use th... |
| **CODE_LIST_MRO_TYPE** | Admin |  | code_fldname This is a pointer to the code_mstr field name (code_fldname) value to be used for the Line MRO Type selection list, and validation. You can also use the prefix "LIST:" followed by a co... |
| **CODE_LIST_REJECTION_CODES** | Power Users | `List:001:Invalid Prices,002:Invalid Accounts` | code_fldname This is a pointer to the code_mstr field name (code_fldname) value to be used for the Rejection Code selection list and validation. A value of blank or a non-existing setting will turn... |
| **CODE_LIST_UM** | Finance | `pt_um` | code_fldname This is a pointer to the code_mstr field name (code_fldname) value to be used for the Line Unit of Measure selection list and validation. A value of blank or a non-existing setting wil... |

---

## Custom/Product Management

| Setting | Owner | Default | Description |
|---------|-------|---------|-------------|
| **PRODUCT_MGR_GROUP** | Purchasing |  | Group ID for product managers. Customer-specific product management setting. |
| **PROD_LINES_DERMIS** | Purchasing |  | Product line categorization for Dermis business unit. Customer-specific. |
| **PROD_LINES_ORTHO** | Purchasing |  | Product line categorization for Ortho business unit. Customer-specific. |
| **PROD_LINES_WOUND_CARE** | Purchasing |  | Product line categorization for Wound Care business unit. Customer-specific. |

---

## EAM Integration

| Setting | Owner | Default | Description |
|---------|-------|---------|-------------|
| **JE_USE_EAM** | Finance | `FALSE` | TRUE \| FALSE. If TRUE, uses EAM system for journal entry processing. |
| **USE_EAM_ACCOUNTS** | Finance | `FALSE` | TRUE \| FALSE. Use EAM account structure. |
| **USE_SINGLE_CURRENCY** | Finance | `FALSE` | TRUE \| FALSE. Force single currency mode, disable multi-currency. |

---

## Email Configuration

Settings for email notifications, SMTP configuration, email templates, and automated email behavior throughout iPurchase.

**Configure these settings when you need to:**
- Configure SMTP server settings
- Control which emails are sent
- Set up email templates and formatting
- Configure approval notification emails

**Common questions this answers:**
- How do I configure email settings?
- How do I disable certain email notifications?
- What is the SMTP configuration?

### Settings

| Setting | Owner | Default | Description |
|---------|-------|---------|-------------|
| **ALLOW_MANUAL_EMAIL_PO** | Admin |  | Comma-Separated list of User ID's or Group ID's. that will have the "Email PO" option which would allow a user to email the PO through iPurchase. Asterisk indicates everyone, a blank indicates no one. |
| **APPLICATION_URL** | Admin |  | Full application URL (e.g., https://ipurchase.company.com). Used by scheduled jobs for email links. On test/backup systems, should be updated to match environment. |
| **APPROVAL_EMAIL_ONLY_NOPO** | Admin | `FALSE` | TRUE \| FALSE. If TRUE, approval emails are sent only when the requisition does NOT require a PO (xxreq_po_required = TRUE). Used to reduce email volume. |
| **BASE_URL** | Admin |  | Base URL/hostname (e.g., https://server.company.com). Used in email notifications and scheduled job links. Should be updated on test/backup systems. |
| **EMAILFROM** | Admin |  | AD Email Address This is a valid email address for which all iPurchase emails will be sent from. |
| **EMAILSERVER** | IT |  | IP Address of SMTP Server. This is the IP Address of the SMTP Server from which iPurchase sends all emails. |
| **EMAILS_TO** | Admin |  | Comma-separated email address(s) where all emails from the service will be sent to. This overrides the actual user's email addresses. |
| **EMAIL_AUTH_PASSWORD** | Admin |  | Technical - Do Not Modify without consulting ISS |
| **EMAIL_AUTH_TYPE** | Admin |  | Technical - Do Not Modify without consulting ISS |
| **EMAIL_AUTH_USER** | Admin |  | Technical - Do Not Modify without consulting ISS |
| **EMAIL_DEBUG_LEVEL** | Admin | `0` | Numeric 0-3. Email system debug verbosity. 0=off, 1=basic, 2=detailed, 3=verbose. Used for troubleshooting email issues. |
| **EMAIL_DISCLAIMER_REJECT** |  | `If questions, please contact the approver that rejected the requisition` | If questions, please contact the approver that rejected the requisition |
| **EMAIL_HEADER** | Admin |  | HTML content. Custom header included in email templates. Used for branding/styling emails. |
| **EMAIL_HELPDESK** | Admin |  | Helpdesk Email Address Enter the email address for the helpdesk. Used on login screen as well as all emails. |
| **EMAIL_HELP_TAG** | Admin | `If questions, email the $HELPDESK, or contact the originator, or approver.` | Include -- If questions, email the helpdesk link on all internal emails." |
| **EMAIL_NEW_USER_BODY** | Admin |  | This setting allows the administrator to set the body of the email that is sent to users when a new user is created. Special tokens that can be inserted in email are $User ID, $PASSWORD, $URL.  The... |
| **EMAIL_NEW_USER_SUBJECT** | Admin |  | This setting allows the administrator to set the subject for the new user email. |
| **EMAIL_NO_REJECT_LINK** | Admin | `FALSE` | True or False - Include link to Reject in email that goes out to approver. Default FALSE |
| **EMAIL_OPEN_PO_INCLUDE_DOMAINS** |  | `*` |  |
| **EMAIL_OPEN_PO_INCLUDE_TYPES** |  | `!Inventory,*` |  |
| **EMAIL_OPEN_PO_INCLUDE_USERS** |  | `*` |  |
| **EMAIL_OPEN_PO_REMINDER_SUBJECT** |  | `Open POs in IPurchase` |  |
| **EMAIL_OPEN_PO_REMINDER_TEXT** |  | `Below is a list of your open purchase orders` |  |
| **EMAIL_PASSWORD_CHANGE_BODY** | Admin |  | This setting allows the administrator to set the body of an email when the administrator changes a password.  Special token is $PASSWORD. |
| **EMAIL_PASSWORD_CHANGE_SUBJECT** | Admin |  | This setting allows the administrator to set the subject for the password change email. |
| **EMAIL_PO_ADDITIONAL** | Purchasing |  | Comma-separated email addresses. Additional recipients for purchase order emails beyond default recipients. |
| **EMAIL_PO_BODY** | Admin | `This should be line one. <br><br> | Allows the administrator to create a custom email body for new PO. |
| **EMAIL_PO_BODY_REVISION** | Admin |  | Allows the administrator to create a custom email body for PO revision emails. |
| **EMAIL_PO_INCLUDE_SIG** | Purchasing | `TRUE` | This setting includes the buyer's contact information for emails automatically sent to suppliers when PO is created. It also includes logged in user's contact information in emails which are manual... |
| **EMAIL_PO_LOGO** | Admin |  | Image URL or file path. Company logo displayed in purchase order emails. |
| **EMAIL_PO_RECEIPTS** | Purchasing | `FALSE` | TRUE \| FALSE. If TRUE, sends email receipts/confirmations when purchase orders are created or modified. |
| **EMAIL_PO_TO_FINAL_APPROVER** | Admin | `FALSE` | TRUE \| FALSE. If TRUE, sends PO creation notification to the final approver on the requisition. |
| **EMAIL_PURGE_DAYS** | Admin | `30` | How often iPurchase will purge emails that have error-ed . Value is in days. |
| **EMAIL_REGISTRATIONS** | Admin |  | Email addresses (comma-separated). Recipients of new user registration notifications. |
| **EMAIL_REPLY_TO** | Admin |  | Email address. Reply-to address used in system-generated emails. If blank, uses FROM address. |
| **EMAIL_REQ_BODY_MIN** | Admin | `FALSE` | When this is TRUE, only the supplier's number and name along with the cost of the requisition are embedded in the email. If the requisition is a change order, then the words "Change Order" will als... |
| **EMAIL_SUPPLIER_ATTACH_FILES** | Admin | `FALSE` | This setting determines whether attachments are added to the email that will go to the supplier when the requisition is approved. |
| **EMAIL_SUPPLIER_ATTACH_LINKS** | Admin | `FALSE` | This setting determines whether attachments to a requisition are sent to the supplier as links in the email. |
| **EMAIL_SUPPLIER_BLANKET_PO** | Purchasing | `FALSE` | This setting determines whether or not an email is automatically sent to a supplier when the blanket order requisition is approved. |
| **EMAIL_SUPPLIER_CONFIRMATION_LINK** | Purchasing | `FALSE` | Determines if confirmation link is included in the PO email that is automatically sent to the supplier. It will also determine if the 'Include Confirmation Link' is displayed as an option on the ma... |
| **EMAIL_SUPPLIER_CONFIRMATION_REMINDER_TEXT** | Purchasing |  | Custom text included in supplier confirmation reminder emails. |
| **EMAIL_SUPPLIER_CONFIRMATION_TEXT** | Purchasing |  | This is the text that is to be inserted above the link which is included in the supplier email PO program. The default is "Please click the link to confirm acceptance of the Purchase Order". |
| **EMAIL_SUPPLIER_PO** | Purchasing | `TRUE` | This setting determines whether or not an email is automatically sent to a supplier when the requisition is approved. |
| **EMAIL_SUPPLIER_PO_CC** | Power Users | `$xxreq_buyer,$xxreq_obo,$xxreq_userid` | This is a list of email address(s) of whom to carbon copy the supplier email to when the PO is created.  A value of "BUYER" will copy the associated buyer which is set on the requisition. If a user... |
| **EMAIL_SUPPLIER_PO_FROM** | Power Users | `$xxreq_buyer` | This is the email address to be used as the "From" field on the email. This can be a static email address or one of $xxreq_buyer, $xxreq_User ID, $xxreq_obo. If this field is left blank then the se... |
| **EMAIL_SUPPLIER_PO_SUBJECT** | Purchasing | `New Purchase Order  - $NBR` | This text will be used as the subject of the email going to the supplier. If you'd like the PO number(s) to appear in the subject, add the text "$NBR" without the quotes in the position that you wa... |
| **EMAIL_SUPPLIER_PO_SUBJECT_PUNCHOUT** | Purchasing | `Punchout Purchase Order - $NBR` | This text will be used as the subject of the email going to the supplier. If you'd like the PO number(s) to appear in the subject, add the text "$NBR" without the quotes in the position that you wa... |
| **EMAIL_SUPPLIER_PO_SUBJECT_REVISION** | Purchasing | `Purchase Order Revision - $NBR` | This text will be used as the subject of the email going to the supplier. If you'd like the PO number(s) to appear in the subject, add the text "$NBR" without the quotes in the position that you wa... |
| **INTERNAL_URL** | Admin |  | Internal network URL for application. Used when APPLICATION_URL/BASE_URL are external-facing. |
| **LOGIN_HIDE_EMAIL_HELPDESK** | Admin |  | Hide the Email Helpdesk link on the login screen |
| **NEW_PO_EMAIL_RECEIPTS** | Purchasing | `no,no` | This setting determines if delivery receipts and read receipts are requested from the recipient's mail server when the email which includes the new PO attached is sent. To turn off this functionali... |
| **NO_CHANGE_EMAIL** | Power Users | `FALSE` | If an approver changes a requisition and this is set to true, then the originator will not be notified. |
| **NO_EMAILS** | Admin | `FALSE` | A value of True will turn off email functionality. A value of False will turn on email functionality. |
| **NO_EMAIL_REQ_BODY** | Power Users | `FALSE` | Do not include the requisition print in emails. Only includes the text. |
| **NO_PO_EMAIL** | ISS |  | Technical - Do Not Modify without consulting ISS |
| **PO_DO_NOT_EMAIL** | Power Users | `FALSE` | If set to true the PO will not be emailed. |
| **RECEIPT_EMAIL_MESSAGE** | Purchasing |  | Custom message text for receipt notification emails. |
| **RECEIPT_EMAIL_REQ_TYPES** | Purchasing |  | Comma-separated req types. Types that trigger receipt emails. |
| **RECEIPT_EMAIL_SUBJECT** | Purchasing | `Receipt Notification` | Email subject for receipt notifications. |
| **RECEIPT_EMAIL_TO** | Purchasing |  | Email addresses for receipt notifications. |
| **RECEIPT_EMAIL_USERS** | Purchasing |  | Can-Do list. Users who receive receipt notification emails. |
| **REMOVE_NEEDED_BY_FROM_EMAILS** | Power Users | `FALSE` | Show 'Needed By 99/99/9999' in the approval email subject. |

---

## GL Accounts & Finance

Settings for GL account validation, financial controls, currency, and accounting-related behavior.

**Configure these settings when you need to:**
- Configure GL account validation
- Set up financial controls
- Configure currency settings

**Common questions this answers:**
- How do I validate GL accounts?
- How do I configure account ranges?
- How does currency handling work?

### Settings

| Setting | Owner | Default | Description |
|---------|-------|---------|-------------|
| **ACCOUNT_RANGE_CANDO** | Finance | `*` | This is a comma separated list of accounts that can be used with iPurchase. The field uses the Progress �Can-Do� function. See Progress help if needed. A sample value can be 5521,!5622,56*,7*,!* Th... |
| **ACCOUNT_REQUIRE_PROJECT** | Finance |  | A list of accounts which will always require a Project Code |
| **ACCOUNT_SHOW_CUSTOMNOTE** | Finance | `FALSE` | Show the value CustomNote Field on the GL record - only for EE |
| **ACCOUNT_SORT_BY_NAME** | Power Users | `FALSE` | A value of true will show the accounts sorted by name. Any other value will sort by number. |
| **ARCHIVE_KEEP_YEARS** | Finance | `3` | The number of years to keep requisitions. Note: Pending Requisitions can't be archived. |
| **BUDGET_ADMINISTRATOR** | Admin |  | Comma Separated list of User ID's or Group ID's who are allowed to maintain budgets in iPurchase. Asterisk indicates everyone, a blank indicates no one. |
| **BUDGET_ASST_EDIT** | Admin | `*` | Allow the budget assistant managers specified in a budget the ability to modify the sub budgets. Assistant Managers can't modify the budget header. |
| **BUDGET_HIDE_OTHER** | Admin | `TRUE` | Do not show nor use the Other column on Budgets. |
| **BUDGET_MGR_EDIT** | Admin | `*` | Allow the budget manager specified in a budget the ability to modify the entire budget |
| **BUDGET_MONTHLY_REPORT** | Finance |  | Can-Do list. Users/groups allowed to access budget monthly reports. Automatically disabled in archive systems. |
| **BUDGET_THRESHOLD_AMT** | Power Users |  | Threshold amount added to defined budget amount before error that you can not create another item using that budget. |
| **BUDGET_THRESHOLD_PCT** | Power Users |  | Threshold pct added to defined budget amount before error that you can not create another item using that budget. |
| **CODE_LIST_TAX_CLASS** | Finance | `comma-separated list of tax classes. List: is not needed on this setting` |  |
| **CODE_LIST_TAX_ENVIRONMENT** | Finance |  | LIST format. Dropdown values for tax environment field. Format: LIST:code:description,code:description |
| **CODE_LIST_TAX_USAGE** | Finance | `comma-separated list of tax usage. List: is not needed on this setting` |  |
| **COST_CENTER_REQUIRE_PROJECT** | Finance |  | Can-Do list. Cost centers that require a project code. Validation error if project is blank for these cost centers. |
| **DEFAULT_SUB_ACCOUNT** | Finance |  | The default sub account is used when creating requisition from catalogs and punchouts. The order in which iPurchase determines the sub account for a requisition created from a Punchout or Catalog i... |
| **DEFAULT_TAX_CLASS** |  |  | You can use this to set the Tax Class field in QAD. If set this will default for all Purchase Orders |
| **DEFAULT_TAX_ENVIRONMENT** |  |  | You can use this to set the Tax Environment field in QAD. If set this will default for all Purchase Orders |
| **DEFAULT_TAX_USAGE** |  |  | You can use this to set the Tax Usage field in QAD. If set this will default for all Purchase Orders. |
| **DEPARTMENTS_USE_ORIG** | Admin | `FALSE` | This setting allows the administrator to set the drop down list of departments at the line entry. If set to TRUE the list will be based on the originator.  If set to FALSE, the department is set ba... |
| **DEPARTMENT_SORT_BY_NAME** | Power Users |  | A value of true will show the departments sorted by name. Any other value will sort by number. |
| **ESTIMATED_TAX_PERCENT** | Finance |  | If the taxable amounts need to figure into the approval rules, then use this setting to enter an estimate tax percentage that will be added on to all taxable requisition lines.  If 10% enter as "10" |
| **ESTIMATED_TAX_PERCENT_[ship to code]** | Finance |  | If the taxable amounts need to figure into the approval rules, then use this setting to enter an estimate tax percentage that will be added on to all taxable requisition lines based on specific shi... |
| **GL_OVERRIDE** | Finance | `FALSE` | If you set this setting to true, then all items entered in the line entry screen will have the account, sub-account, and cost center set to the values which QAD would dictate based on the vendor an... |
| **OOF_LIMIT_BY_DEPT** | Admin | `FALSE` | A setting of True will only allow a user to delegate to another user who shares a same department. A setting of FIRST A setting will only allow a user to delegate to another user who is in the orig... |
| **PROJECT_RANGE_CANDO** | Finance | `*` | Can-Do list. Valid project codes. Default * allows all. |
| **REMOVE_ORIG** | Finance | `TRUE` | This setting does not allow the originator to be an approver for their own requisitions if set to true. |
| **RT_REQUIRE_PROJECT** | Finance | `Capital` | List of requisition typles that require a project code. |
| **RT_REQ_TAXABLE** | Finance |  | Comma-separated req types. Types where tax is calculated. If blank, all types are taxable. |
| **SUB_ACCOUNTS_USE_ORIG** | Finance | `FALSE` | TRUE \| FALSE. If TRUE, uses originator's allowed sub-accounts instead of OBO's. |
| **SUB_ACCOUNT_RANGE_CANDO** | Finance | `*` | This is the same as ACCOUNT_RANGE_CANDO except this applies to sub accounts. USE RT_.... |
| **SUB_ACCOUNT_SORT_BY_NAME** | Power Users |  | True or False A value of TRUE will show the sub-accounts sorted by name. Any other value will sort by number. |
| **TAX_CLASS_FIELD** | Finance |  | [LEGACY/OBSOLETE] Field name for tax class in data upgrades. Commented out in code. |
| **TAX_CUSTOMER** | Finance |  | Default tax customer code for tax calculations. |
| **TAX_USAGE_FIELD** | Finance |  | [LEGACY/OBSOLETE] Field name for tax usage in data upgrades. Commented out in code. |
| **USE_BUDGETS** | Finance | `FALSE` | [LEGACY/OBSOLETE] TRUE \| FALSE. Enable budget functionality. Commented out in code - use BUDGET_USE_IAPPROVE instead. |
| **USE_BUDGETS_AS_FORECAST** | Admin | `FALSE` | Allow full budget functionality but allow reqs to be created and processed even if overbudget. |

---

## Inventory & MRP

| Setting | Owner | Default | Description |
|---------|-------|---------|-------------|
| **CODE_LIST_MRP_BUYERS** | Purchasing |  | Only use this setting if you want to have a different buyer list show up in the MRP Action Center. This list is in the format 'list:code:desc,code:desc' or a generalized code field name like 'ptp_b... |
| **INV_TRANS_REASON_CODES** | Purchasing |  | Comma-separated reason codes. Valid transaction reason codes for inventory movements. |
| **INV_TRANS_TYPES** | Purchasing |  | Comma-separated transaction types. Valid inventory transaction types. |
| **MRP_SORT** | Purchasing |  | Sort field for MRP (Material Requirements Planning) item listings. |
| **RT_MRP** | Purchasing |  | Comma-separated req types. Types that trigger MRP (Material Requirements Planning). |
| **TRANSFER_STATUS** | Purchasing |  | Status value for inventory transfer transactions. |

---

## Portal Integration

| Setting | Owner | Default | Description |
|---------|-------|---------|-------------|
| **PORTAL_CONFIRM_RECEIPT_URL** | ISS |  | URL endpoint for portal receipt confirmation integration. Used for external portal systems. |

---

## Purchase Orders

Settings that control PO creation, numbering, printing, vendor communication, and PO-related workflow.

**Configure these settings when you need to:**
- Configure PO number formats
- Control PO creation behavior
- Set up PO printing and distribution
- Configure vendor PO emails

**Common questions this answers:**
- How are PO numbers generated?
- How do I configure PO printing?
- How do I control PO creation?

### Settings

| Setting | Owner | Default | Description |
|---------|-------|---------|-------------|
| **AUTO_COMMENTS_BUYER** | Power Users |  | Use this setting to automatically attach comments to every Purchase Order when a particular buyer or bill to or ship to or site or line site is used. This is a pointer to the code_mstr field name (... |
| **AUTO_COMMENTS_CO** | Power Users |  | Use this setting to automatically attach comments to every Purchase Order REVISION - CHANGE ORDER. This is a pointer to the code_mstr field name (code_fldname) value to be used. Example: List:Buyer... |
| **AUTO_COMMENTS_LINE_SITE** | Power Users |  | Use this setting to automatically attach comments to every Purchase Order when a particular buyer or bill to or ship to or site or line site is used. This is a pointer to the code_mstr field name (... |
| **AUTO_COMMENTS_OTHER** | Power Users |  | Use this setting to automatically attach comments to every Purchase Order when a particular buyer or bill to or ship to or site or line site is used. This is a pointer to the code_mstr field name (... |
| **BATCH_CREATE_PO_GROUPS** | Admin | `buyers` | Comma Separated list of User ID's or Group ID's that can convert an approved requisition into a PO (only when PO is not created automatically upon final approval) Thios setting also controls if a u... |
| **BLANKET_SEND_PO** | Purchasing | `FALSE` | If set to true the PO will be emailed. |
| **BUYER_MOD** | Purchasing | `FALSE` | TRUE \| FALSE. If TRUE, allows the buyer field to be modified during requisition copy and PO creation. If FALSE, buyer field is locked. |
| **CATALOG_PO_DIFFERENCE** | Power Users | `Lowest` | Possible Values: Blank, Punchout, Catalog, Lowest.  During a punchout, if an item ordered via a punchout site also exists in the catalog, do you want to use the Catalog's price rather than the pric... |
| **CLOSE_PO** | Admin | `buyers` | Comma Separated list of User ID's or Group ID's that will have the ability to close PO  or  PO line on Purchase order.  Either Line or whole PO can be closed. Close or canceled depends on Receipts.... |
| **CO_UPDATE_ORDER_DATE** | Purchasing | `FALSE` | Update the order date on the change order PO to today's date |
| **DEFAULT_BUYER** | Purchasing |  | This is the userid of the default buyer to be used on all new requisitions. This can be overridden by DEFAULT_BUYER_[SITE], RT_[REQ_TYPE]_DEFAULT_BUYER, RT_[REQ_TYPE]_[SITE]_DEFAULT_BUYER, and vd_b... |
| **DEFAULT_BUYER_[SITE]** | Purchasing |  | This is the userid of the default buyer for the specified site, used on all new requisitions. See DEFAULT_BUYER |
| **DEFAULT_SHIPTO** | Power Users |  | In this setting the administrator can set the default value for "Ship To" field. |
| **DEFAULT_SHIPVIA** | Purchasing |  | In this setting the administrator can set the default value for "Ship Via" field. |
| **DEFAULT_SITE** | Admin |  | In this setting the administrator can set the default value for the "Site" field. Must be a valid site. |
| **FIRST_PO_NUMBER** | Purchasing | `1` | Numeric. Starting purchase order number for sequential PO numbering. |
| **MC_BEFORE_NOTES** | Purchasing | `FALSE` | TRUE \| FALSE. If TRUE, places master comments before line notes on PO. |
| **NO_PO_PP** | ISS |  | Technical - Do Not Modify without consulting ISS |
| **PO_BLANKET_PRINT_PROGRAM** | Admin | `us/po/poblrp03.p` | QAD program name which prints blankets, should not be modified. |
| **PO_BREAK_BY** | Power Users | `xxreqd_vendor` | Comma separated list of fields on a requisition that will be used to split the requisition into multiple PO's. Or Comma separated list of fields on a requisition that will be used to consolidate PO... |
| **PO_CONFIRMATION_RESPONSE** | Power Users |  | Message to display to the supplier when the supplier confirms receipt of the PO by clicking on the Confirm Receipt link in their email message. |
| **PO_DO_NOT_PRINT** | Power Users | `FALSE` | Does not print the PO when requisition is approved. |
| **PO_LOGO** | Admin |  | The value of this setting is a path to the physical file name on the app server. Ex. " or apps or iPurchase or logo or frank.jpg". If the logo is in the wdm or agents folder then you only need to p... |
| **PO_LOGO_[po_bill]** | Admin |  | This setting allows the administrator to enter a PO Logo based on the PO Bill To Field. The value of this setting is a path to the physical file name on the app server. Ex. " or apps or iPurchase o... |
| **PO_NBR_USE_QAD** | Purchasing | `FALSE` | TRUE \| FALSE. If TRUE, uses QAD system for PO number generation. |
| **PO_PREFIX** | Purchasing |  | Prefix added to purchase order numbers (e.g., PO- results in PO-12345). |
| **PO_PREFIX_FIELD** | entities |  | Can be either 'Entity' or any fields on the requisition header table. This will allow you to create different prefix or number scheme for different sites |
| **PO_PRINTER** | Admin |  | Printer name defined in QAD. If you're using Optio, Jetforms, Pics, etc, to print graphical purchase orders, enter the name of the printer here, otherwise leave blank. |
| **PO_PRINTER_BATCH_NAME** | Admin | `QADSVC` | This setting allows the administrator to set the Queue that the report will be processed on.  ex: "POPrint" QAD EE 2012 and above allows the ability to print fancy purchase orders. Requirements: Na... |
| **PO_PRINTER_OUTPUT_DIRECTORY** | Admin |  | Is a directory on the iPurchase application server where the QAD Reporting Framework will save the file. If you are using Optio, Jetforms, Pics, etc, to print graphical purchase orders, enter the n... |
| **PO_PRINTER_OUTPUT_DIRECTORY_BLANKET** | Purchasing |  | Directory path. Output folder for blanket purchase order print files. |
| **PO_PRINTER_REPORT_CODE** | Admin | `PurchaseOrderPrint ` | This setting holds the report code for the print version you are using. ex: Custom_PurchaseOrderPrint. QAD EE 2012 and above allows the ability to print fancy purchase orders. Requirements: Names Q... |
| **PO_PRINTER_REPORT_CODE_BLANKET** | Purchasing |  | Report code used for printing blanket purchase orders. |
| **PO_PRINTER_SERVER_XML** | Admin |  | This setting points iPurchase to PO printer server configuration file. ex:  or apps or test or qdt or envs or test or configs or server.xml QAD EE 2012 and above allows the ability to print fancy p... |
| **PO_PRINT_ARCHIVE_DIR** | Admin |  | Directory on application server. Enter the path to a directory on the application server where all purchase orders will be saved to when printing a revision through iPurchase for the first time. Th... |
| **PO_PRINT_ARCHIVE_IN_DB** | Admin | `TRUE` | Store Purchase Order PDF files in database. A setting of true will display a clock icon next to Purchase Order numbers in iPurchase. Clicking the clock icon will display a list of all original prin... |
| **PO_PRINT_DOMAIN_IN_FN** | ISS |  | Technical - Do Not Modify without consulting ISS |
| **PO_PRINT_OFFLINE** | Admin | `FALSE` | This setting will control when the New PO Created email and original PO Print occur. A value of FALSE, the default, will print the PO and send the email as soon as the Purchase Order is created. Mo... |
| **PO_PRINT_PDF_FORMAT** | Power Users | `PLAIN` | Prints the POs using the built in iPurchase look. Valid choices are GRAPHICAL and PLAIN. A value of PLAIN will simply take the text based QAD output and convert it to PDF. |
| **PO_PRINT_PROGRAM** | Admin | `us/po/poporp03.p` | Progress program If you have a custom purchase order print program then enter the Progress program name here. |
| **PO_PRINT_SORT** | Purchasing | `LINE` | This setting determines the value which will be used to sort the Purchase Order on the PO Print screen. |
| **PO_SIGNATURE** | Admin |  | The value of this setting is a path to the physical file name on the app server. Ex " or apps or iPurchase or signatures or frank.jpg". If the signature is in the wdm or agents folder then you only... |
| **PO_SIGNATURE_BUYER_[buyercode]** | Admin |  | This setting allows the administrator to enter a buyers signature based on the buyer's code. The value of this setting is a path to the physical file name on the app server. Ex " or apps or iPurcha... |
| **PO_SIGNATURE_BUYER_[domain code]** | Admin |  | This setting allows the administrator to enter a buyers signature based on the domain in the buyer user record The value of this setting is a path to the physical file name on the app server. Ex " ... |
| **PO_SIGNATURE_BUYER_[domain code]_[site code]** | Admin |  | This setting allows the administrator to enter a buyers signature based on the domain and the site of the buyer user record The value of this setting is a path to the physical file name on the app ... |
| **PO_SIGNATURE_BUYER_[site_code]** | Admin |  | This setting allows the administrator to enter a buyers signature based on the site in the buyer user record The value of this setting is a path to the physical file name on the app server. Ex " or... |
| **PO_SIGNATURE_ON_REPRINT** | Power Users | `TRUE` | This setting allows the administrator to print a signature on a reprint of a Purchase Order. |
| **PO_SIGNATURE_[SITE]** | Admin |  | This setting allows for multiple PO signatures based on domain and site. The value of this setting is a path to the physical file name on the app server. Ex " or apps or iPurchase or signatures or ... |
| **PO_UPDATE_GROUPS** | Admin | `$xxreq_buyer` | Comma separated list of User ID's or Group ID's that would be allowed to use the Copy or Update PO functionality (Change Order).  For buyer, set to "$xxreq_buyer".  Asterisk indicates everyone, a b... |
| **PO_UPDATE_REQ_TYPES** | Purchasing | `*` | You can control the list of requisition types that will allow a change order, or * for all requisition types. |
| **PO_UPDATE_TOLERANCE_AMOUNT** | Admin | `100` | This is the amount that a requisition can be increased by without requiring re-routing the requisition for approval. This is only for those requisitions that are UPDATING a purchase order. |
| **PO_UPDATE_TOLERANCE_PCT** | Admin | `10` | This is the percentage that a requisition can be increased by without requiring re-routing the requisition for approval. This is only for those requisitions that are UPDATING a purchase order. |
| **QX_PO_NAME** |  | `QADERP` | Name of the qxtend instance for Purchase Orders in this environment |
| **QX_PO_VERSION** |  | `eB2_3` | Version of the qxtend PO method for this environment |
| **REOPEN_PO** | Purchasing | `buyers` | Comma separated list of User ID's or Group ID's that are allowed to re-open a closed or cancelled PO via a change order. Asterisk indicates everyone, a blank indicates no one. |
| **RT_PO_REQUIRED** | Power Users |  | This setting is a list of requisition types that would set the PO Required field to True or Yes.  For example if you do not require a PO for credit card purchases and CREDIT_CARD is a Requisition T... |
| **SUPPLIER_PO_ATTACHMENTS** | Admin |  | Comma-Separated List of paths and files. This is a list of files which is to be emailed to the supplier as attachments to the Purchase Order. |
| **SUPPLIER_PO_MERGE_ATTACHMENTS** | Purchasing |  | This setting is where the filename, with the full path to the pdf file or a space delimited list of pdf files that are to be merged in to the PO PDF file which is printed. If you're on windows then... |

---

## QAD Integration

| Setting | Owner | Default | Description |
|---------|-------|---------|-------------|
| **AS400OUTBOUNDFOLDER** | Admin |  | Directory path on application server. Folder where AS400 catalog XML files are written. Files are named [req_nbr].xml. Used in catalog integration. |
| **QAD_COMMENT_TYPE** | Admin | `IP` | This is the comment type to be used when creating PO Header and PO Line comments.  Add IP To Generalized Codes if there are any generalized codes for field name cd_type |
| **QAD_INTERFACE_PASSWORD** | ISS |  | ⚠️ SENSITIVE. Password for QAD system integration user. |
| **QAD_REQUESTED_BY** | Power Users |  | This setting will use OBO as the Requested By. If you set QAD_REQUESTED_BY to "ORIGINATOR" then the req originator (xxreq_userid) will be used. |
| **SKIP_QAD_ACTIVE_CHECK** | Admin | `TRUE` | True or False Do not check the QAD user's active flag. Normally a user (if the QAD User ID matches the iPurchase User ID) needs to be active in QAD in order to login to iPurchase. This does not alw... |
| **SKIP_QAD_DOMAIN_CHECK** | ISS | `FALSE` | TRUE \| FALSE. Skip domain validation in QAD integration. |

---

## Qxtend Integration

| Setting | Owner | Default | Description |
|---------|-------|---------|-------------|
| **QX_BROKER** | ISS |  | Qxtend broker server address for Qxtend integration. |
| **QX_CODEPAGE** | ISS |  | Character encoding for Qxtend communication. |
| **QX_URL** | ISS |  | Qxtend service URL. |
| **QX_VERSION** | ISS |  | Qxtend version number. |

---

## RFQ Management

| Setting | Owner | Default | Description |
|---------|-------|---------|-------------|
| **IRFQ** | Purchasing | `FALSE` | TRUE \| FALSE. Enable iRFQ (RFQ management) module. |
| **RFQ_BODY** | Purchasing |  | Email body template for RFQ emails. |
| **RFQ_SUBJECT** | Purchasing | `Request for Quote` | Email subject for RFQ emails. |

---

## Receiving

| Setting | Owner | Default | Description |
|---------|-------|---------|-------------|
| **ALLOW_RECEIVING** | Purchasing |  | Can-Do list. Users/groups allowed to receive against purchase orders. Can include $xxreq_buyer to allow the buyer on the PO to receive. |
| **AUTO_RECEIVE** | Purchasing | `FALSE` | TRUE \| FALSE. If TRUE, automatically creates receipt transactions when purchase order is created. Timing controlled by AUTO_RECEIVE_TIME setting. |
| **AUTO_RECEIVE_TIME** | Purchasing |  | Time value. Timestamp used when AUTO_RECEIVE creates automatic receipt records. Must be configured correctly when AUTO_RECEIVE is enabled. |
| **BUDGET_HIDE_RECEIPTS** | Admin | `TRUE` | Do not show nor use the Receipts column on Budgets. |
| **LAST_RECEIPT_ID** | ISS |  | iPurchase process receipts in QAD for budgets. It periodically looks for receipts in batch. When implementing you can set the tr_id to start from so that it does not spend time looking at old recei... |

---

## Reporting & Inquiry

| Setting | Owner | Default | Description |
|---------|-------|---------|-------------|
| **EXCEL_EXPORT_FIELDS** | IT | `xxreq_domain,xxreq_vendor,xxreq_entry_date,xxreq_nbr,xxreq_userid,xxreq_buyer,xxreq_type,xxreq_site,xxreqd_item,xxreqd_desc,xxreqd_qty,xxreqd_cost,xxreqd_po_nbr,xxreqd_po_line` | This is the list of fields that will be exported from the requisition workbench. Any requisition header field or line field can be used. You can also use PO and PO line fields. Some common PO/PO Li... |
| **EXCEL_EXPORT_ONE_TAB** | Power Users | `TRUE` | Will export a consolidated view of the requisition when the Excel link is clicked in Requisition Inquiry. Default FALSE |
| **INQUIRY_AFTER_REJECT** | Power Users | `*` | Comma separated list of User ID's or Group ID's that are re-directed to the pending queue once they have rejected a requisition. Asterisk indicates everyone, a blank indicates no one. This setting ... |
| **INQUIRY_LAST_REV_DEFAULT** |  | `TRUE` | Setting this to true will check the Last Revision Only in the requisition inquiry. This is useful when you only want to see the requisition for the last revision of a PO. As opposed to all the requ... |
| **INQUIRY_NOTES_MATCHES** | Admin | `FALSE` | When searching requisitions by using the notes field, use 'matches' vs 'contains', matches can be much slower but more flexible. |
| **INQUIRY_NO_NAME_SEARCH** | Power Users | `FALSE` | If this setting is set to true then when a user searches for a supplier they will not be allowed to search by name, only by supplier number. a value of false enables the user to search by both supp... |
| **INQUIRY_REFRESH_SECONDS** | Power Users | `120` | How often the system automatically refreshes the inquiry screen in seconds. |
| **INQUIRY_SIMPLE_MODE** | Admin |  | Comma separated list of User ID's or Group ID's who only gets to see "Views" on inquiry screen and does not see all the filter fields. This can be used as requisition security. Asterisk indicates e... |

---

## Requisition Types

| Setting | Owner | Default | Description |
|---------|-------|---------|-------------|
| **RT_MEMO_ONLY_LIST** | Finance | `Expense,Capital` | Comma-separated list of requisition types. All line items created for the requisition types defined will be entered as Memo Items on the Purchase Order. |
| **RT_USE_LOCATION** | Purchasing | `Inventory` | List of requisition types which will allow a Item Location to be entered during line item entry |

---

## Requisitions

Settings that control requisition entry, validation, defaults, and requisition-related behavior.

**Configure these settings when you need to:**
- Configure requisition defaults
- Set up validation rules
- Control requisition numbering
- Configure requisition types

**Common questions this answers:**
- How do I configure requisition defaults?
- How do requisition numbers work?
- How do I set up requisition types?

### Settings

| Setting | Owner | Default | Description |
|---------|-------|---------|-------------|
| **ADD_REQ_NBR_TO_PO** | Purchasing | `FALSE` | When a PO is created do you want to add the requisition number and line to pod_req and pod_req_line fields. This should be set to False if using 2009SE or above; or if GRS is being used |
| **ALLOW_NEGATIVE_LINE** | Purchasing |  | Can-Do list. Users/groups allowed to enter negative quantities on requisition line items. Normally rejected with error message. |
| **ALLOW_NEW_REQUEST** | Purchasing |  | Can-Do list. Users/groups allowed to create new requisitions. Controls visibility of New Request button in UI. |
| **ALLOW_SAVE_TEMPLATE** | Purchasing |  | Can-Do list. Users/groups allowed to save requisition templates. |
| **AUDIT_XXREQ_MSTR_EXCEPT** | ISS | `xxreq_cost,xxreq_word_idx,xxreq_word_idx2,xxreq_word_idx3,xxreq_master_comments,xxreq_submit_date,xxreq_submit_attempts,xxreq_submit_date,xxreq_approved,xxreq_app_by,xxreq_submitted` | Technical - Do Not Modify without consulting ISS |
| **AUTO_REQ_TYPE_DISABLE** | Admin | `FALSE` | Disable the requisition type field when there is at least one line item on a requisition - DO NOT MODIFY |
| **CODE_LIST_H_XXREQ_UCHAR1** | Admin | `List:True:Yes,False:No` | List for User Field 1 |
| **CODE_LIST_H_XXREQ_UCHAR2** | Admin | `List:1:Maybe,2:Maybe Not` | List for User Field 2 |
| **CODE_LIST_H_XXREQ_UCHAR3** | Admin | `List:Apples:Apples,Bananas:Bananas,Oranges:Oranges` | List for User Field 3 |
| **CODE_LIST_H_XXREQ_UCHAR4** | Admin | `List:True:True,False:False` | List for User Field 4 |
| **CODE_LIST_H_XXREQ_UCHAR5** | Admin | `List:True:Choice 1,False:Choice 2` | List for User Field 5 |
| **DELIVER_TO_BLANK_DEFAULT** | Purchasing |  | Default deliver-to value used when deliver-to field is left blank on requisition. |
| **EMT_REQ_TYPE** | Admin |  | Technical - Do Not Modify without consulting ISS |
| **ITEM_ADD_DESC2_ALLOW_BLANK** | Purchasing | `FALSE` | TRUE \| FALSE. If TRUE, allows adding catalog items with blank secondary description. |
| **MRO_ITEMS_REQ_TYPES** | Purchasing |  | Comma-separated requisition types. Types that allow MRO (Maintenance, Repair, Operations) items. |
| **PURGE_REQ_DAYS** | Admin | `90` | This setting allows the administrator to set how many days a requisition will be purged based on no activity from either the entry date, last audit record date(header or detail), or last approval r... |
| **PURGE_REQ_NOTIFY_DAYS** | Admin | `10` | This setting allows the administrator to set how many days in advanced the originator will get notified before a requisition is purged from the iPurchase system. The setting works in conjunction wi... |
| **REQUISITION_PREFIX** | Power Users | `T` | This setting allows the administrator to set a special character to be used for the requisition prefix. |
| **REQUISITION_TYPES** | Finance | `List:Expense:Expense,Capital,Contract,Tooling,Other,` | Use the prefix "LIST:" followed by a comma-separated list of values. This will tell iPurchase that the specified list is to be used. Example: LIST:expense:Expense Req,Capex,Inventory,etc All the sy... |
| **REQ_INQUIRY_BUYER_ALWAYS** | Purchasing | `FALSE` | TRUE \| FALSE. If TRUE, buyers can always see all requisitions in inquiry. |
| **REQ_INQUIRY_FIELDS** | Power Users |  | Comma separated list of fields that will be shown as columns in requisition inquiry. |
| **REQ_INQ_HIDDEN_ELEMENTS** | ISS |  | Technical - Do Not Modify without consulting ISS |
| **REQ_MNT_HIDDEN_ELEMENTS** | Power Users |  | Technical - Do Not Modify without consulting ISS |
| **REQ_MNT_HIDDEN_HEADER_FIELDS** | Power Users | `h_production,h_xxreq_uchar1,h_xxreq_uchar2,h_xxreq_uchar3,h_xxreq_uchar4,h_xxreq_uchar5,h_all_items,h_supplier_fax,h_req_perf,h_req_cons,h_xxreq_blanket,h_high_priority` | Comma separated list of fields that are hidden at the header. This should not be changed unless you want to hide other header fields. |
| **REQ_MNT_HIDDEN_LINE_FIELDS** | Power Users | `h_line_xxreqd_tax_usage,h_line_xxreqd_tax_class,h_line_xxreqd_tax_env,h_xxreqd_uchar1,h_xxreqd_uchar2,h_xxreqd_uchar3,h_xxreqd_uchar4,h_xxreqd_uchar5,h_xxreqd_uchar6,h_xxreqd_uchar7,h_xxreqd_uchar8,h_xxreqd_uchar9,h_xxreqd_uchar10,h_xxreqd_ulog1,h_xxreqd_ulog2,h_xxreqd_ulog3,h_xxreqd_ulog4,h_xxreqd_ulog5,h_line_project,h_line_tool_id,h_line_ar,h_line_vendor,h_line_vendor_name,h_line_mro_type,h_line_po_nbr,h_line_perf_date,h_line_freight_cost,h_line_other_cost` | These are the list of fields that are hidden at the line level. These should not be changed unless you want to hide other line fields. |
| **RT_INVENTORY_ITEM_ONLY** | Purchasing |  | Comma-separated req types. Types that require items to be in inventory catalog. |
| **RT_[Requisition Type]_ACCESS** | Finance | `*` | Comma separated list of User ID's or Group ID's that are allowed to create a requisition for the given requisition type. Asterisk indicates everyone, a blank indicates no one. All other users will ... |
| **RT_[Requisition Type]_ACCOUNT_DEFAULT** | Finance |  | Substitute the requisition type for "[REQUISITION TYPE]". This is the default Account to be used for the specified requisition type |
| **RT_[Requisition Type]_ACCOUNT_RANGE** | Finance |  | Substitute the requisition type for "[REQUISITION TYPE]". This setting allows specifying valid accounts for a specific requisition type. The field uses the Progress "Can-Do" function. See Progress ... |
| **RT_[Requisition Type]_ACCOUNT_READONLY** | Admin |  | TRUE or FALSE Substitute the requisition type for "[REQUISITION TYPE]". This setting determines whether the users can change the account during line entry and is specific to the requisition type sp... |
| **RT_[Requisition Type]_DEFAULT_BUYER** | Purchasing |  | See DEFAULT_BUYER |
| **RT_[Requisition Type]_DEPT_DEFAULT** | Finance |  | Substitute the requisition type for "[REQUISITION TYPE]". This is the default Department to be used for the specified requisition type. It will override the default department specified on the user... |
| **RT_[Requisition Type]_DEPT_RANGE** | Finance |  | Substitute the requisition type for "[REQUISITION TYPE]". This setting allows specifying valid departments (cost centers) for a specific requisition type. The field uses the Progress "Can-Do" funct... |
| **RT_[Requisition Type]_DEPT_READONLY** | Admin |  | TRUE or FALSE Substitute the requisition type for "[REQUISITION TYPE]". This setting determines whether the users can change the department during line entry and is specific to the requisition type... |
| **RT_[Requisition Type]_GL_OVERRIDE** | Finance | `False ` | True or False If you set this setting to TRUE, then all items entered in the line entry screen for the specified requisition type will have the account, sub-account, and cost center set to the valu... |
| **RT_[Requisition Type]_INVENTORY_ITEM_ONLY** | Admin |  | True or False For Inventory as an example, only Inventory items can be purchased |
| **RT_[Requisition Type]_REQUIRE_PROJECT** | Admin |  | Comma separated list of requisition types which will require a project code listed. |
| **RT_[Requisition Type]_SUB_ACCOUNT_DEFAULT** | Finance |  | Substitute the requisition type for "[REQUISITION TYPE]". This is the default Sub Account to be used for the specified requisition type. |
| **RT_[Requisition Type]_SUB_ACCOUNT_RANGE** | Finance |  | Substitute the requisition type for "[REQUISITION TYPE]". This setting allows specifying valid sub accounts for a specific requisition type. The field uses the Progress "Can-Do" function. See Progr... |
| **RT_[Requisition Type]_SUB_ACCOUNT_READONLY** | Admin |  | TRUE or FALSE Substitute the requisition type for "[REQUISITION TYPE]". This setting determines whether the users can change the sub account during line entry and is specific to the requisition typ... |
| **RT_[Requisition Type]_[SITE]_DEFAULT_BUYER** | Purchasing |  | See DEFAULT_BUYER |
| **RT_[Requisition Type]_[Site]_ACCOUNT_RANGE** | Finance |  | Substitute the requisition type for "[REQUISITION TYPE]" and site for "[SITE]". This setting allows specifying valid accounts for a specific requisition type and site specified. The field uses the ... |
| **RT_[Requisition Type]_[Site]_ACCOUNT_READONLY** | Admin | `False ` | TRUE or FALSE Substitute the requisition type for "[REQUISITION TYPE]" and site for "[SITE]". This setting determines whether the users can change the account during line entry and is specific to t... |
| **RT_[Requisition Type]_[Site]_DEPT_DEFAULT** | Finance |  | Substitute the requisition type for "[REQUISITION TYPE]" and site for "[SITE]". This is the default Department to be used for the specified requisition type and site. It will override the default d... |
| **RT_[Requisition Type]_[Site]_DEPT_RANGE** | Finance |  | Substitute the requisition type for "[REQUISITION TYPE]" and site for "[SITE]". This setting allows specifying valid departments (cost centers) for a specific requisition type. The field uses the P... |
| **RT_[Requisition Type]_[Site]_DEPT_READONLY** | Finance |  | TRUE or FALSE Substitute the requisition type for "[REQUISITION TYPE]" and site for "[SITE]". This setting determines whether the users can change the department during line entry and is specific t... |
| **RT_[Requisition Type]_[Site]_GL_OVERRIDE** | Finance | `False ` | True or False If you set this setting to TRUE, then all items entered in the line entry screen for the specified requisition type and site combination will have the account, sub-account, and cost c... |
| **RT_[Requisition Type]_[Site]_SUB_ACCOUNT_DEFAULT** | Finance |  | Substitute the requisition type for "[REQUISITION TYPE]" and site for "[SITE]". This is the default Sub Account to be used for the specified requisition type and site combination. |
| **RT_[Requisition Type]_[Site]_SUB_ACCOUNT_RANGE** | Finance |  | Substitute the requisition type for "[REQUISITION TYPE]" and site for "[SITE]". This setting allows specifying valid sub accounts for a specific requisition type and site combination. The field use... |
| **RT_[Requisition Type]_[Site]_SUB_ACCOUNT_READONLY** | Admin |  | TRUE or FALSE Substitute the requisition type for "[REQUISITION TYPE]" and site for "[Site]". This setting determines whether the users can change the sub account during line entry and is specific ... |
| **SYNC_REQ_DET** | Purchasing | `TRUE` | A setting of True will synchronize iPurchase Requisition Lines with the requisition (req_det) functionality in QAD. Only items which are planned by MRP will be synchronized |

---

## Security & Authentication

Settings for user authentication, SSO, password policies, session management, and security controls.

**Configure these settings when you need to:**
- Configure SSO/SAML settings
- Set password policies
- Control session timeouts
- Configure security permissions

**Common questions this answers:**
- How do I configure SSO?
- What are the password requirements?
- How do session timeouts work?

### Settings

| Setting | Owner | Default | Description |
|---------|-------|---------|-------------|
| **ADMIN_IP** | Admin |  | Comma-separated IP addresses. Restricts admin features to specific IP addresses. If blank, all IPs are allowed. Used for IP-based access control. |
| **ALLOW_CHANGE_PASSWORD** | Admin | `*` | Comma separated list of User IDs or Group ID's that are allowed to change passwords. Asterisk indicates everyone, a blank indicates no one. This setting determines whether a user will have the opti... |
| **ALLOW_MULTIPLE_SESSIONS** | Admin | `FALSE` | TRUE \| FALSE. If TRUE, allows users to have multiple simultaneous login sessions. SECURITY RISK if enabled without proper controls. |
| **FAILED_LOGIN_ATTEMPTS** | Power Users | `3` | Identifies how many consecutive failed login attempts will be allowed before disabling a user |
| **IGNORE_IPADDR_SECURITY** | IT | `TRUE` |  |
| **IGNORE_PASSWORDS_ON_TEST** | IT | `TRUE` | TRUE \| FALSE. When TRUE and the environment variable TEST_SYSTEM=TRUE, allows users to login with blank passwords. Used for dev/test environments to simplify testing without requiring password man... |
| **LOGIN_BACK_IN_OFFICE** | Power Users | `ASK` | If you currently have the Out-Of-Office setting on, this setting can automatically turn it off when you login. A setting of "ASK" will prompt the user if they want to turn off OOF, but only once ev... |
| **LOGIN_GOTO_CATALOG** | Admin |  | Comma Separated list of User ID's or Group ID's that will be directed to the catalog screen as their landing page. Asterisk indicates everyone, a blank indicates no one. |
| **LOGIN_GOTO_MNT** | Power Users | `TRUE` | Comma separated list of User ID's or Group ID's that will always be logged into the requisition workbench. This only applies to non-approvers. Asterisk indicates everyone, a blank indicates no one. |
| **LOGIN_HIDE_FORGOT_PASSWORD** | Admin |  | Hide the Forgot Password link on the login screen |
| **LOGIN_HIDE_KEEP_ME_LOGGED_IN** | Admin |  | Hide the Keep me logged in link on the login screen |
| **LOGIN_HIDE_REQUEST_ACCESS** | Admin |  | Hide the Request Access link on the login screen |
| **LOGIN_LIMIT_TO** | Admin |  | Comma separated list of User ID's or Group ID's that are allowed to login to the system. This setting is used for when putting the system in Admin mode (upgrade or new release). Asterisk indicates ... |
| **LOGIN_USE_AD** | Admin |  | Auto login user if using NTLM Active Directory security. |
| **LOGIN_USE_AD_CMD** | Admin |  | Command for AD authentication validation. |
| **LOGIN_USE_AD_URL** | Admin |  | URL for AD authentication service. |
| **LOGIN_USE_SSO** | Admin | `FALSE` | TRUE \| FALSE. Enable SSO authentication. |
| **LOGIN_VIEW_CONTENT** | Power Users | `1,0,1` | This setting allows the administrator to turn off the recent news, events, and video sections from the login page.  To turn these functions off the administrator would need to change the default se... |
| **NO_PASSWORD_ON_APPROVE** | Admin |  | Comma separated list of User ID's or Group ID's that will not be prompted for their password when approving or rejecting a requisition.  Asterisk indicates everyone, a blank indicates no one. |
| **NO_QAD_AUTHENTICATION** | Admin | `true` | Do not use QAD passwords for users that are also in QAD. Let iPurchase manage those passwords. |
| **PASSWORD_EXPIRE_DAYS** | Admin | `45` | This setting allows the administrator to set how often passwords need to be reset. |
| **PASSWORD_REMINDER_DAYS** | Admin | `7` | This setting allows the administrator to set how many days before the password expires to notify user when logging in. |
| **PASSWORD_RESET_TIMEOUT** | Admin |  | Technical - Do Not Modify without consulting ISS |
| **PASSWORD_RULES** | Admin | `1,0,0,0,0,6,0` | Comma-Separated list of preferences (no spaces). There are 7 entries in this field: 1. Require a number in the password 2. Require a non alpha-numeric character in the password 3. Require a number ... |
| **REMOVE_SAVE_PASSWORD** | Admin | `FALSE` | Removes the options of saving your password on the login screen. Users will need to enter their password every time. |
| **SSO_CLIENT_REDIRECT_URL** | Admin |  | URL to redirect to after SSO authentication. |
| **UNSAFE_ID_CHARACTERS** | Admin |  | Characters prohibited in user IDs and identifiers for security. |

---

## System Configuration

General system settings for iPurchase configuration, logging, performance, and system-wide behavior.

**Configure these settings when you need to:**
- Configure system defaults
- Set up logging and debugging
- Control system-wide behavior

**Common questions this answers:**
- How do I configure system settings?
- Where are system logs?
- How do I enable debugging?

### Settings

| Setting | Owner | Default | Description |
|---------|-------|---------|-------------|
| **AUDIT_TABLE_EXCEPT** | Admin |  | Comma-separated field names. Fields to exclude from audit trail for the specified table. Replace {TABLE} with actual table name (e.g., AUDIT_xxreq_mstr_EXCEPT). Used to reduce audit trail volume. |
| **CODE_LIST_H_CREDIT_TERMS** | Admin |  | LIST format. Dropdown values for credit terms. Format: LIST:code:description,code:description |
| **COMPANY_NAME** | Admin |  | Company name displayed on reports, purchase orders, and printed documents. |
| **DEFAULT_ACCT** | Admin |  | The Default Account is used when creating requisition from catalogs and punchouts. The order in which iPurchase determines the account for a requisition created from a Punchout or Catalog is as fol... |
| **DEFAULT_BILLTO** | Finance |  | The administrator can enter a default value for the "Bill To" field. |
| **DEFAULT_BLANKET_CYCLE** | Purchasing |  | After the administrator has added values to the CODE_LIST_H_BLANKET_CYCLE setting, they can add one of the values in that setting to this setting, to be the default value for the cycle code drop do... |
| **DEFAULT_CC** | Finance |  | Administrator can set the default Cost Center or Departments for Punchouts and Catalog orders. |
| **DEFAULT_CURRENCY** | Finance |  | The administrator can set a default currency for iPurchase.  Must be a valid currency. |
| **DEFAULT_FREIGHTTERMS** | Finance |  | Administrator can set the default value for "Who's Paying Freight" field. |
| **DEFAULT_LEADTIME** | Purchasing | `0` | This setting will set the number of days to add to today's date in order to calculate the Need Date on the requisition header. |
| **DEFAULT_REQTYPE** | Power Users |  | In this setting the administrator can set the default value for "Requisition Type" field. |
| **EA_EXPORT_FOLDER** | Admin |  | Directory path on application server. Folder where Enterprise Analytics export files are written. |
| **EXCEL_EXPORT_APPROVALS** | Admin | `FALSE` | TRUE \| FALSE. If TRUE, allows exporting approval data to Excel format. |
| **FILE_UPLOAD_TYPES** | Admin |  | Comma-separated file extensions. Allowed file types for document uploads (e.g., pdf,doc,docx,xlsx). |
| **JOB_RETRY_EMAIL_LAST** | Admin | `FALSE` | TRUE \| FALSE. If TRUE, sends failure email only on final retry attempt rather than every failure. |
| **LICENSE** | Admin |  | Software license key for iPurchase application. |
| **NOTES_POPUP** | Admin | `FALSE` | TRUE \| FALSE. If TRUE, displays notes in popup window instead of inline. |
| **PRINT_COMMAND** | Admin |  | OS command for printing documents (e.g., lp, lpr). |
| **SHOW_INVOICE_INQUIRY** | Admin | `FALSE` | TRUE \| FALSE. Show invoice inquiry link. |
| **SHOW_PO_REV_ON_INQUIRY** | Admin | `FALSE` | TRUE \| FALSE. Show PO revision number on inquiry. |
| **SHOW_PO_STATUS_ON_REQ_INQUIRY** | Admin | `FALSE` | TRUE \| FALSE. Show PO status on requisition inquiry. |
| **SHOW_REQ_REV_ON_INQUIRY** | Admin | `FALSE` | TRUE \| FALSE. Show requisition revision on inquiry. |
| **SHOW_SO_INQUIRY** | Admin | `FALSE` | TRUE \| FALSE. Show sales order inquiry link. |
| **SMS_TO** | Admin |  | Phone numbers for SMS notifications. |
| **TEST_SETTINGS** | Admin |  | Comma-separated list of environment-specific settings that should be preserved when copying production database to dev/test. When production DB is copied down, these settings would be overwritten w... |
| **TEST_SYSTEM** | Admin | `FALSE` | ⚠️ DEPRECATED - Use OS environment variable TEST_SYSTEM instead. This setting is no longer used. Set TEST_SYSTEM=TRUE as an environment variable on the broker/PASOE instance for dev/test environments. |
| **WINDOWS_TASK_NAME** | Admin |  | Windows Task Scheduler task name for iPurchase scheduled jobs. |
| **WORK_DAY_START_TIME** | Admin | `08:00` | Time (HH:MM). Start of business day for escalations/notifications. |
| **WORK_DAY_STOP_TIME** | Admin | `17:00` | Time (HH:MM). End of business day for escalations/notifications. |

---

## Uncategorized

| Setting | Owner | Default | Description |
|---------|-------|---------|-------------|
| **ADVISE_GROUP_MEMBERS** | Power Users | `FALSE` | This setting will send out emails to other users in a group when one of the group members approves a requisition when set to true. |
| **ALLOWED_DOMAINS** | ISS | `QAD` | Enter a comma-separated list of domain codes to be allowed in iPurchase. This can be changed for a given user in User Maintenance |
| **ALLOWED_EXTENSIONS** | Admin | `!exe,!dll,!js*,!com,!bat,!lnk,!ws*,!scr,!msi,*` | This is a comma separated list of allowed or not-allowed file extensions which can be uploaded to iPurchase. This works using the Progress "can-do" function. See Progress Help if needed A default v... |
| **APP_RULE_FIELDS** | ISS |  | List of field name from xxreq_mstr and xxreqd_det which appear in the Approval Rule Maintenance Screen for which you want to change the labels for. This list must match in size with the list in set... |
| **APP_RULE_LABELS** | ISS |  | List of labels for the fields listed in setting APP_RULE_FIELDS |
| **APP_RULE_SKIP_FIELDS** | ISS |  | List of fields from xxreq_mstr and xxreqd_det that you don't want to show in the Approval Rule Maintenance Screen. |
| **ARCHIVE_FOLDER** | IT | `archive` | This should not be changed unless advised by ISS Group This is a temporary storage area for requisitions being transferred to or from the production and archive systems |
| **AUDIT_TRAIL_ACTION_LIST** | ISS | `,Create,Delete,Write` | Technical - Do Not Modify without consulting ISS |
| **AUDIT_TRAIL_DOMAIN_EXEMPTION** | ISS | `pf_mstr,wus_mstr,wgr_mstr,wugr_mstr` | Technical - Do Not Modify without consulting ISS |
| **AUDIT_TRAIL_TABLE_LABEL** | ISS | `,Requisition Detail,Requisition Header,Rule Field,Rule Header,System Settings,Group Master,User Group Relations,User Master` | Technical - Do Not Modify without consulting ISS |
| **AUDIT_TRAIL_TABLE_LIST** | ISS | `,xxreqd_det,xxreq_mstr,xxappfield,xxapprule,pf_mstr,wgr_mstr,wugr_mstr,wus_mstr` | Technical - Do Not Modify without consulting ISS |
| **AUDIT_TRAIL_[XXX]** | ISS |  | There are several settings all beginning with "AUDIT_TRAIL". These setting should not be updated as they have to do with the internals of the Audit Trail Inquiry. |
| **AUDIT_TRANSACTION_LIST** | ISS |  | Technical - Do Not Modify without consulting ISS |
| **AUDIT_WUS_MSTR_EXCEPT** | ISS | `wus_last_login` | Technical - Do Not Modify   The list of fields from the wus_mstr table will not be audited when changed. All other fields will show up in Audit when changed. |
| **AUDIT_XXREQD_DET_EXCEPT** | ISS | `xxreqd_master_comments,` | Technical - Do Not Modify without consulting ISS |
| **AUTO_ADD_DROPSHIP** | Admin | `FALSE` | True or False - Default FALSE. Automatically adds "Dropship" as an option in the Ship To dropdown field in Requisition Workbench |
| **AUTO_ADD_ITEM_MC_TYPES** | Purchasing | `PO` | In QAD master comments, there is a reference number to identify a master comment, if this reference number equals the items number then the master comment will be added to the requisition automatic... |
| **AUTO_CHANGE_GL** | Power Users | `TRUE` | If your company's GL Account, Sub Account, and CC are set by having defaults at the Requisition or Requisition or Site level, then the GL information will change when you change Requisition Types. ... |
| **BACKUP_DB** | Admin | `../db/ipurchase.db` | iPurchase provides a rudimentary backup system. List the full pathname and database name of the iPurchase database |
| **BACKUP_DB_KEEP_DAYS** | Admin | `7` | How many days worth of iPurchase database backups to keep |
| **BACKUP_DB_PATH** | Admin | `../dbbackups` | The location where database backups are stored |
| **BASE_NAME** | ISS | `/custom/ipurchase` | Technical - Do Not Modify without consulting ISS |
| **BG_COLOR_ARCHIVE** | Admin | `#FAE0A0` | The background color of the Archive System - default brown |
| **BG_COLOR_TEST** | Admin | `#d9f2e5` | The background color of the Archive System - default pink |
| **CART_BREAK_BY** | ISS | `xxcartd_det.xxcartd_vendor` | Technical - Do Not Modify without consulting ISS |
| **CART_SUM_LINES** | Admin | `False ` | Within a catalog requisition, iPurchase will add up the quantities of all the items chosen by default.  If the administrator sets this setting to true the system will display number of lines instea... |
| **CAT_IMPORT_DIR** | Admin |  | The administrator will choose a folder on application server where catalog files will be dropped (when catalogs are sent directly from supplier - not supported in base). |
| **COPY_USE_CURRENT_CONTACT** | Power Users | `FALSE` | This setting allows the system to use the current supplier data from the ERP system when a requisition is copied instead of the supplier data coming from the requisition that is being copied. |
| **CURRENCY_SYMBOLS** | ISS | `US,$,USD,$,EUR,&euro;,GBP,&pound;,jpy,&yen;,YEN,&yen;,CHF,&#8355,ITL,&#8356,MXP,&#8369;,CAD, C$` | Comma-Separated List of Currency Codes and HTML symbol codes. For example the symbol for a Euro would be represented with the HTML code "&euro~;" Ensure to add a semi-colon before all semi-colons. |
| **DATE_FORMAT** | Admin | `mdy` | This setting allows the administrator to globally change the format of the date fields in iPurchase. |
| **DELIVER_TO_FILL_IN** | Power Users | `FALSE` | Rather than the Deliver To field being a drop down list of users defined in iPurchase, setting this to TRUE makes the deliver to field an non-validated text field. |
| **DISCREPANCY_DELETE_HIDE** | Admin | `FALSE` | If set to TRUE, will not show deleted items in the discrepancy report |
| **DMS_PROGRAM** | Admin |  | This is the name of the Progress Program which integrates with a document management system. |
| **EDIT_ANYTIME** | Admin | `buyers` | Comma separated list of User ID's or Group ID's that are allowed to edit a Pending requisition at anytime. Asterisk indicates everyone, a blank indicates no one. There is currently a setting "ALWAY... |
| **HELP_URL** |  |  | If you've developed customized help, then enter the URL to that file here. ex. https://google.com |
| **HIDE_MASTER_COMMENTS** | Admin |  | Comma separated list of User ID's or Group ID's that will not get the master comments functionality. Asterisk indicates everyone, a blank indicates no one. |
| **IPURCHASE_VERSION** | ISS | `2023.0426` | Do Not Modify |
| **ITEM_LOOKUP_NO_VP** | Purchasing | `FALSE` | Do not show vendor parts (vp_mstr) when searching for items in line entry. |
| **ITEM_SEARCH_RECENT** | iPurchase will look for matches from previous requisitions." | `TRUE` | When entering line items |
| **LINE_REJECTION_FINAL** | Power Users | `TRUE` | If USE_LINE_APPROVALS = TRUE then you can also set whether or not any items which were previously rejected, can be re-approved by a subsequent approver. A value of TRUE will disallow anyone from ap... |
| **LOCK_OUT_MINUTES** | Admin | `10` | The number of minutes a user will be locked out after failing to login more than the value of setting FAILED_LOGIN_ATTEMPTS |
| **LOGOFF_MINUTES** | Power Users | `0` | Enter how many minutes of inactivity the system will wait until it logs a user off. |
| **LOG_PURGE_DAYS** | Admin | `30` | Many log files are generated by iPurchase. These logs are useful for a short period of time, but in the log run they need to be purged. Temporary log file will be deleted once older than a rolling ... |
| **MANDATORY_FIELDS** | Admin | `h_buyer,xh_supplier_contact,xh_supplier_phone,xh_supplier_fax,xh_deliver_to2,xh_req_type,xh_supplier_email,xh_bill_to,xh_req_need,xh_site,xh_freight_terms,xh_ship_via` | Comma-Separated list of field names. The following fields can be either mandatory or optional. h_buyer,h_supplier_contact,h_supplier_phone,h_supplier_fax,h_deliver_to2,h_req_type,h_supplier_email,h... |
| **MASTER_COMMENTS_ROLE_LIST** | Purchasing | `*` | Comma-Separated list of group ID's or "*" for all. Only members of these groups will be allowed to enter or delete master comments from a requisition. |
| **MAX_UPLOAD_MB** | IT | `10` | Maximum size in megabytes for attachments. |
| **MEMO_ONLY** | Admin | `FALSE` | If this setting is true, then a user will not be allowed to order an item# which exists in the part master (pt_mstr) table. |
| **MESSAGE_ERROR_TIMEOUT** | Power Users | `0` | This setting allows the administrator the ability to set the duration of how long the error message will stay on the screen. A value of 0 will indicate to keep the message on the screen indefinitel... |
| **MESSAGE_WARNING_TIMEOUT** | Power Users | `5` | This setting allows the administrator the ability to set the duration of how long the warning message will stay on the screen. A value of 0 will indicate to keep the message on the screen indefinit... |
| **NUMERIC_FORMAT_DECIMAL** | Admin | `.` | Usually a decimal point |
| **NUMERIC_FORMAT_SEPARATOR** | Admin | `,` | Usually a comma |
| **OOF_LIMIT_BY_DOLLARS** | Admin | `FALSE` | A setting of True will only allow a user to delegate to another user who has at least the same dollar approval level. |
| **OOF_LIMIT_TO** | Admin |  | Comma separated list of User ID's or Group ID's that that can be chosen as delegates. Asterisk indicates everyone, a blank indicates no one. |
| **OOF_NOTIFY_OLD** | Power Users | `TRUE` | A setting of TRUE will email any existing pending requisitions to the newly assigned delegate. If the setting is FALSE, the delegate will not receive an email for any existing pending requisitions.... |
| **REMOVE_ORIGINATOR_FROM_GROUP** | Admin | `TRUE` | If the originator is listed as a member of a group on the approval routing, if this person should be removed from the group set this setting to TRUE. |
| **REMOVE_ORIG_CO** | Admin | `FALSE` | This setting does not allow originator to be an approver for their own requisition for Change Orders if set to true. |
| **REMOVE_ORIG_RELEASE** | Admin | `FALSE` | If set to true, this setting will remove the originator from the approver list on blanket release requisitions. |
| **SHOW_ALLOCATION_CODES** | Admin | `FALSE` | True/false to Show/Hide allocation codes in the account dropdown in req line maintenance. |
| **SHOW_GRAPH** | Admin | `buyers,admin` | Comma separated list of User ID's or group ID's that have access to the graphing functionality. Asterisk indicates everyone, a blank indicates no one. |
| **SHOW_RULE_INFO** | Power Users | `TRUE` | This setting will show the approval rule name when hovering over the Level or Seq field in the Approval History Tab. |
| **TERMS_DISPLAY** | Purchasing | `TRUE` | This setting will display the supplier terms on the requisition header. |
| **UNSPSC_FILTER** | Purchasing | `*` | To modify this setting to control which UNSPSC codes are available to choose from. The syntax for this settings uses the CAN-DO functionality similar to a lot of the other settings. To re-cap, the ... |
| **USE_CHAINED_DELEGATES** | Power Users | `TRUE` | This setting will allow for unlimited levels of Out Of Office functionality. If user A delegates to user B, then user B also delegates to user C, can User C approve or reject a requisition on behal... |
| **USE_LYNC** | Admin | `FALSE` | This setting allows the administrator to allow the use of Lync within the iPurchase solution. Requirements: Office 2010+ with Lync installed on desktop. iPurchase website must be in the "TRUSTED SI... |
| **USE_SINGLE_LANGUAGE** | then this will be the language selected for all users and the language selection box on the login screen will not be displayed." |  | If this is set to something like en-us" |

---

## User Management

Settings for user accounts, profiles, permissions, delegation, and user-related behavior.

**Configure these settings when you need to:**
- Configure user permissions
- Set up delegation/out-of-office
- Control user defaults
- Configure supervisor relationships

**Common questions this answers:**
- How do I configure user permissions?
- How does delegation work?
- How do I set up supervisors?

### Settings

| Setting | Owner | Default | Description |
|---------|-------|---------|-------------|
| **ALLOW_BATCH_PO** | Power Users | `FALSE-ALWAYS` | This setting allows the administrator to set how the PO will be created in iPurchase. The options for this setting are: 1) FALSE - Default is set to create PO now. The last approver will still have... |
| **ALLOW_BLANKET_RELEASE** | Power Users | `buyers` | Comma separated list of User ID's or Group ID's who are allowed to create releases against blanket POs. |
| **ALLOW_BUG** | Admin |  | Can-Do list. Users/groups allowed to submit bug reports through the application interface. |
| **ALLOW_CATALOG** | Admin | `*` | Comma separated list of User ID's or Group ID's that have access to the catalog function within iPurchase. |
| **ALLOW_CATALOG_EDIT** | Power Users | `buyers` | Comma separated list of User ID's or Group ID's that are who are allowed to edit items in a Catalog within iPurchase. Asterisk indicates everyone, a blank indicates no one. In order for the user to... |
| **ALLOW_CATPO_PRICE_CHANGE** |  |  | Comma separated list of User IDs or Group ID's that are allowed to change prices on catalog and punchout items. Asterisk indicates everyone, a blank indicates no one |
| **ALLOW_CONSOLIDATION** | Power Users | `FALSE` | This setting allows the administrator to turn On or Off the consolidation feature. |
| **ALLOW_COPY_PASTE** | description | `true` | This settings controls if users can copy paste in the requisition workbench. Sometimes copying from internet or PDF files cause item number |
| **ALLOW_DELETE_NOT_SUBMITTED** | Admin | `admin` | Comma separated list of User ID's or Group ID's who are allowed to delete a requisition that has not been submitted.  Asterisk indicates everyone, a blank indicates no one. |
| **ALLOW_DELETE_PROCESSED** | Admin | `admin` | Comma separated list of User ID's or Group ID's who are allowed to delete a requisition that has been approved and a PO is already created.  Asterisk indicates everyone, a blank indicates no one. |
| **ALLOW_FEEDBACK** | Admin |  | Can-Do list. Users/groups allowed to submit feedback through the application interface. |
| **ALLOW_HOLD** | Admin | `*` | Comma separated list of User ID's or Group ID's who are allowed to put a requisition on hold while it is pending. Asterisk indicates everyone, a blank indicates no one. Example: It would go on hold... |
| **ALLOW_NEGATIVE_REQ** | Power Users |  | This setting will allow negative total requisition cost if set to True. |
| **ALLOW_OOF** | Admin | `*` | Comma separated list of User ID's or Group ID's that are allowed to set Out of office. Asterisk indicates everyone, a blank indicates no one. This setting determines whether the system will support... |
| **ALLOW_PO_LINE_HISTORY** | Power Users | `buyers` | Comma separated list of User ID's or Group ID's that are allowed to view PO Line history. Use an asterisk for everyone. Leave blank for no one. |
| **ALLOW_PO_PRINT** | Power Users | `*` | Comma separated list of User ID's or Group ID's that are allowed to print a purchase order. Use an asterisk for everyone. Leave blank for no one. |
| **ALLOW_PUNCHOUT** | Admin | `*` | Comma separated list of User ID's or Group ID's that are allowed to use punchouts. Asterisk indicates everyone, a blank indicates no one. This setting turns on or off the Punch-out functionality fo... |
| **ALLOW_PUNCHOUT_COPY** | Power Users |  | Comma separated list of User ID's or Group ID's that are allowed to copy punchout requisitions (prices may no longer be valid). Asterisk indicates everyone, a blank indicates no one. |
| **ALLOW_REQ_AUDIT** | Admin |  | Can-Do list. Users/groups allowed to view requisition audit trail. Automatically disabled in archive systems. |
| **ALLOW_REQ_ENTRY** | Admin | `*` | Comma separated list of User ID's or Group ID's that are allowed to access to the requisition entry screen.   Asterisk indicates everyone, a blank indicates no one. |
| **ALLOW_REQ_INQUIRY** | Admin | `*` | Comma separated list of User ID's or Group ID's that are allowed to access the requisition inquiry screen Asterisk indicates everyone, a blank indicates no one. |
| **ALLOW_REQ_PRINT** | Admin | `*` | Comma separated list of User ID's or Group ID's that are allowed to print requisitions.  Asterisk indicates everyone, a blank indicates no one. |
| **ALLOW_RETRANSMIT_PO** | Admin | `buyers` | Comma separated list of User ID's or Group ID's that allow user to manually transmit cXML PO to Punchout supplier.  Asterisk indicates everyone, a blank indicates no one. |
| **ALWAYS_ALLOW_ATTACHMENTS** | Admin | `buyers` | Comma-Separated list of groups. Any member of these groups will be allowed to add attachments to any req at any time, even after the req is converted to a PO. |
| **ALWAYS_ALLOW_REQ_EDITS** | Power Users |  | Comma separated list of User ID's or Group ID's that are allowed to modify any requisition at any time until it has been approved. You may also use "$xxreq_buyer" (without the quotes) as one of the... |
| **ALWAYS_ALLOW_REQ_EDIT_ORIGINATOR** | Power Users |  | The users listed here will be allowed to modify a requisition while it's being approved if the following scenarios are true: 1) They are listed as the originator or on behalf of. 2) They are an app... |
| **BUDGET_ALLOW_NEW** | Admin |  | Comma Separated list of User ID's or Group ID's who are allowed to create new budgets in iPurchase. Asterisk indicates everyone, a blank indicates no one. |
| **CATALOG_ALLOW_EXPORT** | Admin | `buyers,admin` | Comma Separated list of User ID's or Group ID's that are allowed to export catalogs.  Asterisk indicates everyone, a blank indicates no one. |
| **CATALOG_ALLOW_IMPORT** | Admin | `buyers,admin` | Comma Separated list of User ID's or Group ID's that are allowed to import catalogs.  Asterisk indicates everyone, a blank indicates no one. |
| **CATALOG_REQUEST_ALLOW_IMPORT** | Admin | `buyers,admin` | Comma Separated list of User ID's or Group ID's that can load a new approved catalog into iPurchase.  Asterisk indicates everyone, a blank indicates no one. This setting is related to CATALOG_ALLOW... |
| **EMPLOYMENT_DEPT_LIST** | Admin |  | Comma-separated department codes. Valid departments for user employment records/profiles. |
| **EMPLOYMENT_DIVISION_LIST** | Admin |  | Comma-separated division codes. Valid divisions for user employment records/profiles. |
| **INQUIRY_ALLOW_NEW_VIEWS** | Admin |  | Comma separated list of User ID's or Group ID's that are allowed to create new views in requisition inquiry. Asterisk indicates everyone, a blank indicates no one. |
| **INQUIRY_ALLOW_VIEWS** | Admin |  | Comma separated list of User ID's or Group ID's that are allowed to see views. |
| **LINE_VIEW_FIELDS** | Power Users | `xxreqd_line_type:LT:1,full_item:Item:45,xxreqd_due_date:Due::center,xxreqd_acct::15:center,xxreqd_project,xxreqd_qty,xxreqd_cost` | System default for which fields are displayed in the Requisition Item browse. |
| **QAD_INTERFACE_USER** | Admin |  | Use this setting to set the User ID for integration to QAD. This user ID will be used in QAD to create PO's. This user must be enabled in iPurchase and QAD. This user would need to be created befor... |
| **RESTRICT_USER_ACCOUNTS** | Power Users | `FALSE` | Is the Acct selection limited to those accounts defined in the user's profile? See RESTRICT_USER_DEPARTMENTS for more information on how to set the Acct field in User Maintenance |
| **RESTRICT_USER_DEPARTMENTS** | Power Users | `FALSE` | Is the department selection limited to those departments defined in the user's profile?  If the value of this is True then in User Maintenance you should set up the "Default Dept" field as follows.... |
| **RESTRICT_USER_SUB_ACCOUNTS** | Power Users | `FALSE` | Is the Sub Acct selection limited to those sub accounts defined in the user's profile? See RESTRICT_USER_DEPARTMENTS for more information on how to set the Sub Acct field in User Maintenance |
| **USER_IMPORT_FOLDER** | Admin |  | Directory path on application server. Folder where user import files are placed for processing. |
| **USER_PROFILE_FIELDS** | Admin |  | Comma-separated field names. Custom user profile fields to display/edit. |
| **VIEW_DEPARTMENT_REQS** | Admin | `FALSE` | TRUE \| FALSE. Allow viewing reqs by department. |
| **VIEW_REQS_DEPARTMENT** | Admin | `FALSE` | TRUE \| FALSE. Restrict viewing to user's department reqs. |
| **VIEW_REQS_RESTRICTED_MODE** | Admin | `FALSE` | TRUE \| FALSE. Enable restricted mode for req viewing. |
| **VIEW_SUPPLIER_DOCS** | Admin | `buyers,admin` | True or False or list of users groups. Default value is blank. Will give the users access to the "Contacts" button in Requisition Workbench |

---

## iApprove Integration

| Setting | Owner | Default | Description |
|---------|-------|---------|-------------|
| **BUDGET_USE_IAPPROVE** | Finance | `FALSE` | TRUE \| FALSE. If TRUE, uses iApprove system for budget workflows instead of iPurchase budget module. |
| **CODE_LIST_H_SHIPVIA_XREF** | Purchasing |  | This setting defines a cross-reference between the selected iPurchase ship via, and the code or description that the vendor needs to see on their electronic purchase order. Only applies to Punchout... |
| **CODE_LIST_H_SHIPVIA_XREF_[VENDOR NUMBER]** | Purchasing |  | This setting defines a cross-reference between the selected iPurchase ship via, and the code or description that the vendor needs to see on their electronic purchase order. Only applies to Punchout... |
| **IAEAMJE_MSTR_REQ_PREFIX** | ISS |  | Prefix for requisition numbers in iApprove EAM JE integration. |
| **IAVD_MSTR_REQ_PREFIX** | ISS |  | Prefix for requisition numbers in iApprove vendor integration. |
| **IA_APPROVAL_NOT_REQUIRED_EMAIL_SUBJECT** | Admin | `Approval Not Required` | Email subject line for iApprove notifications when approval is not required. |
| **IA_APPROVAL_REMINDER_EMAIL_SUBJECT** | Admin | `Approval Reminder` | Email subject line for iApprove approval reminder notifications. |
| **IA_APPROVAL_REQUIRED_AGAIN_EMAIL_SUBJECT** | Admin | `Approval Required Again` | Email subject line when iApprove document requires re-approval. |
| **IA_APPROVAL_REQUIRED_EMAIL_SUBJECT** | Admin | `Approval Required` | Email subject line for iApprove initial approval request notifications. |
| **IA_APPROVED_EMAIL_SUBJECT** | Admin | `Approved` | Email subject line when iApprove document is approved. |
| **IA_EMAIL_SUBJECT_APPEND** | Admin |  | Text appended to all iApprove email subject lines. Used for environment identification (e.g., [TEST]). |
| **IA_REJECTED_EMAIL_SUBJECT** | Admin | `Rejected` | Email subject line when iApprove document is rejected. |
| **IA_RETRACTED_EMAIL_SUBJECT** | Admin | `Retracted` | Email subject line when iApprove document is retracted by submitter. |


---

> **Note for AI/RAG:** A verbose, AI-optimized version of this documentation exists at `rag-optimized/system-settings-rag.md`. If modifying this file, regenerate the RAG version using `python3 scripts/gen_settings_rag.py`.

---
