# SSO_REAUTH_PARAMS

## Description
Additional OAuth2 parameters to force re-authentication.

## Default Value
`&max_age=0`

## Category
Security & Authentication

## Notes
Used to force users to re-authenticate with their identity provider. Common values:
- `&max_age=0` - Always prompt for credentials
- `&prompt=login` - Force login prompt (provider-specific)
