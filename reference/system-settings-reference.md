# iPurchase System Settings Reference

Complete catalog of 550+ system settings organized by category.

---

## Table of Contents

- [ACH Integration](#ach-integration) (4 settings)
- [Approval Workflow](#approval-workflow) (48 settings)
- [Catalog & Vendors](#catalog-and-vendors) (41 settings)
- [Change Orders](#change-orders) (16 settings)
- [Code Lists & Dropdowns](#code-lists-and-dropdowns) (10 settings)
- [Custom/Product Management](#custom/product-management) (4 settings)
- [EAM Integration](#eam-integration) (3 settings)
- [Email Configuration](#email-configuration) (62 settings)
- [GL Accounts & Finance](#gl-accounts-and-finance) (38 settings)
- [Inventory & MRP](#inventory-and-mrp) (6 settings)
- [Portal Integration](#portal-integration) (1 settings)
- [Purchase Orders](#purchase-orders) (58 settings)
- [QAD Integration](#qad-integration) (6 settings)
- [Qxtend Integration](#qxtend-integration) (4 settings)
- [RFQ Management](#rfq-management) (3 settings)
- [Receiving](#receiving) (5 settings)
- [Reporting & Inquiry](#reporting-and-inquiry) (8 settings)
- [Requisition Types](#requisition-types) (2 settings)
- [Requisitions](#requisitions) (51 settings)
- [Security & Authentication](#security-and-authentication) (27 settings)
- [System Configuration](#system-configuration) (29 settings)
- [Uncategorized](#uncategorized) (65 settings)
- [User Management](#user-management) (45 settings)
- [iApprove Integration](#iapprove-integration) (13 settings)

---

## ACH Integration

| Setting | Owner | Default | Description |
|---------|-------|---------|-------------|
| [**ACH_ARCHIVE_FOLDER**](../rag-optimized/settings/ACH_ARCHIVE_FOLDER.md) | Admin |  | Directory path on application server. Archive folder where processed ACH files are moved after being polled and processed. Used in job_iaach_poller.p. Related: ACH_POLLING_FOLDER |
| [**ACH_POLLING_FOLDER**](../rag-optimized/settings/ACH_POLLING_FOLDER.md) | Admin |  | Directory path on application server. Folder where incoming ACH files (*.txt) are placed for processing by the ACH polling job. Processed files are moved to ACH_ARCHIVE_FOLDER. Used in job_iaach_po... |
| [**ATTACH_IN_DB**](../rag-optimized/settings/ATTACH_IN_DB.md) | IT | `TRUE` | Store attachments in iPurchase database (True) or store attachments on disk (False). |
| [**COPY_ATTACHMENTS**](../rag-optimized/settings/COPY_ATTACHMENTS.md) | Admin | `TRUE` | This setting indicates whether or not attachments are copied when a requisition is copied |

## Approval Workflow

| Setting | Owner | Default | Description |
|---------|-------|---------|-------------|
| [**ALLOWED_DOLLAR_INCREASE**](../rag-optimized/settings/ALLOWED_DOLLAR_INCREASE.md) | Finance | `100` | Specify the amount that an approver can increase the requisition by without having it re-routed. If the requisition amount is increased greater than the value specified here, then the requisition w... |
| [**ALLOWED_PERCENT_INCREASE**](../rag-optimized/settings/ALLOWED_PERCENT_INCREASE.md) | Finance | `10` | Specify the amount that an approver can increase the requisition by without having it re-routed. If the requisition amount is increased greater than the value specified here, then the requisition w... |
| [**ALLOW_APPROVAL_SIMULATION**](../rag-optimized/settings/ALLOW_APPROVAL_SIMULATION.md) | Admin | `*` | Comma separated list of User ID's or Group ID's that are allowed to view an Approval Simulation. Asterisk indicates everyone, a blank indicates no one. |
| [**ALLOW_APPROVER_CHANGES**](../rag-optimized/settings/ALLOW_APPROVER_CHANGES.md) | Admin | `TRUE` | This is the global setting which controls whether Approvers can be manually added or deleted from the approval routing. It also controls whether the Force Approval functionality is enabled. Also se... |
| [**ALLOW_APPROVER_CHANGES_ORIGINATOR**](../rag-optimized/settings/ALLOW_APPROVER_CHANGES_ORIGINATOR.md) | Power Users | `TRUE` | Indicates whether the originator is allowed to add or remove approvers. In order for this to be enabled, Allow_Approver_Changes must also be set to TRUE. |
| [**ALLOW_APPROVER_CHANGES_REMOVE_APPROVER**](../rag-optimized/settings/ALLOW_APPROVER_CHANGES_REMOVE_APPROVER.md) | Admin | `admin` | Allow a user to remove an approver from the routing rules.  If this is enabled and Allow_Approver_Changes_Originator is enabled then the originator will also be allowed to remove approvers from the... |
| [**ALLOW_APPROVER_CHANGES_ROLES**](../rag-optimized/settings/ALLOW_APPROVER_CHANGES_ROLES.md) | Admin | `admin` | Any member of a group in this list will be allowed to add approvers.  If Allow_Approver_Changes_Remove_Approver is also enabled, then any member of these groups is also allowed to remove approvers.... |
| [**ALLOW_DELETE_APPROVED**](../rag-optimized/settings/ALLOW_DELETE_APPROVED.md) | Admin | `admin` | Comma separated list of User ID's or Group ID's who are allowed to delete an approved requisition.  Asterisk indicates everyone, a blank indicates no one. |
| [**ALLOW_SUPERVISORS_TO_APPROVE**](../rag-optimized/settings/ALLOW_SUPERVISORS_TO_APPROVE.md) | Admin | `*` | Comma separated list of User ID's or Group ID's that are allowed to approve for a subordinate. Asterisk indicates everyone, a blank indicates no one. This setting allows a supervisor to Approve or ... |
| [**APPROVAL_EMAIL_REPLY_TO**](../rag-optimized/settings/APPROVAL_EMAIL_REPLY_TO.md) | Admin |  | Replies to approval email should go to who? Leave blank for originator. Set to 'OBO' for On behalf of. Set to any single email address. |
| [**APPROVAL_INCLUDE_FIELDS**](../rag-optimized/settings/APPROVAL_INCLUDE_FIELDS.md) | ISS |  | Comma-Separated list of fields from xxreq_mstr and xxreqd_det tables. You can limit the fields which display in the approval rules screen to only those in this list. |
| [**APPROVAL_METRICS_RED**](../rag-optimized/settings/APPROVAL_METRICS_RED.md) | Admin | `90` | This setting allows the administrator to set how long the approval time should take before it will turn red on the approval metrics.  MINUTES |
| [**APPROVAL_METRICS_YELLOW**](../rag-optimized/settings/APPROVAL_METRICS_YELLOW.md) | Admin | `30` | This setting allows the administrator to set how long the approval time should take before it will turn yellow on the approval metrics. MINUTES |
| [**APP_ORIG_OR_OBO**](../rag-optimized/settings/APP_ORIG_OR_OBO.md) | Admin | `OBO` | ORIGINATOR \| OBO. Determines whether approval rule xxapp_orig field matches against the requisition originator (xxreq_userid) or the On Behalf Of person (xxreq_obo). Affects approval rule evaluati... |
| [**APP_SUPERVISOR_SEQ**](../rag-optimized/settings/APP_SUPERVISOR_SEQ.md) | Admin | `10` | This is the Approval Level or Sequence when adding supervisors to the approval routing. |
| [**AUTO_APPROVE_FORWARD**](../rag-optimized/settings/AUTO_APPROVE_FORWARD.md) | Admin | `TRUE` | 1 if a user approves go through all other approvals where that user is listed in a group. If that user is the only member of the group, then automatically approve. 2 Last approval is never automati... |
| [**BATCH_APPROVE_GROUPS**](../rag-optimized/settings/BATCH_APPROVE_GROUPS.md) | Admin |  | Comma Separated list of User ID's or Group ID's that will allow an approver to approve multiple requisitions simultaneously from the Requisition Inquiry screen.  If the user is a member of the spec... |
| [**BATCH_APPROVE_GROUPS_ALWAYS**](../rag-optimized/settings/BATCH_APPROVE_GROUPS_ALWAYS.md) | Admin |  | Comma-Separated list of User ID's or Group ID's. By default, the setting BATCH_APPROVE_GROUPS will only allow you to batch approve for requisitions that specifically include yourself. Batch approva... |
| [**BATCH_APPROVE_GROUPS_FINAL**](../rag-optimized/settings/BATCH_APPROVE_GROUPS_FINAL.md) | Admin |  | Can-Do list. Groups allowed to perform batch approval as the final approver. Restricts batch approval to specific approval steps. |
| [**DEFAULT_LINES_TO_APPROVED**](../rag-optimized/settings/DEFAULT_LINES_TO_APPROVED.md) | Power Users | `TRUE` | If using Line Approvals, then setting this to a value of TRUE will set each line to Approved (Green) as the default each time the requisition is submitted for approval. A value of FALSE will set ea... |
| [**DEFAULT_LINES_TO_APPROVED_AUTO**](../rag-optimized/settings/DEFAULT_LINES_TO_APPROVED_AUTO.md) | Admin |  | Comma-Separated List of User ID's or Group ID's. If setting DEFAULT_LINES_TO_APPROVED is set to false, then adding a user or group to this setting will automatically approve any line items which ar... |
| [**EMAIL_NO_APPROVE_LINK**](../rag-optimized/settings/EMAIL_NO_APPROVE_LINK.md) | Admin | `FALSE` | True or False - Include link to Approve in email that goes out to approver. Default FALSE |
| [**EMAIL_SUPPLIER_PO_TO_FINAL_APPROVER**](../rag-optimized/settings/EMAIL_SUPPLIER_PO_TO_FINAL_APPROVER.md) | Power Users | `FALSE` | A value of true will send a copy of the supplier email to the final approver when the PO is created. |
| [**ESCALATION_EXCEPT_USERS**](../rag-optimized/settings/ESCALATION_EXCEPT_USERS.md) | Admin |  | Can-Do list. Users/groups exempt from approval escalation timeouts. Their pending approvals won't escalate. |
| [**ESCALATION_NO_EMAILS_TO**](../rag-optimized/settings/ESCALATION_NO_EMAILS_TO.md) | Admin |  | Can-Do list. Users/groups who do not receive approval escalation notification emails. |
| [**FORCE_APPROVAL_ROLE_LIST**](../rag-optimized/settings/FORCE_APPROVAL_ROLE_LIST.md) | Admin | `admin` | Comma Separated list of User ID's or Group ID's that are allowed to Force Approve any requisition.  Force Approval bypasses all open approvals and creates a PO. A history of this action is maintain... |
| [**IGNORE_SPVSR_LOAD**](../rag-optimized/settings/IGNORE_SPVSR_LOAD.md) | Admin |  | Can-Do list. Users to ignore when calculating supervisor approval workload in load balancing. |
| [**INQUIRY_AFTER_APPROVAL**](../rag-optimized/settings/INQUIRY_AFTER_APPROVAL.md) | Power Users | `*` | Comma separated list of User ID's or group id's that are re-directed to the pending queue once they have approved a requisition. Asterisk indicates everyone, a blank indicates no one. This setting ... |
| [**LOGIN_APPROVERS_ALWAYS_SEE_APPROVALS**](../rag-optimized/settings/LOGIN_APPROVERS_ALWAYS_SEE_APPROVALS.md) | Power Users | `*` | A comma separated list of User ID's or Group ID's that will always be logged into their pending queue, regardless of whether they do or do not have pending requisition to approve. Asterisk indicate... |
| [**MULTIPLE_APPROVALS**](../rag-optimized/settings/MULTIPLE_APPROVALS.md) | Admin | `KEEP_LAST` | When an approver or approval group appears in the approval routing more than once, which approval record is actually added to the routing. When KEEP_ALL is chosen then all approval records for the ... |
| [**NEW_REROUTE_METHOD**](../rag-optimized/settings/NEW_REROUTE_METHOD.md) | Admin | `FALSE` | TRUE \| FALSE. If TRUE, uses new rerouting algorithm for change orders. |
| [**NO_APPROVAL_EMAILS**](../rag-optimized/settings/NO_APPROVAL_EMAILS.md) | Admin |  | Comma separated list of requisition types that will not send approval emails to approvers. |
| [**NO_MGR_ROUTE_TO**](../rag-optimized/settings/NO_MGR_ROUTE_TO.md) | Admin |  | User/group. Skip supervisor chain routing and route directly to this approver. |
| [**OOF_LIMIT_TO_APPROVERS**](../rag-optimized/settings/OOF_LIMIT_TO_APPROVERS.md) | Admin | `FALSE` | A setting of TRUE will allow a user to delegate only to other Approvers. A False value will allow a user to delegate to anyone. |
| [**REMINDER_DAYS**](../rag-optimized/settings/REMINDER_DAYS.md) | Admin | `3` | Numeric. Days before sending reminder emails to pending approvers. |
| [**REMOVE_APPROVER_FROM_GROUPS**](../rag-optimized/settings/REMOVE_APPROVER_FROM_GROUPS.md) | Admin | `FALSE` | TRUE \| FALSE. If TRUE, removes approver from later groups if they already approved. |
| [**REMOVE_APPROVER_ROLE_LIST**](../rag-optimized/settings/REMOVE_APPROVER_ROLE_LIST.md) | Admin | `admin` | Comma separated list of User ID's or Group ID's that are allowed to remove an Approver from any requisition. Asterisk indicates everyone, a blank indicates no one. |
| [**REMOVE_ORIGINATOR_FROM_GROUP_CO**](../rag-optimized/settings/REMOVE_ORIGINATOR_FROM_GROUP_CO.md) | Admin | `FALSE` | TRUE \| FALSE. If TRUE, removes originator from approval routing on change orders. |
| [**ROLES**](../rag-optimized/settings/ROLES.md) | Admin |  | Comma-separated list of role names that can be assigned in the User Roles screen. These roles are combined with hard-coded Types (Account, Cost Center, Project, Site, Sub Account) to create approva... |
| [**ROLE_MISSING_SKIP_LIST**](../rag-optimized/settings/ROLE_MISSING_SKIP_LIST.md) | Admin |  | Comma-separated list of Types (Cost Center, Account, Project, Sub Account, Site). If a role mapping is missing for a Type in this list, the approval engine skips that approver silently. If a Type i... |
| [**SHOW_APPROVER_METRICS**](../rag-optimized/settings/SHOW_APPROVER_METRICS.md) | Admin | `buyers,admin` | Comma separated list of User ID's or group id's that have access to view approval time metrics in the Requisition Inquiry. Asterisk indicates everyone, a blank indicates no one. |
| [**SUPERVISOR_APPROVAL_FIELD**](../rag-optimized/settings/SUPERVISOR_APPROVAL_FIELD.md) | Admin | `wus_supervisor` | Field name. Database field used to determine supervisor chain (default: wus_supervisor). |
| [**SUPERVISOR_ESCALATION_ANYTIME**](../rag-optimized/settings/SUPERVISOR_ESCALATION_ANYTIME.md) | Admin | `FALSE` | TRUE \| FALSE. If TRUE, supervisors can approve/reject anytime, not just when pending. |
| [**SUPERVISOR_ESCALATION_DAYS**](../rag-optimized/settings/SUPERVISOR_ESCALATION_DAYS.md) | Power Users | `3` | This is the number of days which must elapse before an approver can Approve or Reject a requisition on behalf of someone else who reports to this given supervisor. See SUPERVISOR_ESCALATION_LEVEL a... |
| [**SUPERVISOR_ESCALATION_LEVEL**](../rag-optimized/settings/SUPERVISOR_ESCALATION_LEVEL.md) | Admin | `99` | This setting determines how many supervisors up the supervisor tree (organization chart) are allowed to approve or reject a requisition. A value of one will only allow the approver's immediate supe... |
| [**USE_APP_AMOUNT_OWN_REQS**](../rag-optimized/settings/USE_APP_AMOUNT_OWN_REQS.md) | Admin |  | Comma separated list of User ID's or Group ID's that indicates whether a user's requisition can be automatically converted to a PO if the user's approval amount exceeds the requisition amount. If t... |
| [**USE_LINE_APPROVALS**](../rag-optimized/settings/USE_LINE_APPROVALS.md) | Power Users | `FALSE` | This setting determines whether supervisors can approve or reject individual line items. Only those line items which are approved will be added to the PO. If there are any items which are neither a... |
| [**USE_SUPERVISORS_TO_APPROVE**](../rag-optimized/settings/USE_SUPERVISORS_TO_APPROVE.md) | Admin | `FALSE` | TRUE \| FALSE. Use supervisor chain for approvals. |

## Catalog & Vendors

| Setting | Owner | Default | Description |
|---------|-------|---------|-------------|
| [**ALLOW_TEMP_VENDORS**](../rag-optimized/settings/ALLOW_TEMP_VENDORS.md) | Purchasing | `FALSE` | TRUE \| FALSE. If TRUE, allows use of temporary/unverified vendors on requisitions. If FALSE, temporary vendors are rejected. |
| [**APPROVED_SUPPLIERS_ONLY**](../rag-optimized/settings/APPROVED_SUPPLIERS_ONLY.md) | Purchasing | `FALSE` | TRUE \| FALSE. If TRUE, only approved suppliers can be selected on requisitions. Enforces supplier approval workflow. |
| [**AUTO_ADD_SUPPLIER_MC_TYPES**](../rag-optimized/settings/AUTO_ADD_SUPPLIER_MC_TYPES.md) | Purchasing | `PO` | In QAD master comments, there is a reference number to identify a master comment, if this reference number equals the suppler then the master comment will be added to the requisition automatically ... |
| [**AVL_REQ_TYPES**](../rag-optimized/settings/AVL_REQ_TYPES.md) | Purchasing |  | Comma-separated requisition types. Requisition types that require Approved Vendor List validation. Related: SIG_AVL_REQ_TYPES, USE_SIG_AVL |
| [**CART_SINGLE_SUPPLIER**](../rag-optimized/settings/CART_SINGLE_SUPPLIER.md) | Purchasing | `FALSE` | TRUE \| FALSE. If TRUE, shopping cart is restricted to items from a single supplier. Mixed supplier carts are not allowed. |
| [**CATALOG_ACCESS_[Supplier NBR]**](<../rag-optimized/settings/CATALOG_ACCESS_[Supplier NBR].md>) | Admin |  | Comma separated list of User ID's or Group ID's that have access to the specified supplier catalog. If this setting does not exist for a supplier, then everyone will have access to that supplier's ... |
| [**CATALOG_CAN_DELETE**](../rag-optimized/settings/CATALOG_CAN_DELETE.md) | Admin | `admin` | Comma Separated list of User ID's or Group ID's that are allowed to delete catalogs.  Asterisk indicates everyone, a blank indicates no one. |
| [**CATALOG_CAN_RATE**](../rag-optimized/settings/CATALOG_CAN_RATE.md) | Purchasing | `FALSE` | TRUE \| FALSE. If TRUE, users can rate catalog items. Related: CATALOG_SHOW_RATING |
| [**CATALOG_CART_SHOW_DETAILS**](../rag-optimized/settings/CATALOG_CART_SHOW_DETAILS.md) | Admin | `TRUE` | This setting will show supplier, lead time, manufacturer, and UOM in the cart for a catalog if set to true. |
| [**CATALOG_DISPLAY_ROWS**](../rag-optimized/settings/CATALOG_DISPLAY_ROWS.md) | Power Users | `25` | This setting will allow the administrator to decide how many rows of items to display on a catalog requisition. |
| [**CATALOG_EXCEPTION_REQ_TYPE**](../rag-optimized/settings/CATALOG_EXCEPTION_REQ_TYPE.md) | Admin |  | If left blank the catalog exception requisition type should be set to "Catalog Exception". The administrator can change the name of the requisition type assigned to 'Catalog Exception' in this sett... |
| [**CATALOG_EXCEPTION_USER**](../rag-optimized/settings/CATALOG_EXCEPTION_USER.md) | Purchasing |  | Can-Do list. Users/groups exempt from catalog-only purchasing restrictions. Can create requisitions outside catalog. |
| [**CATALOG_ITEM_NBR_MATCH**](../rag-optimized/settings/CATALOG_ITEM_NBR_MATCH.md) | Power Users | `FALSE` | A user can search a catalog using either matches or contains criteria.  If set to True then the system will use the Match functionality. Matches:  If the item number is 12345 then you should be abl... |
| [**CATALOG_REQUEST_REQ_TYPE**](../rag-optimized/settings/CATALOG_REQUEST_REQ_TYPE.md) | ISS | `Catalog Request` | Technical - Do Not Modify |
| [**CATALOG_SHOW_DETAILS**](../rag-optimized/settings/CATALOG_SHOW_DETAILS.md) | Admin | `TRUE` | If true, the catalog screen will display supplier, lead time, minimum quantity. |
| [**CATALOG_SHOW_PICTURES**](../rag-optimized/settings/CATALOG_SHOW_PICTURES.md) | Admin | `TRUE` | If true, images of items will appear in catalogs. |
| [**CATALOG_SHOW_RATING**](../rag-optimized/settings/CATALOG_SHOW_RATING.md) | Purchasing | `FALSE` | TRUE \| FALSE. If TRUE, displays item ratings in catalog interface. Related: CATALOG_CAN_RATE |
| [**CATALOG_SORT**](../rag-optimized/settings/CATALOG_SORT.md) | ISS | `List:by uCatalog.uDomain by uCatalog.SupplierPart:Part Number (Ascending),by uCatalog.uDomain by uCatalog.SupplierPart desc:Part Number (Descending),by uCatalog.UnitPrice:Price (Low to High),by uCatalog.UnitPrice desc:Price (High to Low)` | This setting gives the administrator the option to choose the sort by in a catalog requisition |
| [**CATALOG_USE_CART**](../rag-optimized/settings/CATALOG_USE_CART.md) | Admin | `*` | Comma Separated list of User ID's or Group ID's that will use the catalog functionality in the "New Catalog Req" screen. Asterisk indicates everyone, a blank indicates no one. |
| [**CAT_REJECT_TO_SUPPLIER**](../rag-optimized/settings/CAT_REJECT_TO_SUPPLIER.md) | Admin | `False ` | If a catalog exception requisition is rejected, the supplier will receive an email if set to true. |
| [**CER_SECOND_SOURCE_AMOUNT**](../rag-optimized/settings/CER_SECOND_SOURCE_AMOUNT.md) | Purchasing |  | Dollar amount. Threshold above which second source certification is required. Related to competitive bidding requirements. |
| [**DROP_SHIP_EXCLUDE_SUPPLIER_TYPES**](../rag-optimized/settings/DROP_SHIP_EXCLUDE_SUPPLIER_TYPES.md) |  |  | Comma-Separated list of Supplier Types that should not show in the drop ship search. For example you may want to exclude employee addresses |
| [**NEW_SUPPLIER_NBRS**](../rag-optimized/settings/NEW_SUPPLIER_NBRS.md) |  |  | Comma separated list of supplier numbers which should not allow final approval. |
| [**PUNCHOUT_DISABLE_USERS**](../rag-optimized/settings/PUNCHOUT_DISABLE_USERS.md) | Purchasing |  | Can-Do list. Users/groups who are NOT allowed to use punchout functionality. |
| [**PUNCHOUT_LEADTIME**](../rag-optimized/settings/PUNCHOUT_LEADTIME.md) | Admin | `3` | The number of days to add to today's date in order to calculate the Need Date for the requisition header. Can change by supplier in Supplier Maintenance (iPurchase) |
| [**PUNCHOUT_NOFRAMES**](../rag-optimized/settings/PUNCHOUT_NOFRAMES.md) | Admin |  | iPurchase uses an HTML FRAMESET to display the Punchout website as well as the Return to iPurchase button at the top left. Some suppliers, like Amazon, will not allow the Return to iPurchase button... |
| [**PUNCHOUT_NO_ITEM_DESC**](../rag-optimized/settings/PUNCHOUT_NO_ITEM_DESC.md) | Purchasing | `FALSE` | TRUE \| FALSE. If TRUE, excludes item descriptions from punchout requests. |
| [**PUNCHOUT_REQ_TYPE**](../rag-optimized/settings/PUNCHOUT_REQ_TYPE.md) | Admin |  | This setting allows the administrator to globally set a default requisition type for punchout requisitions. |
| [**PUNCHOUT_REQ_TYPE_[supplier]**](<../rag-optimized/settings/PUNCHOUT_REQ_TYPE_[supplier].md>) | Admin |  | This setting allows the administrator to set a default requisition type by supplier for punchout requisitions. |
| [**PUNCHOUT_RETRY**](../rag-optimized/settings/PUNCHOUT_RETRY.md) | Purchasing | `3` | Numeric. Number of retry attempts for failed punchout connections. |
| [**RT_CATALOG EXCEPTION_PP**](../rag-optimized/settings/RT_CATALOG EXCEPTION_PP.md) | ISS | `catexceptload.p` | Technical - Do Not Modify without consulting ISS |
| [**RT_VENDOR_ITEM_ONLY**](../rag-optimized/settings/RT_VENDOR_ITEM_ONLY.md) | Admin |  | Comma separated list of requisition types which will mandate that an item selected to a requisition must exist in the vendor part cross-reference table in QAD. |
| [**SHOW_COST**](../rag-optimized/settings/SHOW_COST.md) | Purchasing |  | Can-Do list. Users allowed to see item costs. |
| [**SHOW_MARGIN**](../rag-optimized/settings/SHOW_MARGIN.md) | Purchasing |  | Can-Do list. Users allowed to see profit margins. |
| [**SIG_AVL_REQ_TYPES**](../rag-optimized/settings/SIG_AVL_REQ_TYPES.md) | Purchasing |  | Comma-separated types. Types using signature-based approved vendor list. Related: AVL_REQ_TYPES, USE_SIG_AVL |
| [**SUPPLIER_CONFIRMATION**](../rag-optimized/settings/SUPPLIER_CONFIRMATION.md) | Purchasing | `FALSE` | TRUE \| FALSE. Require supplier PO confirmation. |
| [**SUPPLIER_PO_MERGE_ATTACHMENTS_EXCLUDE**](../rag-optimized/settings/SUPPLIER_PO_MERGE_ATTACHMENTS_EXCLUDE.md) | Purchasing |  | Comma-separated suppliers. Suppliers excluded from attachment merging. |
| [**SUPPLIER_SEARCH_MATCHES**](../rag-optimized/settings/SUPPLIER_SEARCH_MATCHES.md) | Admin | `FALSE` | If set to True then a user can search for a supplier using any character in the suppliers name.  If set to True, the supplier lookup will run slower. |
| [**USE_SIG_AVL**](../rag-optimized/settings/USE_SIG_AVL.md) | Purchasing | `FALSE` | TRUE \| FALSE. Enable signature-based approved vendor list. Related: SIG_AVL_REQ_TYPES |
| [**VALIDATE_SUP_ITEM**](../rag-optimized/settings/VALIDATE_SUP_ITEM.md) | Purchasing | `FALSE` | TRUE \| FALSE. Validate that supplier carries the requested item. |
| [**VENDOR_ITEM_ONLY**](../rag-optimized/settings/VENDOR_ITEM_ONLY.md) | Purchasing | `FALSE` | TRUE \| FALSE. Restrict requisitions to items in vendor catalog only. |

## Change Orders

| Setting | Owner | Default | Description |
|---------|-------|---------|-------------|
| [**ALLOW_AUTO_REROUTE**](../rag-optimized/settings/ALLOW_AUTO_REROUTE.md) | Admin | `TRUE` | If an approver makes a change to a requisition, iPurchase will re-check who the approvers should be in order for the changes made. If the new approver set is different from the current approver set... |
| [**CHANGE_ORDER_CHANGE_ORIG**](../rag-optimized/settings/CHANGE_ORDER_CHANGE_ORIG.md) | Purchasing | `FALSE` | TRUE \| FALSE. If TRUE, allows changing the originator (xxreq_userid) field on purchase order change orders. |
| [**CO_DELETE_CANCELLED_LINES**](../rag-optimized/settings/CO_DELETE_CANCELLED_LINES.md) | Purchasing | `FALSE` | TRUE \| FALSE. If TRUE, permanently deletes cancelled lines on change orders. If FALSE, lines remain with cancelled status. |
| [**CO_HEADER_REROUTE_FIELDS**](../rag-optimized/settings/CO_HEADER_REROUTE_FIELDS.md) | Admin |  | Comma Separated list of header fields which will force a change order to automatically re-route if they are changed. |
| [**CO_IGNORE_COST**](../rag-optimized/settings/CO_IGNORE_COST.md) | Purchasing | `FALSE` | TRUE \| FALSE. If TRUE, cost changes are ignored when determining if change order is material (requires re-routing). |
| [**CO_ITEM_REROUTE_FIELDS**](../rag-optimized/settings/CO_ITEM_REROUTE_FIELDS.md) | Admin |  | Comma Separated list of item fields which will force a change order to automatically re-route if they are changed. |
| [**CO_ITEM_REROUTE_NEW**](../rag-optimized/settings/CO_ITEM_REROUTE_NEW.md) | Admin | `FALSE` | Automatically re-route a change order if a new line is added to the requisition. |
| [**CO_REROUTE_EXCLUDE_TYPES**](../rag-optimized/settings/CO_REROUTE_EXCLUDE_TYPES.md) | Purchasing |  | Comma-separated requisition types. Types excluded from change order re-routing even when changes are material. |
| [**PO_UPDATE_CHECK_REROUTE**](../rag-optimized/settings/PO_UPDATE_CHECK_REROUTE.md) | Admin | `TRUE` | As part of the approval process, do you want the system to compare the approvers from the original requisition to the new requisition? If there are any changes then the new requisition will be re-r... |
| [**PO_UPDATE_CHECK_REROUTE_RELEASES**](../rag-optimized/settings/PO_UPDATE_CHECK_REROUTE_RELEASES.md) | Purchasing | `FALSE` | TRUE \| FALSE. If TRUE, checks blanket PO releases for material changes requiring reroute. |
| [**PUNCHOUT_CHANGE_ORDER_SEND**](../rag-optimized/settings/PUNCHOUT_CHANGE_ORDER_SEND.md) | Admin | `*` | Send PO revisions automatically to punchout suppliers via cXML. List of Vendor Numbers or * for all. CAN-DO functionality !staples,* |
| [**UPDATE_COST_ON_CO**](../rag-optimized/settings/UPDATE_COST_ON_CO.md) | Purchasing | `FALSE` | TRUE \| FALSE. Update line costs when creating change order. |
| [**UPDATE_COST_ON_COPY**](../rag-optimized/settings/UPDATE_COST_ON_COPY.md) | Purchasing | `FALSE` | TRUE \| FALSE. Update line costs when copying requisition. |
| [**UP_ONLY_APP_LEVEL_EXCLUDED**](../rag-optimized/settings/UP_ONLY_APP_LEVEL_EXCLUDED.md) | Admin |  | Comma-separated approval levels. Approval levels to exclude from UP_ONLY rule evaluation. |
| [**UP_ONLY_REQ_TYPES**](../rag-optimized/settings/UP_ONLY_REQ_TYPES.md) | Admin |  | Comma-separated requisition types. Types that use UP_ONLY (Update PO Only) routing rule. |
| [**UP_ONLY_RULE**](../rag-optimized/settings/UP_ONLY_RULE.md) | Admin | `FALSE` | TRUE \| FALSE. Enable Update PO Only routing rule for change orders that don't require full re-routing. |

## Code Lists & Dropdowns

| Setting | Owner | Default | Description |
|---------|-------|---------|-------------|
| [**CODE_LIST_H_BILLTO**](../rag-optimized/settings/CODE_LIST_H_BILLTO.md) | Finance |  | This is a pointer to the code_mstr field name (code_fldname) value to be used for the Header Bill To selection list and validation.  Leaving this value blank will tell iPurchase to use the si_mstr ... |
| [**CODE_LIST_H_BLANKET_CYCLE**](../rag-optimized/settings/CODE_LIST_H_BLANKET_CYCLE.md) | ISS | `List:MO:Monthly,WK:Weekly,DA:Daily` | Enter a comma-separated list of cycle codes to be entered in the cycle code drop down menu on the blanket information tab on a requisition. |
| [**CODE_LIST_H_CURRENCY**](../rag-optimized/settings/CODE_LIST_H_CURRENCY.md) | Finance |  | Currency List same as other lists - blank will use all currencies from QAD - cu_mstr |
| [**CODE_LIST_H_FOB**](../rag-optimized/settings/CODE_LIST_H_FOB.md) | Finance | `po_fob` | code_fldname This is a pointer to the code_mstr field name (code_fldname) value to be used for the Header FOB selection list and validation. You can also use the prefix "LIST:" followed by a comma-... |
| [**CODE_LIST_H_SHIPTO**](../rag-optimized/settings/CODE_LIST_H_SHIPTO.md) | Admin |  | code_fldname  or  blank This is a pointer to the code_mstr field name (code_fldname) value to be used for the Header Ship To selection list and validation.  Leaving this value blank will tell iPurc... |
| [**CODE_LIST_H_SHIPVIA**](../rag-optimized/settings/CODE_LIST_H_SHIPVIA.md) | Finance | `po_shipvia` | code_fldname This is a pointer to the code_mstr field name (code_fldname) value to be used for the Header ShipVia selection list and validation. You can also use the prefix "LIST:" followed by a co... |
| [**CODE_LIST_H_SITE**](../rag-optimized/settings/CODE_LIST_H_SITE.md) | Finance |  | code_fldname This is a pointer to the code_mstr field name (code_fldname) value to be used for the Header Site selection list and validation.  Leaving this value blank will tell iPurchase to use th... |
| [**CODE_LIST_MRO_TYPE**](../rag-optimized/settings/CODE_LIST_MRO_TYPE.md) | Admin |  | code_fldname This is a pointer to the code_mstr field name (code_fldname) value to be used for the Line MRO Type selection list, and validation. You can also use the prefix "LIST:" followed by a co... |
| [**CODE_LIST_REJECTION_CODES**](../rag-optimized/settings/CODE_LIST_REJECTION_CODES.md) | Power Users | `List:001:Invalid Prices,002:Invalid Accounts` | code_fldname This is a pointer to the code_mstr field name (code_fldname) value to be used for the Rejection Code selection list and validation. A value of blank or a non-existing setting will turn... |
| [**CODE_LIST_UM**](../rag-optimized/settings/CODE_LIST_UM.md) | Finance | `pt_um` | code_fldname This is a pointer to the code_mstr field name (code_fldname) value to be used for the Line Unit of Measure selection list and validation. A value of blank or a non-existing setting wil... |

## Custom/Product Management

| Setting | Owner | Default | Description |
|---------|-------|---------|-------------|
| [**PRODUCT_MGR_GROUP**](../rag-optimized/settings/PRODUCT_MGR_GROUP.md) | Purchasing |  | Group ID for product managers. Customer-specific product management setting. |
| [**PROD_LINES_DERMIS**](../rag-optimized/settings/PROD_LINES_DERMIS.md) | Purchasing |  | Product line categorization for Dermis business unit. Customer-specific. |
| [**PROD_LINES_ORTHO**](../rag-optimized/settings/PROD_LINES_ORTHO.md) | Purchasing |  | Product line categorization for Ortho business unit. Customer-specific. |
| [**PROD_LINES_WOUND_CARE**](../rag-optimized/settings/PROD_LINES_WOUND_CARE.md) | Purchasing |  | Product line categorization for Wound Care business unit. Customer-specific. |

## EAM Integration

| Setting | Owner | Default | Description |
|---------|-------|---------|-------------|
| [**JE_USE_EAM**](../rag-optimized/settings/JE_USE_EAM.md) | Finance | `FALSE` | TRUE \| FALSE. If TRUE, uses EAM system for journal entry processing. |
| [**USE_EAM_ACCOUNTS**](../rag-optimized/settings/USE_EAM_ACCOUNTS.md) | Finance | `FALSE` | TRUE \| FALSE. Use EAM account structure. |
| [**USE_SINGLE_CURRENCY**](../rag-optimized/settings/USE_SINGLE_CURRENCY.md) | Finance | `FALSE` | TRUE \| FALSE. Force single currency mode, disable multi-currency. |

## Email Configuration

| Setting | Owner | Default | Description |
|---------|-------|---------|-------------|
| [**ALLOW_MANUAL_EMAIL_PO**](../rag-optimized/settings/ALLOW_MANUAL_EMAIL_PO.md) | Admin |  | Comma-Separated list of User ID's or Group ID's. that will have the "Email PO" option which would allow a user to email the PO through iPurchase. Asterisk indicates everyone, a blank indicates no one. |
| [**APPLICATION_URL**](../rag-optimized/settings/APPLICATION_URL.md) | Admin |  | Full application URL (e.g., https://ipurchase.company.com). Used by scheduled jobs for email links. On test/backup systems, should be updated to match environment. |
| [**APPROVAL_EMAIL_ONLY_NOPO**](../rag-optimized/settings/APPROVAL_EMAIL_ONLY_NOPO.md) | Admin | `FALSE` | TRUE \| FALSE. If TRUE, approval emails are sent only when the requisition does NOT require a PO (xxreq_po_required = TRUE). Used to reduce email volume. |
| [**BASE_URL**](../rag-optimized/settings/BASE_URL.md) | Admin |  | Base URL/hostname (e.g., https://server.company.com). Used in email notifications and scheduled job links. Should be updated on test/backup systems. |
| [**EMAILFROM**](../rag-optimized/settings/EMAILFROM.md) | Admin |  | AD Email Address This is a valid email address for which all iPurchase emails will be sent from. |
| [**EMAILSERVER**](../rag-optimized/settings/EMAILSERVER.md) | IT |  | IP Address of SMTP Server. This is the IP Address of the SMTP Server from which iPurchase sends all emails. |
| [**EMAILS_TO**](../rag-optimized/settings/EMAILS_TO.md) | Admin |  | Comma-separated email address(s) where all emails from the service will be sent to. This overrides the actual user's email addresses. |
| [**EMAIL_AUTH_PASSWORD**](../rag-optimized/settings/EMAIL_AUTH_PASSWORD.md) | Admin |  | Technical - Do Not Modify without consulting ISS |
| [**EMAIL_AUTH_TYPE**](../rag-optimized/settings/EMAIL_AUTH_TYPE.md) | Admin |  | Technical - Do Not Modify without consulting ISS |
| [**EMAIL_AUTH_USER**](../rag-optimized/settings/EMAIL_AUTH_USER.md) | Admin |  | Technical - Do Not Modify without consulting ISS |
| [**EMAIL_DEBUG_LEVEL**](../rag-optimized/settings/EMAIL_DEBUG_LEVEL.md) | Admin | `0` | Numeric 0-3. Email system debug verbosity. 0=off, 1=basic, 2=detailed, 3=verbose. Used for troubleshooting email issues. |
| [**EMAIL_DISCLAIMER_REJECT**](../rag-optimized/settings/EMAIL_DISCLAIMER_REJECT.md) |  | `If questions, please contact the approver that rejected the requisition` | If questions, please contact the approver that rejected the requisition |
| [**EMAIL_HEADER**](../rag-optimized/settings/EMAIL_HEADER.md) | Admin |  | HTML content. Custom header included in email templates. Used for branding/styling emails. |
| [**EMAIL_HELPDESK**](../rag-optimized/settings/EMAIL_HELPDESK.md) | Admin |  | Helpdesk Email Address Enter the email address for the helpdesk. Used on login screen as well as all emails. |
| [**EMAIL_HELP_TAG**](../rag-optimized/settings/EMAIL_HELP_TAG.md) | Admin | `If questions, email the $HELPDESK, or contact the originator, or approver.` | Include -- If questions, email the helpdesk link on all internal emails." |
| [**EMAIL_NEW_USER_BODY**](../rag-optimized/settings/EMAIL_NEW_USER_BODY.md) | Admin |  | This setting allows the administrator to set the body of the email that is sent to users when a new user is created. Special tokens that can be inserted in email are $User ID, $PASSWORD, $URL.  The... |
| [**EMAIL_NEW_USER_SUBJECT**](../rag-optimized/settings/EMAIL_NEW_USER_SUBJECT.md) | Admin |  | This setting allows the administrator to set the subject for the new user email. |
| [**EMAIL_NO_REJECT_LINK**](../rag-optimized/settings/EMAIL_NO_REJECT_LINK.md) | Admin | `FALSE` | True or False - Include link to Reject in email that goes out to approver. Default FALSE |
| [**EMAIL_OPEN_PO_INCLUDE_DOMAINS**](../rag-optimized/settings/EMAIL_OPEN_PO_INCLUDE_DOMAINS.md) |  | `*` |  |
| [**EMAIL_OPEN_PO_INCLUDE_TYPES**](../rag-optimized/settings/EMAIL_OPEN_PO_INCLUDE_TYPES.md) |  | `!Inventory,*` |  |
| [**EMAIL_OPEN_PO_INCLUDE_USERS**](../rag-optimized/settings/EMAIL_OPEN_PO_INCLUDE_USERS.md) |  | `*` |  |
| [**EMAIL_OPEN_PO_REMINDER_SUBJECT**](../rag-optimized/settings/EMAIL_OPEN_PO_REMINDER_SUBJECT.md) |  | `Open POs in IPurchase` |  |
| [**EMAIL_OPEN_PO_REMINDER_TEXT**](../rag-optimized/settings/EMAIL_OPEN_PO_REMINDER_TEXT.md) |  | `Below is a list of your open purchase orders` |  |
| [**EMAIL_PASSWORD_CHANGE_BODY**](../rag-optimized/settings/EMAIL_PASSWORD_CHANGE_BODY.md) | Admin |  | This setting allows the administrator to set the body of an email when the administrator changes a password.  Special token is $PASSWORD. |
| [**EMAIL_PASSWORD_CHANGE_SUBJECT**](../rag-optimized/settings/EMAIL_PASSWORD_CHANGE_SUBJECT.md) | Admin |  | This setting allows the administrator to set the subject for the password change email. |
| [**EMAIL_PO_ADDITIONAL**](../rag-optimized/settings/EMAIL_PO_ADDITIONAL.md) | Purchasing |  | Comma-separated email addresses. Additional recipients for purchase order emails beyond default recipients. |
| [**EMAIL_PO_BODY**](../rag-optimized/settings/EMAIL_PO_BODY.md) | Admin | `This should be line one. <br><br> | Allows the administrator to create a custom email body for new PO. |
| [**EMAIL_PO_BODY_REVISION**](../rag-optimized/settings/EMAIL_PO_BODY_REVISION.md) | Admin |  | Allows the administrator to create a custom email body for PO revision emails. |
| [**EMAIL_PO_INCLUDE_SIG**](../rag-optimized/settings/EMAIL_PO_INCLUDE_SIG.md) | Purchasing | `TRUE` | This setting includes the buyer's contact information for emails automatically sent to suppliers when PO is created. It also includes logged in user's contact information in emails which are manual... |
| [**EMAIL_PO_LOGO**](../rag-optimized/settings/EMAIL_PO_LOGO.md) | Admin |  | Image URL or file path. Company logo displayed in purchase order emails. |
| [**EMAIL_PO_RECEIPTS**](../rag-optimized/settings/EMAIL_PO_RECEIPTS.md) | Purchasing | `FALSE` | TRUE \| FALSE. If TRUE, sends email receipts/confirmations when purchase orders are created or modified. |
| [**EMAIL_PO_TO_FINAL_APPROVER**](../rag-optimized/settings/EMAIL_PO_TO_FINAL_APPROVER.md) | Admin | `FALSE` | TRUE \| FALSE. If TRUE, sends PO creation notification to the final approver on the requisition. |
| [**EMAIL_PURGE_DAYS**](../rag-optimized/settings/EMAIL_PURGE_DAYS.md) | Admin | `30` | How often iPurchase will purge emails that have error-ed . Value is in days. |
| [**EMAIL_REGISTRATIONS**](../rag-optimized/settings/EMAIL_REGISTRATIONS.md) | Admin |  | Email addresses (comma-separated). Recipients of new user registration notifications. |
| [**EMAIL_REPLY_TO**](../rag-optimized/settings/EMAIL_REPLY_TO.md) | Admin |  | Email address. Reply-to address used in system-generated emails. If blank, uses FROM address. |
| [**EMAIL_REQ_BODY_MIN**](../rag-optimized/settings/EMAIL_REQ_BODY_MIN.md) | Admin | `FALSE` | When this is TRUE, only the supplier's number and name along with the cost of the requisition are embedded in the email. If the requisition is a change order, then the words "Change Order" will als... |
| [**EMAIL_SUPPLIER_ATTACH_FILES**](../rag-optimized/settings/EMAIL_SUPPLIER_ATTACH_FILES.md) | Admin | `FALSE` | This setting determines whether attachments are added to the email that will go to the supplier when the requisition is approved. |
| [**EMAIL_SUPPLIER_ATTACH_LINKS**](../rag-optimized/settings/EMAIL_SUPPLIER_ATTACH_LINKS.md) | Admin | `FALSE` | This setting determines whether attachments to a requisition are sent to the supplier as links in the email. |
| [**EMAIL_SUPPLIER_BLANKET_PO**](../rag-optimized/settings/EMAIL_SUPPLIER_BLANKET_PO.md) | Purchasing | `FALSE` | This setting determines whether or not an email is automatically sent to a supplier when the blanket order requisition is approved. |
| [**EMAIL_SUPPLIER_CONFIRMATION_LINK**](../rag-optimized/settings/EMAIL_SUPPLIER_CONFIRMATION_LINK.md) | Purchasing | `FALSE` | Determines if confirmation link is included in the PO email that is automatically sent to the supplier. It will also determine if the 'Include Confirmation Link' is displayed as an option on the ma... |
| [**EMAIL_SUPPLIER_CONFIRMATION_REMINDER_TEXT**](../rag-optimized/settings/EMAIL_SUPPLIER_CONFIRMATION_REMINDER_TEXT.md) | Purchasing |  | Custom text included in supplier confirmation reminder emails. |
| [**EMAIL_SUPPLIER_CONFIRMATION_TEXT**](../rag-optimized/settings/EMAIL_SUPPLIER_CONFIRMATION_TEXT.md) | Purchasing |  | This is the text that is to be inserted above the link which is included in the supplier email PO program. The default is "Please click the link to confirm acceptance of the Purchase Order". |
| [**EMAIL_SUPPLIER_PO**](../rag-optimized/settings/EMAIL_SUPPLIER_PO.md) | Purchasing | `TRUE` | This setting determines whether or not an email is automatically sent to a supplier when the requisition is approved. |
| [**EMAIL_SUPPLIER_PO_CC**](../rag-optimized/settings/EMAIL_SUPPLIER_PO_CC.md) | Power Users | `$xxreq_buyer,$xxreq_obo,$xxreq_userid` | This is a list of email address(s) of whom to carbon copy the supplier email to when the PO is created.  A value of "BUYER" will copy the associated buyer which is set on the requisition. If a user... |
| [**EMAIL_SUPPLIER_PO_FROM**](../rag-optimized/settings/EMAIL_SUPPLIER_PO_FROM.md) | Power Users | `$xxreq_buyer` | This is the email address to be used as the "From" field on the email. This can be a static email address or one of $xxreq_buyer, $xxreq_User ID, $xxreq_obo. If this field is left blank then the se... |
| [**EMAIL_SUPPLIER_PO_SUBJECT**](../rag-optimized/settings/EMAIL_SUPPLIER_PO_SUBJECT.md) | Purchasing | `New Purchase Order  - $NBR` | This text will be used as the subject of the email going to the supplier. If you'd like the PO number(s) to appear in the subject, add the text "$NBR" without the quotes in the position that you wa... |
| [**EMAIL_SUPPLIER_PO_SUBJECT_PUNCHOUT**](../rag-optimized/settings/EMAIL_SUPPLIER_PO_SUBJECT_PUNCHOUT.md) | Purchasing | `Punchout Purchase Order - $NBR` | This text will be used as the subject of the email going to the supplier. If you'd like the PO number(s) to appear in the subject, add the text "$NBR" without the quotes in the position that you wa... |
| [**EMAIL_SUPPLIER_PO_SUBJECT_REVISION**](../rag-optimized/settings/EMAIL_SUPPLIER_PO_SUBJECT_REVISION.md) | Purchasing | `Purchase Order Revision - $NBR` | This text will be used as the subject of the email going to the supplier. If you'd like the PO number(s) to appear in the subject, add the text "$NBR" without the quotes in the position that you wa... |
| [**INTERNAL_URL**](../rag-optimized/settings/INTERNAL_URL.md) | Admin |  | Internal network URL for application. Used when APPLICATION_URL/BASE_URL are external-facing. |
| [**LOGIN_HIDE_EMAIL_HELPDESK**](../rag-optimized/settings/LOGIN_HIDE_EMAIL_HELPDESK.md) | Admin |  | Hide the Email Helpdesk link on the login screen |
| [**NEW_PO_EMAIL_RECEIPTS**](../rag-optimized/settings/NEW_PO_EMAIL_RECEIPTS.md) | Purchasing | `no,no` | This setting determines if delivery receipts and read receipts are requested from the recipient's mail server when the email which includes the new PO attached is sent. To turn off this functionali... |
| [**NO_CHANGE_EMAIL**](../rag-optimized/settings/NO_CHANGE_EMAIL.md) | Power Users | `FALSE` | If an approver changes a requisition and this is set to true, then the originator will not be notified. |
| [**NO_EMAILS**](../rag-optimized/settings/NO_EMAILS.md) | Admin | `FALSE` | A value of True will turn off email functionality. A value of False will turn on email functionality. |
| [**NO_EMAIL_REQ_BODY**](../rag-optimized/settings/NO_EMAIL_REQ_BODY.md) | Power Users | `FALSE` | Do not include the requisition print in emails. Only includes the text. |
| [**NO_PO_EMAIL**](../rag-optimized/settings/NO_PO_EMAIL.md) | ISS |  | Technical - Do Not Modify without consulting ISS |
| [**PO_DO_NOT_EMAIL**](../rag-optimized/settings/PO_DO_NOT_EMAIL.md) | Power Users | `FALSE` | If set to true the PO will not be emailed. |
| [**RECEIPT_EMAIL_MESSAGE**](../rag-optimized/settings/RECEIPT_EMAIL_MESSAGE.md) | Purchasing |  | Custom message text for receipt notification emails. |
| [**RECEIPT_EMAIL_REQ_TYPES**](../rag-optimized/settings/RECEIPT_EMAIL_REQ_TYPES.md) | Purchasing |  | Comma-separated req types. Types that trigger receipt emails. |
| [**RECEIPT_EMAIL_SUBJECT**](../rag-optimized/settings/RECEIPT_EMAIL_SUBJECT.md) | Purchasing | `Receipt Notification` | Email subject for receipt notifications. |
| [**RECEIPT_EMAIL_TO**](../rag-optimized/settings/RECEIPT_EMAIL_TO.md) | Purchasing |  | Email addresses for receipt notifications. |
| [**RECEIPT_EMAIL_USERS**](../rag-optimized/settings/RECEIPT_EMAIL_USERS.md) | Purchasing |  | Can-Do list. Users who receive receipt notification emails. |
| [**REMOVE_NEEDED_BY_FROM_EMAILS**](../rag-optimized/settings/REMOVE_NEEDED_BY_FROM_EMAILS.md) | Power Users | `FALSE` | Show 'Needed By 99/99/9999' in the approval email subject. |

## GL Accounts & Finance

| Setting | Owner | Default | Description |
|---------|-------|---------|-------------|
| [**ACCOUNT_RANGE_CANDO**](../rag-optimized/settings/ACCOUNT_RANGE_CANDO.md) | Finance | `*` | This is a comma separated list of accounts that can be used with iPurchase. The field uses the Progress �Can-Do� function. See Progress help if needed. A sample value can be 5521,!5622,56*,7*,!* Th... |
| [**ACCOUNT_REQUIRE_PROJECT**](../rag-optimized/settings/ACCOUNT_REQUIRE_PROJECT.md) | Finance |  | A list of accounts which will always require a Project Code |
| [**ACCOUNT_SHOW_CUSTOMNOTE**](../rag-optimized/settings/ACCOUNT_SHOW_CUSTOMNOTE.md) | Finance | `FALSE` | Show the value CustomNote Field on the GL record - only for EE |
| [**ACCOUNT_SORT_BY_NAME**](../rag-optimized/settings/ACCOUNT_SORT_BY_NAME.md) | Power Users | `FALSE` | A value of true will show the accounts sorted by name. Any other value will sort by number. |
| [**ARCHIVE_KEEP_YEARS**](../rag-optimized/settings/ARCHIVE_KEEP_YEARS.md) | Finance | `3` | The number of years to keep requisitions. Note: Pending Requisitions can't be archived. |
| [**BUDGET_ADMINISTRATOR**](../rag-optimized/settings/BUDGET_ADMINISTRATOR.md) | Admin |  | Comma Separated list of User ID's or Group ID's who are allowed to maintain budgets in iPurchase. Asterisk indicates everyone, a blank indicates no one. |
| [**BUDGET_ASST_EDIT**](../rag-optimized/settings/BUDGET_ASST_EDIT.md) | Admin | `*` | Allow the budget assistant managers specified in a budget the ability to modify the sub budgets. Assistant Managers can't modify the budget header. |
| [**BUDGET_HIDE_OTHER**](../rag-optimized/settings/BUDGET_HIDE_OTHER.md) | Admin | `TRUE` | Do not show nor use the Other column on Budgets. |
| [**BUDGET_MGR_EDIT**](../rag-optimized/settings/BUDGET_MGR_EDIT.md) | Admin | `*` | Allow the budget manager specified in a budget the ability to modify the entire budget |
| [**BUDGET_MONTHLY_REPORT**](../rag-optimized/settings/BUDGET_MONTHLY_REPORT.md) | Finance |  | Can-Do list. Users/groups allowed to access budget monthly reports. Automatically disabled in archive systems. |
| [**BUDGET_THRESHOLD_AMT**](../rag-optimized/settings/BUDGET_THRESHOLD_AMT.md) | Power Users |  | Threshold amount added to defined budget amount before error that you can not create another item using that budget. |
| [**BUDGET_THRESHOLD_PCT**](../rag-optimized/settings/BUDGET_THRESHOLD_PCT.md) | Power Users |  | Threshold pct added to defined budget amount before error that you can not create another item using that budget. |
| [**CODE_LIST_TAX_CLASS**](../rag-optimized/settings/CODE_LIST_TAX_CLASS.md) | Finance | `comma-separated list of tax classes. List: is not needed on this setting` |  |
| [**CODE_LIST_TAX_ENVIRONMENT**](../rag-optimized/settings/CODE_LIST_TAX_ENVIRONMENT.md) | Finance |  | LIST format. Dropdown values for tax environment field. Format: LIST:code:description,code:description |
| [**CODE_LIST_TAX_USAGE**](../rag-optimized/settings/CODE_LIST_TAX_USAGE.md) | Finance | `comma-separated list of tax usage. List: is not needed on this setting` |  |
| [**COST_CENTER_REQUIRE_PROJECT**](../rag-optimized/settings/COST_CENTER_REQUIRE_PROJECT.md) | Finance |  | Can-Do list. Cost centers that require a project code. Validation error if project is blank for these cost centers. |
| [**DEFAULT_SUB_ACCOUNT**](../rag-optimized/settings/DEFAULT_SUB_ACCOUNT.md) | Finance |  | The default sub account is used when creating requisition from catalogs and punchouts. The order in which iPurchase determines the sub account for a requisition created from a Punchout or Catalog i... |
| [**DEFAULT_TAX_CLASS**](../rag-optimized/settings/DEFAULT_TAX_CLASS.md) |  |  | You can use this to set the Tax Class field in QAD. If set this will default for all Purchase Orders |
| [**DEFAULT_TAX_ENVIRONMENT**](../rag-optimized/settings/DEFAULT_TAX_ENVIRONMENT.md) |  |  | You can use this to set the Tax Environment field in QAD. If set this will default for all Purchase Orders |
| [**DEFAULT_TAX_USAGE**](../rag-optimized/settings/DEFAULT_TAX_USAGE.md) |  |  | You can use this to set the Tax Usage field in QAD. If set this will default for all Purchase Orders. |
| [**DEPARTMENTS_USE_ORIG**](../rag-optimized/settings/DEPARTMENTS_USE_ORIG.md) | Admin | `FALSE` | This setting allows the administrator to set the drop down list of departments at the line entry. If set to TRUE the list will be based on the originator.  If set to FALSE, the department is set ba... |
| [**DEPARTMENT_SORT_BY_NAME**](../rag-optimized/settings/DEPARTMENT_SORT_BY_NAME.md) | Power Users |  | A value of true will show the departments sorted by name. Any other value will sort by number. |
| [**ESTIMATED_TAX_PERCENT**](../rag-optimized/settings/ESTIMATED_TAX_PERCENT.md) | Finance |  | If the taxable amounts need to figure into the approval rules, then use this setting to enter an estimate tax percentage that will be added on to all taxable requisition lines.  If 10% enter as "10" |
| [**ESTIMATED_TAX_PERCENT_[ship to code]**](<../rag-optimized/settings/ESTIMATED_TAX_PERCENT_[ship to code].md>) | Finance |  | If the taxable amounts need to figure into the approval rules, then use this setting to enter an estimate tax percentage that will be added on to all taxable requisition lines based on specific shi... |
| [**GL_OVERRIDE**](../rag-optimized/settings/GL_OVERRIDE.md) | Finance | `FALSE` | If you set this setting to true, then all items entered in the line entry screen will have the account, sub-account, and cost center set to the values which QAD would dictate based on the vendor an... |
| [**OOF_LIMIT_BY_DEPT**](../rag-optimized/settings/OOF_LIMIT_BY_DEPT.md) | Admin | `FALSE` | A setting of True will only allow a user to delegate to another user who shares a same department. A setting of FIRST A setting will only allow a user to delegate to another user who is in the orig... |
| [**PROJECT_RANGE_CANDO**](../rag-optimized/settings/PROJECT_RANGE_CANDO.md) | Finance | `*` | Can-Do list. Valid project codes. Default * allows all. |
| [**REMOVE_ORIG**](../rag-optimized/settings/REMOVE_ORIG.md) | Finance | `TRUE` | This setting does not allow the originator to be an approver for their own requisitions if set to true. |
| [**RT_REQUIRE_PROJECT**](../rag-optimized/settings/RT_REQUIRE_PROJECT.md) | Finance | `Capital` | List of requisition typles that require a project code. |
| [**RT_REQ_TAXABLE**](../rag-optimized/settings/RT_REQ_TAXABLE.md) | Finance |  | Comma-separated req types. Types where tax is calculated. If blank, all types are taxable. |
| [**SUB_ACCOUNTS_USE_ORIG**](../rag-optimized/settings/SUB_ACCOUNTS_USE_ORIG.md) | Finance | `FALSE` | TRUE \| FALSE. If TRUE, uses originator's allowed sub-accounts instead of OBO's. |
| [**SUB_ACCOUNT_RANGE_CANDO**](../rag-optimized/settings/SUB_ACCOUNT_RANGE_CANDO.md) | Finance | `*` | This is the same as ACCOUNT_RANGE_CANDO except this applies to sub accounts. USE RT_.... |
| [**SUB_ACCOUNT_SORT_BY_NAME**](../rag-optimized/settings/SUB_ACCOUNT_SORT_BY_NAME.md) | Power Users |  | True or False A value of TRUE will show the sub-accounts sorted by name. Any other value will sort by number. |
| [**TAX_CLASS_FIELD**](../rag-optimized/settings/TAX_CLASS_FIELD.md) | Finance |  | [LEGACY/OBSOLETE] Field name for tax class in data upgrades. Commented out in code. |
| [**TAX_CUSTOMER**](../rag-optimized/settings/TAX_CUSTOMER.md) | Finance |  | Default tax customer code for tax calculations. |
| [**TAX_USAGE_FIELD**](../rag-optimized/settings/TAX_USAGE_FIELD.md) | Finance |  | [LEGACY/OBSOLETE] Field name for tax usage in data upgrades. Commented out in code. |
| [**USE_BUDGETS**](../rag-optimized/settings/USE_BUDGETS.md) | Finance | `FALSE` | [LEGACY/OBSOLETE] TRUE \| FALSE. Enable budget functionality. Commented out in code - use BUDGET_USE_IAPPROVE instead. |
| [**USE_BUDGETS_AS_FORECAST**](../rag-optimized/settings/USE_BUDGETS_AS_FORECAST.md) | Admin | `FALSE` | Allow full budget functionality but allow reqs to be created and processed even if overbudget. |

## Inventory & MRP

| Setting | Owner | Default | Description |
|---------|-------|---------|-------------|
| [**CODE_LIST_MRP_BUYERS**](../rag-optimized/settings/CODE_LIST_MRP_BUYERS.md) | Purchasing |  | Only use this setting if you want to have a different buyer list show up in the MRP Action Center. This list is in the format 'list:code:desc,code:desc' or a generalized code field name like 'ptp_b... |
| [**INV_TRANS_REASON_CODES**](../rag-optimized/settings/INV_TRANS_REASON_CODES.md) | Purchasing |  | Comma-separated reason codes. Valid transaction reason codes for inventory movements. |
| [**INV_TRANS_TYPES**](../rag-optimized/settings/INV_TRANS_TYPES.md) | Purchasing |  | Comma-separated transaction types. Valid inventory transaction types. |
| [**MRP_SORT**](../rag-optimized/settings/MRP_SORT.md) | Purchasing |  | Sort field for MRP (Material Requirements Planning) item listings. |
| [**RT_MRP**](../rag-optimized/settings/RT_MRP.md) | Purchasing |  | Comma-separated req types. Types that trigger MRP (Material Requirements Planning). |
| [**TRANSFER_STATUS**](../rag-optimized/settings/TRANSFER_STATUS.md) | Purchasing |  | Status value for inventory transfer transactions. |

## Portal Integration

| Setting | Owner | Default | Description |
|---------|-------|---------|-------------|
| [**PORTAL_CONFIRM_RECEIPT_URL**](../rag-optimized/settings/PORTAL_CONFIRM_RECEIPT_URL.md) | ISS |  | URL endpoint for portal receipt confirmation integration. Used for external portal systems. |

## Purchase Orders

| Setting | Owner | Default | Description |
|---------|-------|---------|-------------|
| [**AUTO_COMMENTS_BUYER**](../rag-optimized/settings/AUTO_COMMENTS_BUYER.md) | Power Users |  | Use this setting to automatically attach comments to every Purchase Order when a particular buyer or bill to or ship to or site or line site is used. This is a pointer to the code_mstr field name (... |
| [**AUTO_COMMENTS_CO**](../rag-optimized/settings/AUTO_COMMENTS_CO.md) | Power Users |  | Use this setting to automatically attach comments to every Purchase Order REVISION - CHANGE ORDER. This is a pointer to the code_mstr field name (code_fldname) value to be used. Example: List:Buyer... |
| [**AUTO_COMMENTS_LINE_SITE**](../rag-optimized/settings/AUTO_COMMENTS_LINE_SITE.md) | Power Users |  | Use this setting to automatically attach comments to every Purchase Order when a particular buyer or bill to or ship to or site or line site is used. This is a pointer to the code_mstr field name (... |
| [**AUTO_COMMENTS_OTHER**](../rag-optimized/settings/AUTO_COMMENTS_OTHER.md) | Power Users |  | Use this setting to automatically attach comments to every Purchase Order when a particular buyer or bill to or ship to or site or line site is used. This is a pointer to the code_mstr field name (... |
| [**BATCH_CREATE_PO_GROUPS**](../rag-optimized/settings/BATCH_CREATE_PO_GROUPS.md) | Admin | `buyers` | Comma Separated list of User ID's or Group ID's that can convert an approved requisition into a PO (only when PO is not created automatically upon final approval) Thios setting also controls if a u... |
| [**BLANKET_SEND_PO**](../rag-optimized/settings/BLANKET_SEND_PO.md) | Purchasing | `FALSE` | If set to true the PO will be emailed. |
| [**BUYER_MOD**](../rag-optimized/settings/BUYER_MOD.md) | Purchasing | `FALSE` | TRUE \| FALSE. If TRUE, allows the buyer field to be modified during requisition copy and PO creation. If FALSE, buyer field is locked. |
| [**CATALOG_PO_DIFFERENCE**](../rag-optimized/settings/CATALOG_PO_DIFFERENCE.md) | Power Users | `Lowest` | Possible Values: Blank, Punchout, Catalog, Lowest.  During a punchout, if an item ordered via a punchout site also exists in the catalog, do you want to use the Catalog's price rather than the pric... |
| [**CLOSE_PO**](../rag-optimized/settings/CLOSE_PO.md) | Admin | `buyers` | Comma Separated list of User ID's or Group ID's that will have the ability to close PO  or  PO line on Purchase order.  Either Line or whole PO can be closed. Close or canceled depends on Receipts.... |
| [**CO_UPDATE_ORDER_DATE**](../rag-optimized/settings/CO_UPDATE_ORDER_DATE.md) | Purchasing | `FALSE` | Update the order date on the change order PO to today's date |
| [**DEFAULT_BUYER**](../rag-optimized/settings/DEFAULT_BUYER.md) | Purchasing |  | This is the userid of the default buyer to be used on all new requisitions. This can be overridden by DEFAULT_BUYER_[SITE], RT_[REQ_TYPE]_DEFAULT_BUYER, RT_[REQ_TYPE]_[SITE]_DEFAULT_BUYER, and vd_b... |
| [**DEFAULT_BUYER_[SITE]**](<../rag-optimized/settings/DEFAULT_BUYER_[SITE].md>) | Purchasing |  | This is the userid of the default buyer for the specified site, used on all new requisitions. See DEFAULT_BUYER |
| [**DEFAULT_SHIPTO**](../rag-optimized/settings/DEFAULT_SHIPTO.md) | Power Users |  | In this setting the administrator can set the default value for "Ship To" field. |
| [**DEFAULT_SHIPVIA**](../rag-optimized/settings/DEFAULT_SHIPVIA.md) | Purchasing |  | In this setting the administrator can set the default value for "Ship Via" field. |
| [**DEFAULT_SITE**](../rag-optimized/settings/DEFAULT_SITE.md) | Admin |  | In this setting the administrator can set the default value for the "Site" field. Must be a valid site. |
| [**FIRST_PO_NUMBER**](../rag-optimized/settings/FIRST_PO_NUMBER.md) | Purchasing | `1` | Numeric. Starting purchase order number for sequential PO numbering. |
| [**MC_BEFORE_NOTES**](../rag-optimized/settings/MC_BEFORE_NOTES.md) | Purchasing | `FALSE` | TRUE \| FALSE. If TRUE, places master comments before line notes on PO. |
| [**NO_PO_PP**](../rag-optimized/settings/NO_PO_PP.md) | ISS |  | Technical - Do Not Modify without consulting ISS |
| [**PO_BLANKET_PRINT_PROGRAM**](../rag-optimized/settings/PO_BLANKET_PRINT_PROGRAM.md) | Admin | `us/po/poblrp03.p` | QAD program name which prints blankets, should not be modified. |
| [**PO_BREAK_BY**](../rag-optimized/settings/PO_BREAK_BY.md) | Power Users | `xxreqd_vendor` | Comma separated list of fields on a requisition that will be used to split the requisition into multiple PO's. Or Comma separated list of fields on a requisition that will be used to consolidate PO... |
| [**PO_CONFIRMATION_RESPONSE**](../rag-optimized/settings/PO_CONFIRMATION_RESPONSE.md) | Power Users |  | Message to display to the supplier when the supplier confirms receipt of the PO by clicking on the Confirm Receipt link in their email message. |
| [**PO_DO_NOT_PRINT**](../rag-optimized/settings/PO_DO_NOT_PRINT.md) | Power Users | `FALSE` | Does not print the PO when requisition is approved. |
| [**PO_LOGO**](../rag-optimized/settings/PO_LOGO.md) | Admin |  | The value of this setting is a path to the physical file name on the app server. Ex. " or apps or iPurchase or logo or frank.jpg". If the logo is in the wdm or agents folder then you only need to p... |
| [**PO_LOGO_[po_bill]**](<../rag-optimized/settings/PO_LOGO_[po_bill].md>) | Admin |  | This setting allows the administrator to enter a PO Logo based on the PO Bill To Field. The value of this setting is a path to the physical file name on the app server. Ex. " or apps or iPurchase o... |
| [**PO_NBR_USE_QAD**](../rag-optimized/settings/PO_NBR_USE_QAD.md) | Purchasing | `FALSE` | TRUE \| FALSE. If TRUE, uses QAD system for PO number generation. |
| [**PO_PREFIX**](../rag-optimized/settings/PO_PREFIX.md) | Purchasing |  | Prefix added to purchase order numbers (e.g., PO- results in PO-12345). |
| [**PO_PREFIX_FIELD**](../rag-optimized/settings/PO_PREFIX_FIELD.md) | entities |  | Can be either 'Entity' or any fields on the requisition header table. This will allow you to create different prefix or number scheme for different sites |
| [**PO_PRINTER**](../rag-optimized/settings/PO_PRINTER.md) | Admin |  | Printer name defined in QAD. If you're using Optio, Jetforms, Pics, etc, to print graphical purchase orders, enter the name of the printer here, otherwise leave blank. |
| [**PO_PRINTER_BATCH_NAME**](../rag-optimized/settings/PO_PRINTER_BATCH_NAME.md) | Admin | `QADSVC` | This setting allows the administrator to set the Queue that the report will be processed on.  ex: "POPrint" QAD EE 2012 and above allows the ability to print fancy purchase orders. Requirements: Na... |
| [**PO_PRINTER_OUTPUT_DIRECTORY**](../rag-optimized/settings/PO_PRINTER_OUTPUT_DIRECTORY.md) | Admin |  | Is a directory on the iPurchase application server where the QAD Reporting Framework will save the file. If you are using Optio, Jetforms, Pics, etc, to print graphical purchase orders, enter the n... |
| [**PO_PRINTER_OUTPUT_DIRECTORY_BLANKET**](../rag-optimized/settings/PO_PRINTER_OUTPUT_DIRECTORY_BLANKET.md) | Purchasing |  | Directory path. Output folder for blanket purchase order print files. |
| [**PO_PRINTER_REPORT_CODE**](../rag-optimized/settings/PO_PRINTER_REPORT_CODE.md) | Admin | `PurchaseOrderPrint ` | This setting holds the report code for the print version you are using. ex: Custom_PurchaseOrderPrint. QAD EE 2012 and above allows the ability to print fancy purchase orders. Requirements: Names Q... |
| [**PO_PRINTER_REPORT_CODE_BLANKET**](../rag-optimized/settings/PO_PRINTER_REPORT_CODE_BLANKET.md) | Purchasing |  | Report code used for printing blanket purchase orders. |
| [**PO_PRINTER_SERVER_XML**](../rag-optimized/settings/PO_PRINTER_SERVER_XML.md) | Admin |  | This setting points iPurchase to PO printer server configuration file. ex:  or apps or test or qdt or envs or test or configs or server.xml QAD EE 2012 and above allows the ability to print fancy p... |
| [**PO_PRINT_ARCHIVE_DIR**](../rag-optimized/settings/PO_PRINT_ARCHIVE_DIR.md) | Admin |  | Directory on application server. Enter the path to a directory on the application server where all purchase orders will be saved to when printing a revision through iPurchase for the first time. Th... |
| [**PO_PRINT_ARCHIVE_IN_DB**](../rag-optimized/settings/PO_PRINT_ARCHIVE_IN_DB.md) | Admin | `TRUE` | Store Purchase Order PDF files in database. A setting of true will display a clock icon next to Purchase Order numbers in iPurchase. Clicking the clock icon will display a list of all original prin... |
| [**PO_PRINT_DOMAIN_IN_FN**](../rag-optimized/settings/PO_PRINT_DOMAIN_IN_FN.md) | ISS |  | Technical - Do Not Modify without consulting ISS |
| [**PO_PRINT_OFFLINE**](../rag-optimized/settings/PO_PRINT_OFFLINE.md) | Admin | `FALSE` | This setting will control when the New PO Created email and original PO Print occur. A value of FALSE, the default, will print the PO and send the email as soon as the Purchase Order is created. Mo... |
| [**PO_PRINT_PDF_FORMAT**](../rag-optimized/settings/PO_PRINT_PDF_FORMAT.md) | Power Users | `PLAIN` | Prints the POs using the built in iPurchase look. Valid choices are GRAPHICAL and PLAIN. A value of PLAIN will simply take the text based QAD output and convert it to PDF. |
| [**PO_PRINT_PROGRAM**](../rag-optimized/settings/PO_PRINT_PROGRAM.md) | Admin | `us/po/poporp03.p` | Progress program If you have a custom purchase order print program then enter the Progress program name here. |
| [**PO_PRINT_SORT**](../rag-optimized/settings/PO_PRINT_SORT.md) | Purchasing | `LINE` | This setting determines the value which will be used to sort the Purchase Order on the PO Print screen. |
| [**PO_SIGNATURE**](../rag-optimized/settings/PO_SIGNATURE.md) | Admin |  | The value of this setting is a path to the physical file name on the app server. Ex " or apps or iPurchase or signatures or frank.jpg". If the signature is in the wdm or agents folder then you only... |
| [**PO_SIGNATURE_BUYER_[buyercode]**](<../rag-optimized/settings/PO_SIGNATURE_BUYER_[buyercode].md>) | Admin |  | This setting allows the administrator to enter a buyers signature based on the buyer's code. The value of this setting is a path to the physical file name on the app server. Ex " or apps or iPurcha... |
| [**PO_SIGNATURE_BUYER_[domain code]**](<../rag-optimized/settings/PO_SIGNATURE_BUYER_[domain code].md>) | Admin |  | This setting allows the administrator to enter a buyers signature based on the domain in the buyer user record The value of this setting is a path to the physical file name on the app server. Ex " ... |
| [**PO_SIGNATURE_BUYER_[domain code]_[site code]**](<../rag-optimized/settings/PO_SIGNATURE_BUYER_[domain code]_[site code].md>) | Admin |  | This setting allows the administrator to enter a buyers signature based on the domain and the site of the buyer user record The value of this setting is a path to the physical file name on the app ... |
| [**PO_SIGNATURE_BUYER_[site_code]**](<../rag-optimized/settings/PO_SIGNATURE_BUYER_[site_code].md>) | Admin |  | This setting allows the administrator to enter a buyers signature based on the site in the buyer user record The value of this setting is a path to the physical file name on the app server. Ex " or... |
| [**PO_SIGNATURE_ON_REPRINT**](../rag-optimized/settings/PO_SIGNATURE_ON_REPRINT.md) | Power Users | `TRUE` | This setting allows the administrator to print a signature on a reprint of a Purchase Order. |
| [**PO_SIGNATURE_[SITE]**](<../rag-optimized/settings/PO_SIGNATURE_[SITE].md>) | Admin |  | This setting allows for multiple PO signatures based on domain and site. The value of this setting is a path to the physical file name on the app server. Ex " or apps or iPurchase or signatures or ... |
| [**PO_UPDATE_GROUPS**](../rag-optimized/settings/PO_UPDATE_GROUPS.md) | Admin | `$xxreq_buyer` | Comma separated list of User ID's or Group ID's that would be allowed to use the Copy or Update PO functionality (Change Order).  For buyer, set to "$xxreq_buyer".  Asterisk indicates everyone, a b... |
| [**PO_UPDATE_REQ_TYPES**](../rag-optimized/settings/PO_UPDATE_REQ_TYPES.md) | Purchasing | `*` | You can control the list of requisition types that will allow a change order, or * for all requisition types. |
| [**PO_UPDATE_TOLERANCE_AMOUNT**](../rag-optimized/settings/PO_UPDATE_TOLERANCE_AMOUNT.md) | Admin | `100` | This is the amount that a requisition can be increased by without requiring re-routing the requisition for approval. This is only for those requisitions that are UPDATING a purchase order. |
| [**PO_UPDATE_TOLERANCE_PCT**](../rag-optimized/settings/PO_UPDATE_TOLERANCE_PCT.md) | Admin | `10` | This is the percentage that a requisition can be increased by without requiring re-routing the requisition for approval. This is only for those requisitions that are UPDATING a purchase order. |
| [**QX_PO_NAME**](../rag-optimized/settings/QX_PO_NAME.md) |  | `QADERP` | Name of the qxtend instance for Purchase Orders in this environment |
| [**QX_PO_VERSION**](../rag-optimized/settings/QX_PO_VERSION.md) |  | `eB2_3` | Version of the qxtend PO method for this environment |
| [**REOPEN_PO**](../rag-optimized/settings/REOPEN_PO.md) | Purchasing | `buyers` | Comma separated list of User ID's or Group ID's that are allowed to re-open a closed or cancelled PO via a change order. Asterisk indicates everyone, a blank indicates no one. |
| [**RT_PO_REQUIRED**](../rag-optimized/settings/RT_PO_REQUIRED.md) | Power Users |  | This setting is a list of requisition types that would set the PO Required field to True or Yes.  For example if you do not require a PO for credit card purchases and CREDIT_CARD is a Requisition T... |
| [**SUPPLIER_PO_ATTACHMENTS**](../rag-optimized/settings/SUPPLIER_PO_ATTACHMENTS.md) | Admin |  | Comma-Separated List of paths and files. This is a list of files which is to be emailed to the supplier as attachments to the Purchase Order. |
| [**SUPPLIER_PO_MERGE_ATTACHMENTS**](../rag-optimized/settings/SUPPLIER_PO_MERGE_ATTACHMENTS.md) | Purchasing |  | This setting is where the filename, with the full path to the pdf file or a space delimited list of pdf files that are to be merged in to the PO PDF file which is printed. If you're on windows then... |

## QAD Integration

| Setting | Owner | Default | Description |
|---------|-------|---------|-------------|
| [**AS400OUTBOUNDFOLDER**](../rag-optimized/settings/AS400OUTBOUNDFOLDER.md) | Admin |  | Directory path on application server. Folder where AS400 catalog XML files are written. Files are named [req_nbr].xml. Used in catalog integration. |
| [**QAD_COMMENT_TYPE**](../rag-optimized/settings/QAD_COMMENT_TYPE.md) | Admin | `IP` | This is the comment type to be used when creating PO Header and PO Line comments.  Add IP To Generalized Codes if there are any generalized codes for field name cd_type |
| [**QAD_INTERFACE_PASSWORD**](../rag-optimized/settings/QAD_INTERFACE_PASSWORD.md) | ISS |  | ⚠️ SENSITIVE. Password for QAD system integration user. |
| [**QAD_REQUESTED_BY**](../rag-optimized/settings/QAD_REQUESTED_BY.md) | Power Users |  | This setting will use OBO as the Requested By. If you set QAD_REQUESTED_BY to "ORIGINATOR" then the req originator (xxreq_userid) will be used. |
| [**SKIP_QAD_ACTIVE_CHECK**](../rag-optimized/settings/SKIP_QAD_ACTIVE_CHECK.md) | Admin | `TRUE` | True or False Do not check the QAD user's active flag. Normally a user (if the QAD User ID matches the iPurchase User ID) needs to be active in QAD in order to login to iPurchase. This does not alw... |
| [**SKIP_QAD_DOMAIN_CHECK**](../rag-optimized/settings/SKIP_QAD_DOMAIN_CHECK.md) | ISS | `FALSE` | TRUE \| FALSE. Skip domain validation in QAD integration. |

## Qxtend Integration

| Setting | Owner | Default | Description |
|---------|-------|---------|-------------|
| [**QX_BROKER**](../rag-optimized/settings/QX_BROKER.md) | ISS |  | Qxtend broker server address for Qxtend integration. |
| [**QX_CODEPAGE**](../rag-optimized/settings/QX_CODEPAGE.md) | ISS |  | Character encoding for Qxtend communication. |
| [**QX_URL**](../rag-optimized/settings/QX_URL.md) | ISS |  | Qxtend service URL. |
| [**QX_VERSION**](../rag-optimized/settings/QX_VERSION.md) | ISS |  | Qxtend version number. |

## RFQ Management

| Setting | Owner | Default | Description |
|---------|-------|---------|-------------|
| [**IRFQ**](../rag-optimized/settings/IRFQ.md) | Purchasing | `FALSE` | TRUE \| FALSE. Enable iRFQ (RFQ management) module. |
| [**RFQ_BODY**](../rag-optimized/settings/RFQ_BODY.md) | Purchasing |  | Email body template for RFQ emails. |
| [**RFQ_SUBJECT**](../rag-optimized/settings/RFQ_SUBJECT.md) | Purchasing | `Request for Quote` | Email subject for RFQ emails. |

## Receiving

| Setting | Owner | Default | Description |
|---------|-------|---------|-------------|
| [**ALLOW_RECEIVING**](../rag-optimized/settings/ALLOW_RECEIVING.md) | Purchasing |  | Can-Do list. Users/groups allowed to receive against purchase orders. Can include $xxreq_buyer to allow the buyer on the PO to receive. |
| [**AUTO_RECEIVE**](../rag-optimized/settings/AUTO_RECEIVE.md) | Purchasing | `FALSE` | TRUE \| FALSE. If TRUE, automatically creates receipt transactions when purchase order is created. Timing controlled by AUTO_RECEIVE_TIME setting. |
| [**AUTO_RECEIVE_TIME**](../rag-optimized/settings/AUTO_RECEIVE_TIME.md) | Purchasing |  | Time value. Timestamp used when AUTO_RECEIVE creates automatic receipt records. Must be configured correctly when AUTO_RECEIVE is enabled. |
| [**BUDGET_HIDE_RECEIPTS**](../rag-optimized/settings/BUDGET_HIDE_RECEIPTS.md) | Admin | `TRUE` | Do not show nor use the Receipts column on Budgets. |
| [**LAST_RECEIPT_ID**](../rag-optimized/settings/LAST_RECEIPT_ID.md) | ISS |  | iPurchase process receipts in QAD for budgets. It periodically looks for receipts in batch. When implementing you can set the tr_id to start from so that it does not spend time looking at old recei... |

## Reporting & Inquiry

| Setting | Owner | Default | Description |
|---------|-------|---------|-------------|
| [**EXCEL_EXPORT_FIELDS**](../rag-optimized/settings/EXCEL_EXPORT_FIELDS.md) | IT | `xxreq_domain,xxreq_vendor,xxreq_entry_date,xxreq_nbr,xxreq_userid,xxreq_buyer,xxreq_type,xxreq_site,xxreqd_item,xxreqd_desc,xxreqd_qty,xxreqd_cost,xxreqd_po_nbr,xxreqd_po_line` | This is the list of fields that will be exported from the requisition workbench. Any requisition header field or line field can be used. You can also use PO and PO line fields. Some common PO/PO Li... |
| [**EXCEL_EXPORT_ONE_TAB**](../rag-optimized/settings/EXCEL_EXPORT_ONE_TAB.md) | Power Users | `TRUE` | Will export a consolidated view of the requisition when the Excel link is clicked in Requisition Inquiry. Default FALSE |
| [**INQUIRY_AFTER_REJECT**](../rag-optimized/settings/INQUIRY_AFTER_REJECT.md) | Power Users | `*` | Comma separated list of User ID's or Group ID's that are re-directed to the pending queue once they have rejected a requisition. Asterisk indicates everyone, a blank indicates no one. This setting ... |
| [**INQUIRY_LAST_REV_DEFAULT**](../rag-optimized/settings/INQUIRY_LAST_REV_DEFAULT.md) |  | `TRUE` | Setting this to true will check the Last Revision Only in the requisition inquiry. This is useful when you only want to see the requisition for the last revision of a PO. As opposed to all the requ... |
| [**INQUIRY_NOTES_MATCHES**](../rag-optimized/settings/INQUIRY_NOTES_MATCHES.md) | Admin | `FALSE` | When searching requisitions by using the notes field, use 'matches' vs 'contains', matches can be much slower but more flexible. |
| [**INQUIRY_NO_NAME_SEARCH**](../rag-optimized/settings/INQUIRY_NO_NAME_SEARCH.md) | Power Users | `FALSE` | If this setting is set to true then when a user searches for a supplier they will not be allowed to search by name, only by supplier number. a value of false enables the user to search by both supp... |
| [**INQUIRY_REFRESH_SECONDS**](../rag-optimized/settings/INQUIRY_REFRESH_SECONDS.md) | Power Users | `120` | How often the system automatically refreshes the inquiry screen in seconds. |
| [**INQUIRY_SIMPLE_MODE**](../rag-optimized/settings/INQUIRY_SIMPLE_MODE.md) | Admin |  | Comma separated list of User ID's or Group ID's who only gets to see "Views" on inquiry screen and does not see all the filter fields. This can be used as requisition security. Asterisk indicates e... |

## Requisition Types

| Setting | Owner | Default | Description |
|---------|-------|---------|-------------|
| [**RT_MEMO_ONLY_LIST**](../rag-optimized/settings/RT_MEMO_ONLY_LIST.md) | Finance | `Expense,Capital` | Comma-separated list of requisition types. All line items created for the requisition types defined will be entered as Memo Items on the Purchase Order. |
| [**RT_USE_LOCATION**](../rag-optimized/settings/RT_USE_LOCATION.md) | Purchasing | `Inventory` | List of requisition types which will allow a Item Location to be entered during line item entry |

## Requisitions

| Setting | Owner | Default | Description |
|---------|-------|---------|-------------|
| [**ADD_REQ_NBR_TO_PO**](../rag-optimized/settings/ADD_REQ_NBR_TO_PO.md) | Purchasing | `FALSE` | When a PO is created do you want to add the requisition number and line to pod_req and pod_req_line fields. This should be set to False if using 2009SE or above; or if GRS is being used |
| [**ALLOW_NEGATIVE_LINE**](../rag-optimized/settings/ALLOW_NEGATIVE_LINE.md) | Purchasing |  | Can-Do list. Users/groups allowed to enter negative quantities on requisition line items. Normally rejected with error message. |
| [**ALLOW_NEW_REQUEST**](../rag-optimized/settings/ALLOW_NEW_REQUEST.md) | Purchasing |  | Can-Do list. Users/groups allowed to create new requisitions. Controls visibility of New Request button in UI. |
| [**ALLOW_SAVE_TEMPLATE**](../rag-optimized/settings/ALLOW_SAVE_TEMPLATE.md) | Purchasing |  | Can-Do list. Users/groups allowed to save requisition templates. |
| [**AUDIT_XXREQ_MSTR_EXCEPT**](../rag-optimized/settings/AUDIT_XXREQ_MSTR_EXCEPT.md) | ISS | `xxreq_cost,xxreq_word_idx,xxreq_word_idx2,xxreq_word_idx3,xxreq_master_comments,xxreq_submit_date,xxreq_submit_attempts,xxreq_submit_date,xxreq_approved,xxreq_app_by,xxreq_submitted` | Technical - Do Not Modify without consulting ISS |
| [**AUTO_REQ_TYPE_DISABLE**](../rag-optimized/settings/AUTO_REQ_TYPE_DISABLE.md) | Admin | `FALSE` | Disable the requisition type field when there is at least one line item on a requisition - DO NOT MODIFY |
| [**CODE_LIST_H_XXREQ_UCHAR1**](../rag-optimized/settings/CODE_LIST_H_XXREQ_UCHAR1.md) | Admin | `List:True:Yes,False:No` | List for User Field 1 |
| [**CODE_LIST_H_XXREQ_UCHAR2**](../rag-optimized/settings/CODE_LIST_H_XXREQ_UCHAR2.md) | Admin | `List:1:Maybe,2:Maybe Not` | List for User Field 2 |
| [**CODE_LIST_H_XXREQ_UCHAR3**](../rag-optimized/settings/CODE_LIST_H_XXREQ_UCHAR3.md) | Admin | `List:Apples:Apples,Bananas:Bananas,Oranges:Oranges` | List for User Field 3 |
| [**CODE_LIST_H_XXREQ_UCHAR4**](../rag-optimized/settings/CODE_LIST_H_XXREQ_UCHAR4.md) | Admin | `List:True:True,False:False` | List for User Field 4 |
| [**CODE_LIST_H_XXREQ_UCHAR5**](../rag-optimized/settings/CODE_LIST_H_XXREQ_UCHAR5.md) | Admin | `List:True:Choice 1,False:Choice 2` | List for User Field 5 |
| [**DELIVER_TO_BLANK_DEFAULT**](../rag-optimized/settings/DELIVER_TO_BLANK_DEFAULT.md) | Purchasing |  | Default deliver-to value used when deliver-to field is left blank on requisition. |
| [**EMT_REQ_TYPE**](../rag-optimized/settings/EMT_REQ_TYPE.md) | Admin |  | Technical - Do Not Modify without consulting ISS |
| [**ITEM_ADD_DESC2_ALLOW_BLANK**](../rag-optimized/settings/ITEM_ADD_DESC2_ALLOW_BLANK.md) | Purchasing | `FALSE` | TRUE \| FALSE. If TRUE, allows adding catalog items with blank secondary description. |
| [**MRO_ITEMS_REQ_TYPES**](../rag-optimized/settings/MRO_ITEMS_REQ_TYPES.md) | Purchasing |  | Comma-separated requisition types. Types that allow MRO (Maintenance, Repair, Operations) items. |
| [**PURGE_REQ_DAYS**](../rag-optimized/settings/PURGE_REQ_DAYS.md) | Admin | `90` | This setting allows the administrator to set how many days a requisition will be purged based on no activity from either the entry date, last audit record date(header or detail), or last approval r... |
| [**PURGE_REQ_NOTIFY_DAYS**](../rag-optimized/settings/PURGE_REQ_NOTIFY_DAYS.md) | Admin | `10` | This setting allows the administrator to set how many days in advanced the originator will get notified before a requisition is purged from the iPurchase system. The setting works in conjunction wi... |
| [**REQUISITION_PREFIX**](../rag-optimized/settings/REQUISITION_PREFIX.md) | Power Users | `T` | This setting allows the administrator to set a special character to be used for the requisition prefix. |
| [**REQUISITION_TYPES**](../rag-optimized/settings/REQUISITION_TYPES.md) | Finance | `List:Expense:Expense,Capital,Contract,Tooling,Other,` | Use the prefix "LIST:" followed by a comma-separated list of values. This will tell iPurchase that the specified list is to be used. Example: LIST:expense:Expense Req,Capex,Inventory,etc All the sy... |
| [**REQ_INQUIRY_BUYER_ALWAYS**](../rag-optimized/settings/REQ_INQUIRY_BUYER_ALWAYS.md) | Purchasing | `FALSE` | TRUE \| FALSE. If TRUE, buyers can always see all requisitions in inquiry. |
| [**REQ_INQUIRY_FIELDS**](../rag-optimized/settings/REQ_INQUIRY_FIELDS.md) | Power Users |  | Comma separated list of fields that will be shown as columns in requisition inquiry. |
| [**REQ_INQ_HIDDEN_ELEMENTS**](../rag-optimized/settings/REQ_INQ_HIDDEN_ELEMENTS.md) | ISS |  | Technical - Do Not Modify without consulting ISS |
| [**REQ_MNT_HIDDEN_ELEMENTS**](../rag-optimized/settings/REQ_MNT_HIDDEN_ELEMENTS.md) | Power Users |  | Technical - Do Not Modify without consulting ISS |
| [**REQ_MNT_HIDDEN_HEADER_FIELDS**](../rag-optimized/settings/REQ_MNT_HIDDEN_HEADER_FIELDS.md) | Power Users | `h_production,h_xxreq_uchar1,h_xxreq_uchar2,h_xxreq_uchar3,h_xxreq_uchar4,h_xxreq_uchar5,h_all_items,h_supplier_fax,h_req_perf,h_req_cons,h_xxreq_blanket,h_high_priority` | Comma separated list of fields that are hidden at the header. This should not be changed unless you want to hide other header fields. |
| [**REQ_MNT_HIDDEN_LINE_FIELDS**](../rag-optimized/settings/REQ_MNT_HIDDEN_LINE_FIELDS.md) | Power Users | `h_line_xxreqd_tax_usage,h_line_xxreqd_tax_class,h_line_xxreqd_tax_env,h_xxreqd_uchar1,h_xxreqd_uchar2,h_xxreqd_uchar3,h_xxreqd_uchar4,h_xxreqd_uchar5,h_xxreqd_uchar6,h_xxreqd_uchar7,h_xxreqd_uchar8,h_xxreqd_uchar9,h_xxreqd_uchar10,h_xxreqd_ulog1,h_xxreqd_ulog2,h_xxreqd_ulog3,h_xxreqd_ulog4,h_xxreqd_ulog5,h_line_project,h_line_tool_id,h_line_ar,h_line_vendor,h_line_vendor_name,h_line_mro_type,h_line_po_nbr,h_line_perf_date,h_line_freight_cost,h_line_other_cost` | These are the list of fields that are hidden at the line level. These should not be changed unless you want to hide other line fields. |
| [**RT_INVENTORY_ITEM_ONLY**](../rag-optimized/settings/RT_INVENTORY_ITEM_ONLY.md) | Purchasing |  | Comma-separated req types. Types that require items to be in inventory catalog. |
| [**RT_[Requisition Type]_ACCESS**](<../rag-optimized/settings/RT_[Requisition Type]_ACCESS.md>) | Finance | `*` | Comma separated list of User ID's or Group ID's that are allowed to create a requisition for the given requisition type. Asterisk indicates everyone, a blank indicates no one. All other users will ... |
| [**RT_[Requisition Type]_ACCOUNT_DEFAULT**](<../rag-optimized/settings/RT_[Requisition Type]_ACCOUNT_DEFAULT.md>) | Finance |  | Substitute the requisition type for "[REQUISITION TYPE]". This is the default Account to be used for the specified requisition type |
| [**RT_[Requisition Type]_ACCOUNT_RANGE**](<../rag-optimized/settings/RT_[Requisition Type]_ACCOUNT_RANGE.md>) | Finance |  | Substitute the requisition type for "[REQUISITION TYPE]". This setting allows specifying valid accounts for a specific requisition type. The field uses the Progress "Can-Do" function. See Progress ... |
| [**RT_[Requisition Type]_ACCOUNT_READONLY**](<../rag-optimized/settings/RT_[Requisition Type]_ACCOUNT_READONLY.md>) | Admin |  | TRUE or FALSE Substitute the requisition type for "[REQUISITION TYPE]". This setting determines whether the users can change the account during line entry and is specific to the requisition type sp... |
| [**RT_[Requisition Type]_DEFAULT_BUYER**](<../rag-optimized/settings/RT_[Requisition Type]_DEFAULT_BUYER.md>) | Purchasing |  | See DEFAULT_BUYER |
| [**RT_[Requisition Type]_DEPT_DEFAULT**](<../rag-optimized/settings/RT_[Requisition Type]_DEPT_DEFAULT.md>) | Finance |  | Substitute the requisition type for "[REQUISITION TYPE]". This is the default Department to be used for the specified requisition type. It will override the default department specified on the user... |
| [**RT_[Requisition Type]_DEPT_RANGE**](<../rag-optimized/settings/RT_[Requisition Type]_DEPT_RANGE.md>) | Finance |  | Substitute the requisition type for "[REQUISITION TYPE]". This setting allows specifying valid departments (cost centers) for a specific requisition type. The field uses the Progress "Can-Do" funct... |
| [**RT_[Requisition Type]_DEPT_READONLY**](<../rag-optimized/settings/RT_[Requisition Type]_DEPT_READONLY.md>) | Admin |  | TRUE or FALSE Substitute the requisition type for "[REQUISITION TYPE]". This setting determines whether the users can change the department during line entry and is specific to the requisition type... |
| [**RT_[Requisition Type]_GL_OVERRIDE**](<../rag-optimized/settings/RT_[Requisition Type]_GL_OVERRIDE.md>) | Finance | `False ` | True or False If you set this setting to TRUE, then all items entered in the line entry screen for the specified requisition type will have the account, sub-account, and cost center set to the valu... |
| [**RT_[Requisition Type]_INVENTORY_ITEM_ONLY**](<../rag-optimized/settings/RT_[Requisition Type]_INVENTORY_ITEM_ONLY.md>) | Admin |  | True or False For Inventory as an example, only Inventory items can be purchased |
| [**RT_[Requisition Type]_REQUIRE_PROJECT**](<../rag-optimized/settings/RT_[Requisition Type]_REQUIRE_PROJECT.md>) | Admin |  | Comma separated list of requisition types which will require a project code listed. |
| [**RT_[Requisition Type]_SUB_ACCOUNT_DEFAULT**](<../rag-optimized/settings/RT_[Requisition Type]_SUB_ACCOUNT_DEFAULT.md>) | Finance |  | Substitute the requisition type for "[REQUISITION TYPE]". This is the default Sub Account to be used for the specified requisition type. |
| [**RT_[Requisition Type]_SUB_ACCOUNT_RANGE**](<../rag-optimized/settings/RT_[Requisition Type]_SUB_ACCOUNT_RANGE.md>) | Finance |  | Substitute the requisition type for "[REQUISITION TYPE]". This setting allows specifying valid sub accounts for a specific requisition type. The field uses the Progress "Can-Do" function. See Progr... |
| [**RT_[Requisition Type]_SUB_ACCOUNT_READONLY**](<../rag-optimized/settings/RT_[Requisition Type]_SUB_ACCOUNT_READONLY.md>) | Admin |  | TRUE or FALSE Substitute the requisition type for "[REQUISITION TYPE]". This setting determines whether the users can change the sub account during line entry and is specific to the requisition typ... |
| [**RT_[Requisition Type]_[SITE]_DEFAULT_BUYER**](<../rag-optimized/settings/RT_[Requisition Type]_[SITE]_DEFAULT_BUYER.md>) | Purchasing |  | See DEFAULT_BUYER |
| [**RT_[Requisition Type]_[Site]_ACCOUNT_RANGE**](<../rag-optimized/settings/RT_[Requisition Type]_[Site]_ACCOUNT_RANGE.md>) | Finance |  | Substitute the requisition type for "[REQUISITION TYPE]" and site for "[SITE]". This setting allows specifying valid accounts for a specific requisition type and site specified. The field uses the ... |
| [**RT_[Requisition Type]_[Site]_ACCOUNT_READONLY**](<../rag-optimized/settings/RT_[Requisition Type]_[Site]_ACCOUNT_READONLY.md>) | Admin | `False ` | TRUE or FALSE Substitute the requisition type for "[REQUISITION TYPE]" and site for "[SITE]". This setting determines whether the users can change the account during line entry and is specific to t... |
| [**RT_[Requisition Type]_[Site]_DEPT_DEFAULT**](<../rag-optimized/settings/RT_[Requisition Type]_[Site]_DEPT_DEFAULT.md>) | Finance |  | Substitute the requisition type for "[REQUISITION TYPE]" and site for "[SITE]". This is the default Department to be used for the specified requisition type and site. It will override the default d... |
| [**RT_[Requisition Type]_[Site]_DEPT_RANGE**](<../rag-optimized/settings/RT_[Requisition Type]_[Site]_DEPT_RANGE.md>) | Finance |  | Substitute the requisition type for "[REQUISITION TYPE]" and site for "[SITE]". This setting allows specifying valid departments (cost centers) for a specific requisition type. The field uses the P... |
| [**RT_[Requisition Type]_[Site]_DEPT_READONLY**](<../rag-optimized/settings/RT_[Requisition Type]_[Site]_DEPT_READONLY.md>) | Finance |  | TRUE or FALSE Substitute the requisition type for "[REQUISITION TYPE]" and site for "[SITE]". This setting determines whether the users can change the department during line entry and is specific t... |
| [**RT_[Requisition Type]_[Site]_GL_OVERRIDE**](<../rag-optimized/settings/RT_[Requisition Type]_[Site]_GL_OVERRIDE.md>) | Finance | `False ` | True or False If you set this setting to TRUE, then all items entered in the line entry screen for the specified requisition type and site combination will have the account, sub-account, and cost c... |
| [**RT_[Requisition Type]_[Site]_SUB_ACCOUNT_DEFAULT**](<../rag-optimized/settings/RT_[Requisition Type]_[Site]_SUB_ACCOUNT_DEFAULT.md>) | Finance |  | Substitute the requisition type for "[REQUISITION TYPE]" and site for "[SITE]". This is the default Sub Account to be used for the specified requisition type and site combination. |
| [**RT_[Requisition Type]_[Site]_SUB_ACCOUNT_RANGE**](<../rag-optimized/settings/RT_[Requisition Type]_[Site]_SUB_ACCOUNT_RANGE.md>) | Finance |  | Substitute the requisition type for "[REQUISITION TYPE]" and site for "[SITE]". This setting allows specifying valid sub accounts for a specific requisition type and site combination. The field use... |
| [**RT_[Requisition Type]_[Site]_SUB_ACCOUNT_READONLY**](<../rag-optimized/settings/RT_[Requisition Type]_[Site]_SUB_ACCOUNT_READONLY.md>) | Admin |  | TRUE or FALSE Substitute the requisition type for "[REQUISITION TYPE]" and site for "[Site]". This setting determines whether the users can change the sub account during line entry and is specific ... |
| [**SYNC_REQ_DET**](../rag-optimized/settings/SYNC_REQ_DET.md) | Purchasing | `TRUE` | A setting of True will synchronize iPurchase Requisition Lines with the requisition (req_det) functionality in QAD. Only items which are planned by MRP will be synchronized |

## Security & Authentication

| Setting | Owner | Default | Description |
|---------|-------|---------|-------------|
| [**ADMIN_IP**](../rag-optimized/settings/ADMIN_IP.md) | Admin |  | Comma-separated IP addresses. Restricts admin features to specific IP addresses. If blank, all IPs are allowed. Used for IP-based access control. |
| [**ALLOW_CHANGE_PASSWORD**](../rag-optimized/settings/ALLOW_CHANGE_PASSWORD.md) | Admin | `*` | Comma separated list of User IDs or Group ID's that are allowed to change passwords. Asterisk indicates everyone, a blank indicates no one. This setting determines whether a user will have the opti... |
| [**ALLOW_MULTIPLE_SESSIONS**](../rag-optimized/settings/ALLOW_MULTIPLE_SESSIONS.md) | Admin | `FALSE` | TRUE \| FALSE. If TRUE, allows users to have multiple simultaneous login sessions. SECURITY RISK if enabled without proper controls. |
| [**FAILED_LOGIN_ATTEMPTS**](../rag-optimized/settings/FAILED_LOGIN_ATTEMPTS.md) | Power Users | `3` | Identifies how many consecutive failed login attempts will be allowed before disabling a user |
| [**IGNORE_IPADDR_SECURITY**](../rag-optimized/settings/IGNORE_IPADDR_SECURITY.md) | IT | `TRUE` |  |
| [**IGNORE_PASSWORDS_ON_TEST**](../rag-optimized/settings/IGNORE_PASSWORDS_ON_TEST.md) | IT | `TRUE` | TRUE \| FALSE. When TRUE and the environment variable TEST_SYSTEM=TRUE, allows users to login with blank passwords. Used for dev/test environments to simplify testing without requiring password man... |
| [**LOGIN_BACK_IN_OFFICE**](../rag-optimized/settings/LOGIN_BACK_IN_OFFICE.md) | Power Users | `ASK` | If you currently have the Out-Of-Office setting on, this setting can automatically turn it off when you login. A setting of "ASK" will prompt the user if they want to turn off OOF, but only once ev... |
| [**LOGIN_GOTO_CATALOG**](../rag-optimized/settings/LOGIN_GOTO_CATALOG.md) | Admin |  | Comma Separated list of User ID's or Group ID's that will be directed to the catalog screen as their landing page. Asterisk indicates everyone, a blank indicates no one. |
| [**LOGIN_GOTO_MNT**](../rag-optimized/settings/LOGIN_GOTO_MNT.md) | Power Users | `TRUE` | Comma separated list of User ID's or Group ID's that will always be logged into the requisition workbench. This only applies to non-approvers. Asterisk indicates everyone, a blank indicates no one. |
| [**LOGIN_HIDE_FORGOT_PASSWORD**](../rag-optimized/settings/LOGIN_HIDE_FORGOT_PASSWORD.md) | Admin |  | Hide the Forgot Password link on the login screen |
| [**LOGIN_HIDE_KEEP_ME_LOGGED_IN**](../rag-optimized/settings/LOGIN_HIDE_KEEP_ME_LOGGED_IN.md) | Admin |  | Hide the Keep me logged in link on the login screen |
| [**LOGIN_HIDE_REQUEST_ACCESS**](../rag-optimized/settings/LOGIN_HIDE_REQUEST_ACCESS.md) | Admin |  | Hide the Request Access link on the login screen |
| [**LOGIN_LIMIT_TO**](../rag-optimized/settings/LOGIN_LIMIT_TO.md) | Admin |  | Comma separated list of User ID's or Group ID's that are allowed to login to the system. This setting is used for when putting the system in Admin mode (upgrade or new release). Asterisk indicates ... |
| [**LOGIN_USE_AD**](../rag-optimized/settings/LOGIN_USE_AD.md) | Admin |  | Auto login user if using NTLM Active Directory security. |
| [**LOGIN_USE_AD_CMD**](../rag-optimized/settings/LOGIN_USE_AD_CMD.md) | Admin |  | Command for AD authentication validation. |
| [**LOGIN_USE_AD_URL**](../rag-optimized/settings/LOGIN_USE_AD_URL.md) | Admin |  | URL for AD authentication service. |
| [**LOGIN_USE_SSO**](../rag-optimized/settings/LOGIN_USE_SSO.md) | Admin | `FALSE` | TRUE \| FALSE. Enable SSO authentication. |
| [**LOGIN_VIEW_CONTENT**](../rag-optimized/settings/LOGIN_VIEW_CONTENT.md) | Power Users | `1,0,1` | This setting allows the administrator to turn off the recent news, events, and video sections from the login page.  To turn these functions off the administrator would need to change the default se... |
| [**NO_PASSWORD_ON_APPROVE**](../rag-optimized/settings/NO_PASSWORD_ON_APPROVE.md) | Admin |  | Comma separated list of User ID's or Group ID's that will not be prompted for their password when approving or rejecting a requisition.  Asterisk indicates everyone, a blank indicates no one. |
| [**NO_QAD_AUTHENTICATION**](../rag-optimized/settings/NO_QAD_AUTHENTICATION.md) | Admin | `true` | Do not use QAD passwords for users that are also in QAD. Let iPurchase manage those passwords. |
| [**PASSWORD_EXPIRE_DAYS**](../rag-optimized/settings/PASSWORD_EXPIRE_DAYS.md) | Admin | `45` | This setting allows the administrator to set how often passwords need to be reset. |
| [**PASSWORD_REMINDER_DAYS**](../rag-optimized/settings/PASSWORD_REMINDER_DAYS.md) | Admin | `7` | This setting allows the administrator to set how many days before the password expires to notify user when logging in. |
| [**PASSWORD_RESET_TIMEOUT**](../rag-optimized/settings/PASSWORD_RESET_TIMEOUT.md) | Admin |  | Technical - Do Not Modify without consulting ISS |
| [**PASSWORD_RULES**](../rag-optimized/settings/PASSWORD_RULES.md) | Admin | `1,0,0,0,0,6,0` | Comma-Separated list of preferences (no spaces). There are 7 entries in this field: 1. Require a number in the password 2. Require a non alpha-numeric character in the password 3. Require a number ... |
| [**REMOVE_SAVE_PASSWORD**](../rag-optimized/settings/REMOVE_SAVE_PASSWORD.md) | Admin | `FALSE` | Removes the options of saving your password on the login screen. Users will need to enter their password every time. |
| [**SSO_CLIENT_REDIRECT_URL**](../rag-optimized/settings/SSO_CLIENT_REDIRECT_URL.md) | Admin |  | URL to redirect to after SSO authentication. |
| [**UNSAFE_ID_CHARACTERS**](../rag-optimized/settings/UNSAFE_ID_CHARACTERS.md) | Admin |  | Characters prohibited in user IDs and identifiers for security. |

## System Configuration

| Setting | Owner | Default | Description |
|---------|-------|---------|-------------|
| [**AUDIT_TABLE_EXCEPT**](../rag-optimized/settings/AUDIT_TABLE_EXCEPT.md) | Admin |  | Comma-separated field names. Fields to exclude from audit trail for the specified table. Replace {TABLE} with actual table name (e.g., AUDIT_xxreq_mstr_EXCEPT). Used to reduce audit trail volume. |
| [**CODE_LIST_H_CREDIT_TERMS**](../rag-optimized/settings/CODE_LIST_H_CREDIT_TERMS.md) | Admin |  | LIST format. Dropdown values for credit terms. Format: LIST:code:description,code:description |
| [**COMPANY_NAME**](../rag-optimized/settings/COMPANY_NAME.md) | Admin |  | Company name displayed on reports, purchase orders, and printed documents. |
| [**DEFAULT_ACCT**](../rag-optimized/settings/DEFAULT_ACCT.md) | Admin |  | The Default Account is used when creating requisition from catalogs and punchouts. The order in which iPurchase determines the account for a requisition created from a Punchout or Catalog is as fol... |
| [**DEFAULT_BILLTO**](../rag-optimized/settings/DEFAULT_BILLTO.md) | Finance |  | The administrator can enter a default value for the "Bill To" field. |
| [**DEFAULT_BLANKET_CYCLE**](../rag-optimized/settings/DEFAULT_BLANKET_CYCLE.md) | Purchasing |  | After the administrator has added values to the CODE_LIST_H_BLANKET_CYCLE setting, they can add one of the values in that setting to this setting, to be the default value for the cycle code drop do... |
| [**DEFAULT_CC**](../rag-optimized/settings/DEFAULT_CC.md) | Finance |  | Administrator can set the default Cost Center or Departments for Punchouts and Catalog orders. |
| [**DEFAULT_CURRENCY**](../rag-optimized/settings/DEFAULT_CURRENCY.md) | Finance |  | The administrator can set a default currency for iPurchase.  Must be a valid currency. |
| [**DEFAULT_FREIGHTTERMS**](../rag-optimized/settings/DEFAULT_FREIGHTTERMS.md) | Finance |  | Administrator can set the default value for "Who's Paying Freight" field. |
| [**DEFAULT_LEADTIME**](../rag-optimized/settings/DEFAULT_LEADTIME.md) | Purchasing | `0` | This setting will set the number of days to add to today's date in order to calculate the Need Date on the requisition header. |
| [**DEFAULT_REQTYPE**](../rag-optimized/settings/DEFAULT_REQTYPE.md) | Power Users |  | In this setting the administrator can set the default value for "Requisition Type" field. |
| [**EA_EXPORT_FOLDER**](../rag-optimized/settings/EA_EXPORT_FOLDER.md) | Admin |  | Directory path on application server. Folder where Enterprise Analytics export files are written. |
| [**EXCEL_EXPORT_APPROVALS**](../rag-optimized/settings/EXCEL_EXPORT_APPROVALS.md) | Admin | `FALSE` | TRUE \| FALSE. If TRUE, allows exporting approval data to Excel format. |
| [**FILE_UPLOAD_TYPES**](../rag-optimized/settings/FILE_UPLOAD_TYPES.md) | Admin |  | Comma-separated file extensions. Allowed file types for document uploads (e.g., pdf,doc,docx,xlsx). |
| [**JOB_RETRY_EMAIL_LAST**](../rag-optimized/settings/JOB_RETRY_EMAIL_LAST.md) | Admin | `FALSE` | TRUE \| FALSE. If TRUE, sends failure email only on final retry attempt rather than every failure. |
| [**LICENSE**](../rag-optimized/settings/LICENSE.md) | Admin |  | Software license key for iPurchase application. |
| [**NOTES_POPUP**](../rag-optimized/settings/NOTES_POPUP.md) | Admin | `FALSE` | TRUE \| FALSE. If TRUE, displays notes in popup window instead of inline. |
| [**PRINT_COMMAND**](../rag-optimized/settings/PRINT_COMMAND.md) | Admin |  | OS command for printing documents (e.g., lp, lpr). |
| [**SHOW_INVOICE_INQUIRY**](../rag-optimized/settings/SHOW_INVOICE_INQUIRY.md) | Admin | `FALSE` | TRUE \| FALSE. Show invoice inquiry link. |
| [**SHOW_PO_REV_ON_INQUIRY**](../rag-optimized/settings/SHOW_PO_REV_ON_INQUIRY.md) | Admin | `FALSE` | TRUE \| FALSE. Show PO revision number on inquiry. |
| [**SHOW_PO_STATUS_ON_REQ_INQUIRY**](../rag-optimized/settings/SHOW_PO_STATUS_ON_REQ_INQUIRY.md) | Admin | `FALSE` | TRUE \| FALSE. Show PO status on requisition inquiry. |
| [**SHOW_REQ_REV_ON_INQUIRY**](../rag-optimized/settings/SHOW_REQ_REV_ON_INQUIRY.md) | Admin | `FALSE` | TRUE \| FALSE. Show requisition revision on inquiry. |
| [**SHOW_SO_INQUIRY**](../rag-optimized/settings/SHOW_SO_INQUIRY.md) | Admin | `FALSE` | TRUE \| FALSE. Show sales order inquiry link. |
| [**SMS_TO**](../rag-optimized/settings/SMS_TO.md) | Admin |  | Phone numbers for SMS notifications. |
| [**TEST_SETTINGS**](../rag-optimized/settings/TEST_SETTINGS.md) | Admin |  | Comma-separated list of environment-specific settings that should be preserved when copying production database to dev/test. When production DB is copied down, these settings would be overwritten w... |
| [**TEST_SYSTEM**](../rag-optimized/settings/TEST_SYSTEM.md) | Admin | `FALSE` | ⚠️ DEPRECATED - Use OS environment variable TEST_SYSTEM instead. This setting is no longer used. Set TEST_SYSTEM=TRUE as an environment variable on the broker/PASOE instance for dev/test environments. |
| [**WINDOWS_TASK_NAME**](../rag-optimized/settings/WINDOWS_TASK_NAME.md) | Admin |  | Windows Task Scheduler task name for iPurchase scheduled jobs. |
| [**WORK_DAY_START_TIME**](../rag-optimized/settings/WORK_DAY_START_TIME.md) | Admin | `08:00` | Time (HH:MM). Start of business day for escalations/notifications. |
| [**WORK_DAY_STOP_TIME**](../rag-optimized/settings/WORK_DAY_STOP_TIME.md) | Admin | `17:00` | Time (HH:MM). End of business day for escalations/notifications. |

## Uncategorized

| Setting | Owner | Default | Description |
|---------|-------|---------|-------------|
| [**ADVISE_GROUP_MEMBERS**](../rag-optimized/settings/ADVISE_GROUP_MEMBERS.md) | Power Users | `FALSE` | This setting will send out emails to other users in a group when one of the group members approves a requisition when set to true. |
| [**ALLOWED_DOMAINS**](../rag-optimized/settings/ALLOWED_DOMAINS.md) | ISS | `QAD` | Enter a comma-separated list of domain codes to be allowed in iPurchase. This can be changed for a given user in User Maintenance |
| [**ALLOWED_EXTENSIONS**](../rag-optimized/settings/ALLOWED_EXTENSIONS.md) | Admin | `!exe,!dll,!js*,!com,!bat,!lnk,!ws*,!scr,!msi,*` | This is a comma separated list of allowed or not-allowed file extensions which can be uploaded to iPurchase. This works using the Progress "can-do" function. See Progress Help if needed A default v... |
| [**APP_RULE_FIELDS**](../rag-optimized/settings/APP_RULE_FIELDS.md) | ISS |  | List of field name from xxreq_mstr and xxreqd_det which appear in the Approval Rule Maintenance Screen for which you want to change the labels for. This list must match in size with the list in set... |
| [**APP_RULE_LABELS**](../rag-optimized/settings/APP_RULE_LABELS.md) | ISS |  | List of labels for the fields listed in setting APP_RULE_FIELDS |
| [**APP_RULE_SKIP_FIELDS**](../rag-optimized/settings/APP_RULE_SKIP_FIELDS.md) | ISS |  | List of fields from xxreq_mstr and xxreqd_det that you don't want to show in the Approval Rule Maintenance Screen. |
| [**ARCHIVE_FOLDER**](../rag-optimized/settings/ARCHIVE_FOLDER.md) | IT | `archive` | This should not be changed unless advised by ISS Group This is a temporary storage area for requisitions being transferred to or from the production and archive systems |
| [**AUDIT_TRAIL_ACTION_LIST**](../rag-optimized/settings/AUDIT_TRAIL_ACTION_LIST.md) | ISS | `,Create,Delete,Write` | Technical - Do Not Modify without consulting ISS |
| [**AUDIT_TRAIL_DOMAIN_EXEMPTION**](../rag-optimized/settings/AUDIT_TRAIL_DOMAIN_EXEMPTION.md) | ISS | `pf_mstr,wus_mstr,wgr_mstr,wugr_mstr` | Technical - Do Not Modify without consulting ISS |
| [**AUDIT_TRAIL_TABLE_LABEL**](../rag-optimized/settings/AUDIT_TRAIL_TABLE_LABEL.md) | ISS | `,Requisition Detail,Requisition Header,Rule Field,Rule Header,System Settings,Group Master,User Group Relations,User Master` | Technical - Do Not Modify without consulting ISS |
| [**AUDIT_TRAIL_TABLE_LIST**](../rag-optimized/settings/AUDIT_TRAIL_TABLE_LIST.md) | ISS | `,xxreqd_det,xxreq_mstr,xxappfield,xxapprule,pf_mstr,wgr_mstr,wugr_mstr,wus_mstr` | Technical - Do Not Modify without consulting ISS |
| [**AUDIT_TRAIL_[XXX]**](<../rag-optimized/settings/AUDIT_TRAIL_[XXX].md>) | ISS |  | There are several settings all beginning with "AUDIT_TRAIL". These setting should not be updated as they have to do with the internals of the Audit Trail Inquiry. |
| [**AUDIT_TRANSACTION_LIST**](../rag-optimized/settings/AUDIT_TRANSACTION_LIST.md) | ISS |  | Technical - Do Not Modify without consulting ISS |
| [**AUDIT_WUS_MSTR_EXCEPT**](../rag-optimized/settings/AUDIT_WUS_MSTR_EXCEPT.md) | ISS | `wus_last_login` | Technical - Do Not Modify   The list of fields from the wus_mstr table will not be audited when changed. All other fields will show up in Audit when changed. |
| [**AUDIT_XXREQD_DET_EXCEPT**](../rag-optimized/settings/AUDIT_XXREQD_DET_EXCEPT.md) | ISS | `xxreqd_master_comments,` | Technical - Do Not Modify without consulting ISS |
| [**AUTO_ADD_DROPSHIP**](../rag-optimized/settings/AUTO_ADD_DROPSHIP.md) | Admin | `FALSE` | True or False - Default FALSE. Automatically adds "Dropship" as an option in the Ship To dropdown field in Requisition Workbench |
| [**AUTO_ADD_ITEM_MC_TYPES**](../rag-optimized/settings/AUTO_ADD_ITEM_MC_TYPES.md) | Purchasing | `PO` | In QAD master comments, there is a reference number to identify a master comment, if this reference number equals the items number then the master comment will be added to the requisition automatic... |
| [**AUTO_CHANGE_GL**](../rag-optimized/settings/AUTO_CHANGE_GL.md) | Power Users | `TRUE` | If your company's GL Account, Sub Account, and CC are set by having defaults at the Requisition or Requisition or Site level, then the GL information will change when you change Requisition Types. ... |
| [**BACKUP_DB**](../rag-optimized/settings/BACKUP_DB.md) | Admin | `../db/ipurchase.db` | iPurchase provides a rudimentary backup system. List the full pathname and database name of the iPurchase database |
| [**BACKUP_DB_KEEP_DAYS**](../rag-optimized/settings/BACKUP_DB_KEEP_DAYS.md) | Admin | `7` | How many days worth of iPurchase database backups to keep |
| [**BACKUP_DB_PATH**](../rag-optimized/settings/BACKUP_DB_PATH.md) | Admin | `../dbbackups` | The location where database backups are stored |
| [**BASE_NAME**](../rag-optimized/settings/BASE_NAME.md) | ISS | `/custom/ipurchase` | Technical - Do Not Modify without consulting ISS |
| [**BG_COLOR_ARCHIVE**](../rag-optimized/settings/BG_COLOR_ARCHIVE.md) | Admin | `#FAE0A0` | The background color of the Archive System - default brown |
| [**BG_COLOR_TEST**](../rag-optimized/settings/BG_COLOR_TEST.md) | Admin | `#d9f2e5` | The background color of the Archive System - default pink |
| [**CART_BREAK_BY**](../rag-optimized/settings/CART_BREAK_BY.md) | ISS | `xxcartd_det.xxcartd_vendor` | Technical - Do Not Modify without consulting ISS |
| [**CART_SUM_LINES**](../rag-optimized/settings/CART_SUM_LINES.md) | Admin | `False ` | Within a catalog requisition, iPurchase will add up the quantities of all the items chosen by default.  If the administrator sets this setting to true the system will display number of lines instea... |
| [**CAT_IMPORT_DIR**](../rag-optimized/settings/CAT_IMPORT_DIR.md) | Admin |  | The administrator will choose a folder on application server where catalog files will be dropped (when catalogs are sent directly from supplier - not supported in base). |
| [**COPY_USE_CURRENT_CONTACT**](../rag-optimized/settings/COPY_USE_CURRENT_CONTACT.md) | Power Users | `FALSE` | This setting allows the system to use the current supplier data from the ERP system when a requisition is copied instead of the supplier data coming from the requisition that is being copied. |
| [**CURRENCY_SYMBOLS**](../rag-optimized/settings/CURRENCY_SYMBOLS.md) | ISS | `US,$,USD,$,EUR,&euro;,GBP,&pound;,jpy,&yen;,YEN,&yen;,CHF,&#8355,ITL,&#8356,MXP,&#8369;,CAD, C$` | Comma-Separated List of Currency Codes and HTML symbol codes. For example the symbol for a Euro would be represented with the HTML code "&euro~;" Ensure to add a semi-colon before all semi-colons. |
| [**DATE_FORMAT**](../rag-optimized/settings/DATE_FORMAT.md) | Admin | `mdy` | This setting allows the administrator to globally change the format of the date fields in iPurchase. |
| [**DELIVER_TO_FILL_IN**](../rag-optimized/settings/DELIVER_TO_FILL_IN.md) | Power Users | `FALSE` | Rather than the Deliver To field being a drop down list of users defined in iPurchase, setting this to TRUE makes the deliver to field an non-validated text field. |
| [**DISCREPANCY_DELETE_HIDE**](../rag-optimized/settings/DISCREPANCY_DELETE_HIDE.md) | Admin | `FALSE` | If set to TRUE, will not show deleted items in the discrepancy report |
| [**DMS_PROGRAM**](../rag-optimized/settings/DMS_PROGRAM.md) | Admin |  | This is the name of the Progress Program which integrates with a document management system. |
| [**EDIT_ANYTIME**](../rag-optimized/settings/EDIT_ANYTIME.md) | Admin | `buyers` | Comma separated list of User ID's or Group ID's that are allowed to edit a Pending requisition at anytime. Asterisk indicates everyone, a blank indicates no one. There is currently a setting "ALWAY... |
| [**HELP_URL**](../rag-optimized/settings/HELP_URL.md) |  |  | If you've developed customized help, then enter the URL to that file here. ex. https://google.com |
| [**HIDE_MASTER_COMMENTS**](../rag-optimized/settings/HIDE_MASTER_COMMENTS.md) | Admin |  | Comma separated list of User ID's or Group ID's that will not get the master comments functionality. Asterisk indicates everyone, a blank indicates no one. |
| [**IPURCHASE_VERSION**](../rag-optimized/settings/IPURCHASE_VERSION.md) | ISS | `2023.0426` | Do Not Modify |
| [**ITEM_LOOKUP_NO_VP**](../rag-optimized/settings/ITEM_LOOKUP_NO_VP.md) | Purchasing | `FALSE` | Do not show vendor parts (vp_mstr) when searching for items in line entry. |
| [**ITEM_SEARCH_RECENT**](../rag-optimized/settings/ITEM_SEARCH_RECENT.md) | iPurchase will look for matches from previous requisitions." | `TRUE` | When entering line items |
| [**LINE_REJECTION_FINAL**](../rag-optimized/settings/LINE_REJECTION_FINAL.md) | Power Users | `TRUE` | If USE_LINE_APPROVALS = TRUE then you can also set whether or not any items which were previously rejected, can be re-approved by a subsequent approver. A value of TRUE will disallow anyone from ap... |
| [**LOCK_OUT_MINUTES**](../rag-optimized/settings/LOCK_OUT_MINUTES.md) | Admin | `10` | The number of minutes a user will be locked out after failing to login more than the value of setting FAILED_LOGIN_ATTEMPTS |
| [**LOGOFF_MINUTES**](../rag-optimized/settings/LOGOFF_MINUTES.md) | Power Users | `0` | Enter how many minutes of inactivity the system will wait until it logs a user off. |
| [**LOG_PURGE_DAYS**](../rag-optimized/settings/LOG_PURGE_DAYS.md) | Admin | `30` | Many log files are generated by iPurchase. These logs are useful for a short period of time, but in the log run they need to be purged. Temporary log file will be deleted once older than a rolling ... |
| [**MANDATORY_FIELDS**](../rag-optimized/settings/MANDATORY_FIELDS.md) | Admin | `h_buyer,xh_supplier_contact,xh_supplier_phone,xh_supplier_fax,xh_deliver_to2,xh_req_type,xh_supplier_email,xh_bill_to,xh_req_need,xh_site,xh_freight_terms,xh_ship_via` | Comma-Separated list of field names. The following fields can be either mandatory or optional. h_buyer,h_supplier_contact,h_supplier_phone,h_supplier_fax,h_deliver_to2,h_req_type,h_supplier_email,h... |
| [**MASTER_COMMENTS_ROLE_LIST**](../rag-optimized/settings/MASTER_COMMENTS_ROLE_LIST.md) | Purchasing | `*` | Comma-Separated list of group ID's or "*" for all. Only members of these groups will be allowed to enter or delete master comments from a requisition. |
| [**MAX_UPLOAD_MB**](../rag-optimized/settings/MAX_UPLOAD_MB.md) | IT | `10` | Maximum size in megabytes for attachments. |
| [**MEMO_ONLY**](../rag-optimized/settings/MEMO_ONLY.md) | Admin | `FALSE` | If this setting is true, then a user will not be allowed to order an item# which exists in the part master (pt_mstr) table. |
| [**MESSAGE_ERROR_TIMEOUT**](../rag-optimized/settings/MESSAGE_ERROR_TIMEOUT.md) | Power Users | `0` | This setting allows the administrator the ability to set the duration of how long the error message will stay on the screen. A value of 0 will indicate to keep the message on the screen indefinitel... |
| [**MESSAGE_WARNING_TIMEOUT**](../rag-optimized/settings/MESSAGE_WARNING_TIMEOUT.md) | Power Users | `5` | This setting allows the administrator the ability to set the duration of how long the warning message will stay on the screen. A value of 0 will indicate to keep the message on the screen indefinit... |
| [**NUMERIC_FORMAT_DECIMAL**](../rag-optimized/settings/NUMERIC_FORMAT_DECIMAL.md) | Admin | `.` | Usually a decimal point |
| [**NUMERIC_FORMAT_SEPARATOR**](../rag-optimized/settings/NUMERIC_FORMAT_SEPARATOR.md) | Admin | `,` | Usually a comma |
| [**OOF_LIMIT_BY_DOLLARS**](../rag-optimized/settings/OOF_LIMIT_BY_DOLLARS.md) | Admin | `FALSE` | A setting of True will only allow a user to delegate to another user who has at least the same dollar approval level. |
| [**OOF_LIMIT_TO**](../rag-optimized/settings/OOF_LIMIT_TO.md) | Admin |  | Comma separated list of User ID's or Group ID's that that can be chosen as delegates. Asterisk indicates everyone, a blank indicates no one. |
| [**OOF_NOTIFY_OLD**](../rag-optimized/settings/OOF_NOTIFY_OLD.md) | Power Users | `TRUE` | A setting of TRUE will email any existing pending requisitions to the newly assigned delegate. If the setting is FALSE, the delegate will not receive an email for any existing pending requisitions.... |
| [**REMOVE_ORIGINATOR_FROM_GROUP**](../rag-optimized/settings/REMOVE_ORIGINATOR_FROM_GROUP.md) | Admin | `TRUE` | If the originator is listed as a member of a group on the approval routing, if this person should be removed from the group set this setting to TRUE. |
| [**REMOVE_ORIG_CO**](../rag-optimized/settings/REMOVE_ORIG_CO.md) | Admin | `FALSE` | This setting does not allow originator to be an approver for their own requisition for Change Orders if set to true. |
| [**REMOVE_ORIG_RELEASE**](../rag-optimized/settings/REMOVE_ORIG_RELEASE.md) | Admin | `FALSE` | If set to true, this setting will remove the originator from the approver list on blanket release requisitions. |
| [**SHOW_ALLOCATION_CODES**](../rag-optimized/settings/SHOW_ALLOCATION_CODES.md) | Admin | `FALSE` | True/false to Show/Hide allocation codes in the account dropdown in req line maintenance. |
| [**SHOW_GRAPH**](../rag-optimized/settings/SHOW_GRAPH.md) | Admin | `buyers,admin` | Comma separated list of User ID's or group ID's that have access to the graphing functionality. Asterisk indicates everyone, a blank indicates no one. |
| [**SHOW_RULE_INFO**](../rag-optimized/settings/SHOW_RULE_INFO.md) | Power Users | `TRUE` | This setting will show the approval rule name when hovering over the Level or Seq field in the Approval History Tab. |
| [**TERMS_DISPLAY**](../rag-optimized/settings/TERMS_DISPLAY.md) | Purchasing | `TRUE` | This setting will display the supplier terms on the requisition header. |
| [**UNSPSC_FILTER**](../rag-optimized/settings/UNSPSC_FILTER.md) | Purchasing | `*` | To modify this setting to control which UNSPSC codes are available to choose from. The syntax for this settings uses the CAN-DO functionality similar to a lot of the other settings. To re-cap, the ... |
| [**USE_CHAINED_DELEGATES**](../rag-optimized/settings/USE_CHAINED_DELEGATES.md) | Power Users | `TRUE` | This setting will allow for unlimited levels of Out Of Office functionality. If user A delegates to user B, then user B also delegates to user C, can User C approve or reject a requisition on behal... |
| [**USE_LYNC**](../rag-optimized/settings/USE_LYNC.md) | Admin | `FALSE` | This setting allows the administrator to allow the use of Lync within the iPurchase solution. Requirements: Office 2010+ with Lync installed on desktop. iPurchase website must be in the "TRUSTED SI... |
| [**USE_SINGLE_LANGUAGE**](../rag-optimized/settings/USE_SINGLE_LANGUAGE.md) | then this will be the language selected for all users and the language selection box on the login screen will not be displayed." |  | If this is set to something like en-us" |

## User Management

| Setting | Owner | Default | Description |
|---------|-------|---------|-------------|
| [**ALLOW_BATCH_PO**](../rag-optimized/settings/ALLOW_BATCH_PO.md) | Power Users | `FALSE-ALWAYS` | This setting allows the administrator to set how the PO will be created in iPurchase. The options for this setting are: 1) FALSE - Default is set to create PO now. The last approver will still have... |
| [**ALLOW_BLANKET_RELEASE**](../rag-optimized/settings/ALLOW_BLANKET_RELEASE.md) | Power Users | `buyers` | Comma separated list of User ID's or Group ID's who are allowed to create releases against blanket POs. |
| [**ALLOW_BUG**](../rag-optimized/settings/ALLOW_BUG.md) | Admin |  | Can-Do list. Users/groups allowed to submit bug reports through the application interface. |
| [**ALLOW_CATALOG**](../rag-optimized/settings/ALLOW_CATALOG.md) | Admin | `*` | Comma separated list of User ID's or Group ID's that have access to the catalog function within iPurchase. |
| [**ALLOW_CATALOG_EDIT**](../rag-optimized/settings/ALLOW_CATALOG_EDIT.md) | Power Users | `buyers` | Comma separated list of User ID's or Group ID's that are who are allowed to edit items in a Catalog within iPurchase. Asterisk indicates everyone, a blank indicates no one. In order for the user to... |
| [**ALLOW_CATPO_PRICE_CHANGE**](../rag-optimized/settings/ALLOW_CATPO_PRICE_CHANGE.md) |  |  | Comma separated list of User IDs or Group ID's that are allowed to change prices on catalog and punchout items. Asterisk indicates everyone, a blank indicates no one |
| [**ALLOW_CONSOLIDATION**](../rag-optimized/settings/ALLOW_CONSOLIDATION.md) | Power Users | `FALSE` | This setting allows the administrator to turn On or Off the consolidation feature. |
| [**ALLOW_COPY_PASTE**](../rag-optimized/settings/ALLOW_COPY_PASTE.md) | description | `true` | This settings controls if users can copy paste in the requisition workbench. Sometimes copying from internet or PDF files cause item number |
| [**ALLOW_DELETE_NOT_SUBMITTED**](../rag-optimized/settings/ALLOW_DELETE_NOT_SUBMITTED.md) | Admin | `admin` | Comma separated list of User ID's or Group ID's who are allowed to delete a requisition that has not been submitted.  Asterisk indicates everyone, a blank indicates no one. |
| [**ALLOW_DELETE_PROCESSED**](../rag-optimized/settings/ALLOW_DELETE_PROCESSED.md) | Admin | `admin` | Comma separated list of User ID's or Group ID's who are allowed to delete a requisition that has been approved and a PO is already created.  Asterisk indicates everyone, a blank indicates no one. |
| [**ALLOW_FEEDBACK**](../rag-optimized/settings/ALLOW_FEEDBACK.md) | Admin |  | Can-Do list. Users/groups allowed to submit feedback through the application interface. |
| [**ALLOW_HOLD**](../rag-optimized/settings/ALLOW_HOLD.md) | Admin | `*` | Comma separated list of User ID's or Group ID's who are allowed to put a requisition on hold while it is pending. Asterisk indicates everyone, a blank indicates no one. Example: It would go on hold... |
| [**ALLOW_NEGATIVE_REQ**](../rag-optimized/settings/ALLOW_NEGATIVE_REQ.md) | Power Users |  | This setting will allow negative total requisition cost if set to True. |
| [**ALLOW_OOF**](../rag-optimized/settings/ALLOW_OOF.md) | Admin | `*` | Comma separated list of User ID's or Group ID's that are allowed to set Out of office. Asterisk indicates everyone, a blank indicates no one. This setting determines whether the system will support... |
| [**ALLOW_PO_LINE_HISTORY**](../rag-optimized/settings/ALLOW_PO_LINE_HISTORY.md) | Power Users | `buyers` | Comma separated list of User ID's or Group ID's that are allowed to view PO Line history. Use an asterisk for everyone. Leave blank for no one. |
| [**ALLOW_PO_PRINT**](../rag-optimized/settings/ALLOW_PO_PRINT.md) | Power Users | `*` | Comma separated list of User ID's or Group ID's that are allowed to print a purchase order. Use an asterisk for everyone. Leave blank for no one. |
| [**ALLOW_PUNCHOUT**](../rag-optimized/settings/ALLOW_PUNCHOUT.md) | Admin | `*` | Comma separated list of User ID's or Group ID's that are allowed to use punchouts. Asterisk indicates everyone, a blank indicates no one. This setting turns on or off the Punch-out functionality fo... |
| [**ALLOW_PUNCHOUT_COPY**](../rag-optimized/settings/ALLOW_PUNCHOUT_COPY.md) | Power Users |  | Comma separated list of User ID's or Group ID's that are allowed to copy punchout requisitions (prices may no longer be valid). Asterisk indicates everyone, a blank indicates no one. |
| [**ALLOW_REQ_AUDIT**](../rag-optimized/settings/ALLOW_REQ_AUDIT.md) | Admin |  | Can-Do list. Users/groups allowed to view requisition audit trail. Automatically disabled in archive systems. |
| [**ALLOW_REQ_ENTRY**](../rag-optimized/settings/ALLOW_REQ_ENTRY.md) | Admin | `*` | Comma separated list of User ID's or Group ID's that are allowed to access to the requisition entry screen.   Asterisk indicates everyone, a blank indicates no one. |
| [**ALLOW_REQ_INQUIRY**](../rag-optimized/settings/ALLOW_REQ_INQUIRY.md) | Admin | `*` | Comma separated list of User ID's or Group ID's that are allowed to access the requisition inquiry screen Asterisk indicates everyone, a blank indicates no one. |
| [**ALLOW_REQ_PRINT**](../rag-optimized/settings/ALLOW_REQ_PRINT.md) | Admin | `*` | Comma separated list of User ID's or Group ID's that are allowed to print requisitions.  Asterisk indicates everyone, a blank indicates no one. |
| [**ALLOW_RETRANSMIT_PO**](../rag-optimized/settings/ALLOW_RETRANSMIT_PO.md) | Admin | `buyers` | Comma separated list of User ID's or Group ID's that allow user to manually transmit cXML PO to Punchout supplier.  Asterisk indicates everyone, a blank indicates no one. |
| [**ALWAYS_ALLOW_ATTACHMENTS**](../rag-optimized/settings/ALWAYS_ALLOW_ATTACHMENTS.md) | Admin | `buyers` | Comma-Separated list of groups. Any member of these groups will be allowed to add attachments to any req at any time, even after the req is converted to a PO. |
| [**ALWAYS_ALLOW_REQ_EDITS**](../rag-optimized/settings/ALWAYS_ALLOW_REQ_EDITS.md) | Power Users |  | Comma separated list of User ID's or Group ID's that are allowed to modify any requisition at any time until it has been approved. You may also use "$xxreq_buyer" (without the quotes) as one of the... |
| [**ALWAYS_ALLOW_REQ_EDIT_ORIGINATOR**](../rag-optimized/settings/ALWAYS_ALLOW_REQ_EDIT_ORIGINATOR.md) | Power Users |  | The users listed here will be allowed to modify a requisition while it's being approved if the following scenarios are true: 1) They are listed as the originator or on behalf of. 2) They are an app... |
| [**BUDGET_ALLOW_NEW**](../rag-optimized/settings/BUDGET_ALLOW_NEW.md) | Admin |  | Comma Separated list of User ID's or Group ID's who are allowed to create new budgets in iPurchase. Asterisk indicates everyone, a blank indicates no one. |
| [**CATALOG_ALLOW_EXPORT**](../rag-optimized/settings/CATALOG_ALLOW_EXPORT.md) | Admin | `buyers,admin` | Comma Separated list of User ID's or Group ID's that are allowed to export catalogs.  Asterisk indicates everyone, a blank indicates no one. |
| [**CATALOG_ALLOW_IMPORT**](../rag-optimized/settings/CATALOG_ALLOW_IMPORT.md) | Admin | `buyers,admin` | Comma Separated list of User ID's or Group ID's that are allowed to import catalogs.  Asterisk indicates everyone, a blank indicates no one. |
| [**CATALOG_REQUEST_ALLOW_IMPORT**](../rag-optimized/settings/CATALOG_REQUEST_ALLOW_IMPORT.md) | Admin | `buyers,admin` | Comma Separated list of User ID's or Group ID's that can load a new approved catalog into iPurchase.  Asterisk indicates everyone, a blank indicates no one. This setting is related to CATALOG_ALLOW... |
| [**EMPLOYMENT_DEPT_LIST**](../rag-optimized/settings/EMPLOYMENT_DEPT_LIST.md) | Admin |  | Comma-separated department codes. Valid departments for user employment records/profiles. |
| [**EMPLOYMENT_DIVISION_LIST**](../rag-optimized/settings/EMPLOYMENT_DIVISION_LIST.md) | Admin |  | Comma-separated division codes. Valid divisions for user employment records/profiles. |
| [**INQUIRY_ALLOW_NEW_VIEWS**](../rag-optimized/settings/INQUIRY_ALLOW_NEW_VIEWS.md) | Admin |  | Comma separated list of User ID's or Group ID's that are allowed to create new views in requisition inquiry. Asterisk indicates everyone, a blank indicates no one. |
| [**INQUIRY_ALLOW_VIEWS**](../rag-optimized/settings/INQUIRY_ALLOW_VIEWS.md) | Admin |  | Comma separated list of User ID's or Group ID's that are allowed to see views. |
| [**LINE_VIEW_FIELDS**](../rag-optimized/settings/LINE_VIEW_FIELDS.md) | Power Users | `xxreqd_line_type:LT:1,full_item:Item:45,xxreqd_due_date:Due::center,xxreqd_acct::15:center,xxreqd_project,xxreqd_qty,xxreqd_cost` | System default for which fields are displayed in the Requisition Item browse. |
| [**QAD_INTERFACE_USER**](../rag-optimized/settings/QAD_INTERFACE_USER.md) | Admin |  | Use this setting to set the User ID for integration to QAD. This user ID will be used in QAD to create PO's. This user must be enabled in iPurchase and QAD. This user would need to be created befor... |
| [**RESTRICT_USER_ACCOUNTS**](../rag-optimized/settings/RESTRICT_USER_ACCOUNTS.md) | Power Users | `FALSE` | Is the Acct selection limited to those accounts defined in the user's profile? See RESTRICT_USER_DEPARTMENTS for more information on how to set the Acct field in User Maintenance |
| [**RESTRICT_USER_DEPARTMENTS**](../rag-optimized/settings/RESTRICT_USER_DEPARTMENTS.md) | Power Users | `FALSE` | Is the department selection limited to those departments defined in the user's profile?  If the value of this is True then in User Maintenance you should set up the "Default Dept" field as follows.... |
| [**RESTRICT_USER_SUB_ACCOUNTS**](../rag-optimized/settings/RESTRICT_USER_SUB_ACCOUNTS.md) | Power Users | `FALSE` | Is the Sub Acct selection limited to those sub accounts defined in the user's profile? See RESTRICT_USER_DEPARTMENTS for more information on how to set the Sub Acct field in User Maintenance |
| [**USER_IMPORT_FOLDER**](../rag-optimized/settings/USER_IMPORT_FOLDER.md) | Admin |  | Directory path on application server. Folder where user import files are placed for processing. |
| [**USER_PROFILE_FIELDS**](../rag-optimized/settings/USER_PROFILE_FIELDS.md) | Admin |  | Comma-separated field names. Custom user profile fields to display/edit. |
| [**VIEW_DEPARTMENT_REQS**](../rag-optimized/settings/VIEW_DEPARTMENT_REQS.md) | Admin | `FALSE` | TRUE \| FALSE. Allow viewing reqs by department. |
| [**VIEW_REQS_DEPARTMENT**](../rag-optimized/settings/VIEW_REQS_DEPARTMENT.md) | Admin | `FALSE` | TRUE \| FALSE. Restrict viewing to user's department reqs. |
| [**VIEW_REQS_RESTRICTED_MODE**](../rag-optimized/settings/VIEW_REQS_RESTRICTED_MODE.md) | Admin | `FALSE` | TRUE \| FALSE. Enable restricted mode for req viewing. |
| [**VIEW_SUPPLIER_DOCS**](../rag-optimized/settings/VIEW_SUPPLIER_DOCS.md) | Admin | `buyers,admin` | True or False or list of users groups. Default value is blank. Will give the users access to the "Contacts" button in Requisition Workbench |

## iApprove Integration

| Setting | Owner | Default | Description |
|---------|-------|---------|-------------|
| [**BUDGET_USE_IAPPROVE**](../rag-optimized/settings/BUDGET_USE_IAPPROVE.md) | Finance | `FALSE` | TRUE \| FALSE. If TRUE, uses iApprove system for budget workflows instead of iPurchase budget module. |
| [**CODE_LIST_H_SHIPVIA_XREF**](../rag-optimized/settings/CODE_LIST_H_SHIPVIA_XREF.md) | Purchasing |  | This setting defines a cross-reference between the selected iPurchase ship via, and the code or description that the vendor needs to see on their electronic purchase order. Only applies to Punchout... |
| [**CODE_LIST_H_SHIPVIA_XREF_[VENDOR NUMBER]**](<../rag-optimized/settings/CODE_LIST_H_SHIPVIA_XREF_[VENDOR NUMBER].md>) | Purchasing |  | This setting defines a cross-reference between the selected iPurchase ship via, and the code or description that the vendor needs to see on their electronic purchase order. Only applies to Punchout... |
| [**IAEAMJE_MSTR_REQ_PREFIX**](../rag-optimized/settings/IAEAMJE_MSTR_REQ_PREFIX.md) | ISS |  | Prefix for requisition numbers in iApprove EAM JE integration. |
| [**IAVD_MSTR_REQ_PREFIX**](../rag-optimized/settings/IAVD_MSTR_REQ_PREFIX.md) | ISS |  | Prefix for requisition numbers in iApprove vendor integration. |
| [**IA_APPROVAL_NOT_REQUIRED_EMAIL_SUBJECT**](../rag-optimized/settings/IA_APPROVAL_NOT_REQUIRED_EMAIL_SUBJECT.md) | Admin | `Approval Not Required` | Email subject line for iApprove notifications when approval is not required. |
| [**IA_APPROVAL_REMINDER_EMAIL_SUBJECT**](../rag-optimized/settings/IA_APPROVAL_REMINDER_EMAIL_SUBJECT.md) | Admin | `Approval Reminder` | Email subject line for iApprove approval reminder notifications. |
| [**IA_APPROVAL_REQUIRED_AGAIN_EMAIL_SUBJECT**](../rag-optimized/settings/IA_APPROVAL_REQUIRED_AGAIN_EMAIL_SUBJECT.md) | Admin | `Approval Required Again` | Email subject line when iApprove document requires re-approval. |
| [**IA_APPROVAL_REQUIRED_EMAIL_SUBJECT**](../rag-optimized/settings/IA_APPROVAL_REQUIRED_EMAIL_SUBJECT.md) | Admin | `Approval Required` | Email subject line for iApprove initial approval request notifications. |
| [**IA_APPROVED_EMAIL_SUBJECT**](../rag-optimized/settings/IA_APPROVED_EMAIL_SUBJECT.md) | Admin | `Approved` | Email subject line when iApprove document is approved. |
| [**IA_EMAIL_SUBJECT_APPEND**](../rag-optimized/settings/IA_EMAIL_SUBJECT_APPEND.md) | Admin |  | Text appended to all iApprove email subject lines. Used for environment identification (e.g., [TEST]). |
| [**IA_REJECTED_EMAIL_SUBJECT**](../rag-optimized/settings/IA_REJECTED_EMAIL_SUBJECT.md) | Admin | `Rejected` | Email subject line when iApprove document is rejected. |
| [**IA_RETRACTED_EMAIL_SUBJECT**](../rag-optimized/settings/IA_RETRACTED_EMAIL_SUBJECT.md) | Admin | `Retracted` | Email subject line when iApprove document is retracted by submitter. |


---

> **Note for AI/RAG:** A verbose, AI-optimized version of this documentation exists at `rag-optimized/system-settings-rag.md`. If modifying this file, regenerate the RAG version using `python3 scripts/gen_settings_rag.py`.
