# SSO_AUTHORIZATION_URL

## Description
The OAuth2 authorization endpoint URL for your SSO identity provider.

## Default Value
`(set during configuration)`

## Example Values
- Microsoft/Azure: `https://login.microsoftonline.com/common/oauth2/v2.0/authorize`
- Google: `https://accounts.google.com/o/oauth2/auth`
- Okta: `https://[YOUR_DOMAIN].okta.com/oauth2/default/v1/authorize`

## Category
Security & Authentication

## Notes
For Microsoft, use `common` for multi-tenant or your specific tenant ID for single-tenant.
