# Header vs Line Evaluation - iPurchase Approval Rules

**Purpose:** Understanding how approval rules compare amounts - by total requisition (Header) or by individual line items (Line). This applies to both simple rules (xxapp_mstr.xxapp_which_cost) and complex rules (xxAppRule.xxAR_AmtType and xxAR_Eval_Lines).

**Keywords:** which cost, header vs line, line evaluation, amount comparison, xxapp_which_cost, xxAR_AmtType, xxAR_Eval_Lines, cross-department, split requisition, multi-department, line-by-line approval

### Overview

Every approval rule with amount thresholds must decide HOW to compare the requisition amount:

| Setting | Field (Simple Rules) | Field (Complex Rules) | Behavior |
|---------|---------------------|----------------------|----------|
| **Header** | `xxapp_which_cost = "Header"` | `xxAR_AmtType = "Header"` | Compare against total requisition amount |
| **Line** | `xxapp_which_cost = "Line"` | `xxAR_AmtType = "Line"` + `xxAR_Eval_Lines = TRUE` | Compare against each line item separately |

### Header Mode (Total Requisition Cost)

- Compares rule's min/max amount against the **total requisition amount** (`xxreq_cost_gl`)
- Creates **one approval record** if the rule matches
- Most common setting for standard approvals

**Best for:**
- Executive approvals ("CFO approves anything over $100K")
- Standard cost center approvals
- When you want simpler, faster routing

### Line Mode (Individual Line Evaluation)

- Compares rule's min/max amount against **each line item's amount** (`xxreqd_total_gl`)
- Can create **multiple approval records** from a single rule
- Each matching line generates its own approval requirement

**Best for:**
- Cross-department requisitions where each department approves their portion
- Commodity-specific approvals (different approvers by UNSPSC code)
- When you need granular control over who approves what

### Example Scenario

A $15,000 requisition with 3 lines charging to different cost centers:

| Line | Amount | Cost Center |
|------|--------|-------------|
| 1 | $8,000 | 8100 (Marketing) |
| 2 | $5,000 | 8200 (Engineering) |
| 3 | $2,000 | 8300 (Operations) |

**With Header evaluation:**
- Rule checks: Is $15,000 (total) within my amount range?
- Result: One approval record based on total amount
- The cost center filter would match only ONE of the cost centers (typically the first line or header default)

**With Line evaluation:**
- Rule checks each line: Is $8,000 within range? Is $5,000? Is $2,000?
- Result: Could generate up to 3 separate approval records
- Each line's cost center is evaluated, so CC 8100, 8200, and 8300 managers could each approve their portion

### Cross-Department Charging

Line evaluation is essential when requisitions charge to multiple departments:

**Scenario:** User in Marketing creates a $20K requisition:
- $12K for Marketing supplies (CC 8100)
- $8K for shared project with Engineering (CC 8200)

**Without Line evaluation:** Only Marketing manager approves (based on header cost center)

**With Line evaluation:** 
- Marketing manager approves the $12K portion
- Engineering manager approves the $8K portion
- Both departments have visibility and control over their budgets

### Configuration in Simple Rules (xxapp_mstr)

Set the `xxapp_which_cost` field:
- `"Header"` - Use total requisition amount
- `"Line"` - Evaluate each line separately

### Configuration in Complex Rules (xxAppRule)

Two fields control this behavior:

| Field | Value | Effect |
|-------|-------|--------|
| `xxAR_AmtType` | `"Header"` or `"Line"` | Which amount to compare |
| `xxAR_Eval_Lines` | `TRUE` or `FALSE` | Whether to create separate approval per matching line |

**Common combinations:**
- `AmtType="Header"`, `Eval_Lines=FALSE` - Standard header evaluation
- `AmtType="Line"`, `Eval_Lines=TRUE` - Full line-by-line evaluation with separate approvals
- `AmtType="Line"`, `Eval_Lines=FALSE` - Sum of matching lines only, one approval record

### When to Use Each

| Scenario | Recommended Setting |
|----------|-------------------|
| Executive approval (CFO, CEO) | Header |
| Standard cost center approval | Header |
| Cross-department requisitions | Line |
| Commodity-specific approval (by UNSPSC) | Line |
| Project-based approval across departments | Line |
| Fast, simple routing | Header |

### Related Settings

- `MULTIPLE_APPROVALS` - How to handle when same approver appears multiple times
- `APP_ORIG_OR_OBO` - Whether rules match against originator or On-Behalf-Of person
