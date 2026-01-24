# Purchase Orders FAQ

Common questions about PO creation, printing, and emailing.

---

## PO Creation

### When is a PO created?

Default behavior: PO is created immediately after the buyer (final approver) approves.

**Setting:** `BATCH_CREATE_PO_GROUPS = buyers`

### Which QAD user creates the POs?

iPurchase uses a single QAD interface account to create all POs.

**Settings:**
- `QAD_INTERFACE_USER` - QAD user ID
- `QAD_INTERFACE_PASSWORD` - QAD password

This account needs permission to PO maintenance, blanket POs, receiving, and PO print functions in QAD.

---

## PO Printing

### Who can print POs?

Controlled by `ALLOW_PO_PRINT` setting.

**Options:**
- `*` or blank = everyone
- `buyers,admin` = specific groups only

The PO print icon only appears for users in the allowed groups.

### What format are POs printed in?

Controlled by `PO_PRINT_PDF_FORMAT` setting.

**Options:**
- `graphical` - Uses iPurchase PO template
- QAD QRF - Uses QAD Reporting Framework (recommended if available)

### Can I add my company logo to POs?

Yes. Set `PO_LOGO` to point to your logo file.

### Can I add Terms & Conditions to POs?

Yes. Use `AUTO_COMMENTS_OTHER = Terms_and_Conditions` to attach a T&C document to all POs.

### Can buyer signatures be printed on POs?

Yes. Provide buyer signatures in .png format and configure in system settings.

---

## Emailing POs

### Can POs be automatically emailed to suppliers?

Yes. Set `EMAIL_SUPPLIER_PO = TRUE`

**Related Settings:**

| Setting | Description |
|---------|-------------|
| `EMAIL_SUPPLIER_PO` | TRUE = Auto-email on approval |
| `EMAIL_SUPPLIER_ATTACH_FILES` | Attach files to email |
| `EMAIL_SUPPLIER_ATTACH_LINKS` | Include attachment links |

**Requirement:** Supplier email addresses must be in QAD vendor master.

### Can buyers manually email POs?

Yes. Set `ALLOW_MANUAL_EMAIL_PO = buyers`

This shows the EMAIL PO button for specified groups.

### Who gets copied on supplier PO emails?

Controlled by `EMAIL_SUPPLIER_PO_CC` setting.

**Default:** `$xxreq_userid,$xxreq_obo,$xxreq_buyer`

This sends a copy to the originator, on-behalf-of person, and buyer.

---

## Supplier Confirmation

### Can suppliers confirm receipt of POs?

Yes. This requires the iPurchase web server to be accessible from outside your firewall.

**Setting:** `EMAIL_SUPPLIER_CONFIRMATION_LINK`

**Features:**
- Confirmation icons on Requisition Inquiry screen
- Ability to search for confirmed/unconfirmed POs
- Works with auto or manual email options

---

## Blanket POs

### Does iPurchase support blanket POs?

Yes. iPurchase works with QAD blanket POs and releases.

**Key Settings:**

| Setting | Description |
|---------|-------------|
| `EMAIL_SUPPLIER_BLANKET_PO` | Auto-email blanket POs |
| `BLANKET_SEND_PO` | Send original blanket to supplier |
| `ALLOW_BLANKET_RELEASE` | Who can create blanket releases |

**Default:** Only buyers can create QAD blanket releases.

---

## Email Configuration

### How do I configure the email server?

**Setting:** `EMAILSERVER`

For on-premises Exchange, provide server address, username, and password.

---

## Master Comments

### Can I use QAD Master Comments on POs?

Yes. Master comments can be used at header and line level.

**Setting:** `HIDE_MASTER_COMMENTS` - Set to hide specific master comments

**Note:** Master comments can be attached to suppliers and items in QAD.

`MC_BEFORE_NOTES = TRUE` - Print master comments before PO notes

---

## See Also

- [System Settings Reference](../reference/system-settings-reference.md) - All PO_ settings
- [Change Orders FAQ](change-orders.md) - PO modifications

---

*Last Updated: January 2026*
