# Syncplicity Mass User Offboarding Script
This is a simple Python utility used to automate the offboarding process for users from an Axway Syncplicity account.

## Instructions:
1. Create a developer profile in Syncplicity API (https://developer.syncplicity.com)
2. Create a API application under your developer profile and obtain client ID (clientID) and secret key (secretKey)
3. Log into your production Syncplicity account (https://[tenant].syncplicity.com) and select "Account"
4. Generate an application token that is associated with your user account (must be the same account shared with the API application)
5. Edit `syncp.config` file and set your clientID, secretKey, and appToken
6. Populate `syncp.users.txt` with a list of email addresses to be offboarded
7. Run `python3 syncp-user-offboard.py`

## Note:
The user account associated with the application token must be a company administrator in order to execute the script.
