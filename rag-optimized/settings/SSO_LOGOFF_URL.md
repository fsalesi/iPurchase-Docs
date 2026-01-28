# SSO_LOGOFF_URL

## Description
The logout/sign-out URL for your SSO identity provider.

## Default Value
`(set during configuration)`

## Example Values
- Microsoft/Azure: `https://login.microsoftonline.com/[TENANT_ID]/oauth2/v2.0/logout`
- Google: `https://www.google.com/accounts/Logout`
- Okta: `https://[YOUR_DOMAIN].okta.com/login/signout`

## Category
Security & Authentication

## Notes
Replace `[TENANT_ID]` or `[YOUR_DOMAIN]` with your organization's values.
