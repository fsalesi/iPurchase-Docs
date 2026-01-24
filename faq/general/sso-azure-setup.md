# Single Sign-On (SSO) Setup with Azure AD

This guide walks through configuring iPurchase to use Microsoft Azure Active Directory (Entra ID) for Single Sign-On authentication using OAuth2.

---

## Prerequisites

- Access to Azure Portal with permissions to create App Registrations
- iPurchase administrator access to System Settings
- Your iPurchase server's fully qualified domain name (FQDN)

---

## Part 1: Azure Portal Configuration

### Step 1: Create App Registration

1. Log into the [Azure Portal](https://portal.azure.com)
2. Navigate to **Azure Active Directory** → **App registrations**
3. Click **New registration**
4. Enter a name (e.g., "iPurchase SSO")
5. Under **Supported account types**, select:
   - **Accounts in any organizational directory (Any Azure AD directory - Multitenant)**
6. Click **Register**

### Step 2: Note Your IDs

After registration, note these values from the **Overview** page:
- **Application (client) ID** - You'll need this for iPurchase settings
- **Directory (tenant) ID** - You'll need this for the token URL

### Step 3: Configure Authentication

1. Go to **Authentication** in the left menu
2. Under **Platform configurations**, click **Add a platform** → **Web**
3. Add **Redirect URIs** (replace `[FQDN]` with your server's domain):
   ```
   https://[FQDN]/efw50/ifw/iframework.html
   ```
   Add entries for each environment (DEV, TEST, PROD) if they have different URLs.

4. Under **Implicit grant and hybrid flows**, check:
   - ☑️ **Access tokens**
   - ☑️ **ID tokens**

5. Click **Save**

### Step 4: Create Client Secret

1. Go to **Certificates & secrets** in the left menu
2. Click **New client secret**
3. Enter a description (e.g., "iPurchase Production")
4. Select an expiration period
5. Click **Add**
6. **Immediately copy the secret Value** - it will only be shown once!
7. **Set a calendar reminder** to renew before expiration

### Step 5: Configure API Permissions

1. Go to **API permissions** in the left menu
2. Click **Add a permission** → **Microsoft Graph** → **Delegated permissions**
3. Add these permissions:
   - `openid`
   - `profile`
   - `email`
4. Click **Add permissions**
5. If required by your organization, click **Grant admin consent**

### Step 6: Optional - Branding

1. Go to **Branding & properties**
2. Add your company logo
3. Configure display name shown to users during login

---

## Part 2: iPurchase Configuration

Configure these System Settings in iPurchase (Admin → System Settings):

### Required Settings

| Setting | Value | Description |
|---------|-------|-------------|
| `LOGIN_USE_SSO` | `FALSE` | Start with FALSE to allow both login types during testing |
| `SSO_CHOICE` | `Microsoft` | Specifies Microsoft/Azure as the SSO provider |
| `SSO_CLIENT_ID` | `[Application ID]` | From Azure App Registration Overview |
| `SSO_CLIENT_SECRET` | `[Client Secret]` | From Certificates & secrets |
| `SSO_TOKEN_URL` | `https://login.microsoftonline.com/[TenantID]/oauth2/v2.0/token` | Replace `[TenantID]` with your Directory ID |
| `SSO_AUTHORIZATION_URL` | `https://login.microsoftonline.com/common/oauth2/v2.0/authorize` | Standard Microsoft authorization endpoint |

### Microsoft-Specific Settings (if using multiple providers)

| Setting | Value |
|---------|-------|
| `SSO_CLIENT_ID_MICROSOFT` | `[Application ID]` |
| `SSO_CLIENT_SECRET_MICROSOFT` | `[Client Secret]` |
| `SSO_TOKEN_URL_MICROSOFT` | `https://login.microsoftonline.com/[TenantID]/oauth2/v2.0/token` |
| `SSO_AUTHORIZATION_URL_MICROSOFT` | `https://login.microsoftonline.com/common/oauth2/v2.0/authorize` |

---

## Part 3: Testing

### Test with Both Login Methods

1. With `LOGIN_USE_SSO = FALSE`, users see both options:
   - Traditional username/password login
   - "Sign in with Microsoft" button

2. Test SSO login:
   - Click "Sign in with Microsoft"
   - Authenticate with Azure AD credentials
   - Verify you're logged into iPurchase correctly

3. Verify user mapping:
   - SSO matches Azure email to iPurchase user's email address
   - Ensure iPurchase users have correct email addresses in their profiles

### Go Live

Once testing is successful:

1. Set `LOGIN_USE_SSO = TRUE`
2. Users will only see the SSO login option
3. Traditional login is disabled

---

## Troubleshooting

### "User not found" after SSO login
- Verify the user's email in iPurchase matches their Azure AD email exactly
- Check for extra spaces or case sensitivity issues

### "Invalid redirect URI" error
- Verify the redirect URI in Azure matches your iPurchase URL exactly
- Check for http vs https
- Ensure no trailing slashes where not expected

### Token expired errors
- Check if the client secret has expired
- Generate a new secret and update `SSO_CLIENT_SECRET`

### Users can't access after SSO enabled
- Temporarily set `LOGIN_USE_SSO = FALSE` to allow traditional login
- Verify user email mappings
- Check Azure AD group permissions if applicable

---

## Security Best Practices

1. **Rotate secrets regularly** - Set calendar reminders before expiration
2. **Use separate App Registrations** for DEV/TEST/PROD environments
3. **Limit API permissions** to only what's needed (openid, profile, email)
4. **Monitor sign-in logs** in Azure AD for suspicious activity
5. **Require MFA** in Azure AD for additional security

---

## Related Settings

| Setting | Description |
|---------|-------------|
| `PASSWORD_EXPIRE_DAYS` | Not applicable when using SSO |
| `PASSWORD_RULES` | Not applicable when using SSO |
| `NO_PASSWORD_ON_APPROVE` | Still applicable - controls approval re-authentication |

---

## See Also

- [System Settings Reference](../../reference/system-settings-reference.md) - Complete settings catalog
- [Users and Groups](../admin/screens/01-users-and-groups.md) - User email configuration

---

*Last Updated: January 2026*
