#!/usr/bin/env python

"""
Instructions:
1. Create developer profile in Syncplicity API (https://developer.syncplicity.com)
2. Create API application and obtain client ID (clientID) and secret key (secretKey)
3. Log into production Syncplicity (https://[tenant].syncplicity.com) and select "Account"
4. Generate application token for your user account
5. Edit "syncp.config" file and set your clientID, secretKey, and appToken
6. Populate "syncp.users.txt" with a list of email addresses to be offboarded
7. Run "syncp-user-offboard.py"
"""

# Libraries
import requests, json, csv, urllib.parse

# Meta
__author__      = "Nick McLarty"
__copyright__   = "2021 The Texas A&M University System"
__version__     = "1.0.0"
__email__       = "nmclarty@tamus.edu"
__status__      = "Prod"

# Constants
apiBaseUri      = "https://api.syncplicity.com"
oauthUri        = "oauth/token"
userUri         = "provisioning/user.svc"

# Read config file
with open('syncp.config', 'r') as config_file:
    config_data = config_file.read()
config = json.loads(config_data)

# Authenticate to Syncplicity API
headers = {
    "Sync-App-Token": config['appToken']
}
data = {
    "grant_type": "client_credentials"
}
url = "{}/{}".format(apiBaseUri, oauthUri)

r = requests.post(url,
    auth=(config['clientID'], config['secretKey']),
    headers=headers,
    data=data)

bearerToken = r.json()['access_token']

# Process Users File
headers = {
    "Authorization": "Bearer {}".format(bearerToken)
}

with open('syncp.users.txt', 'r') as users_file:
    csv_reader = csv.reader(users_file, delimiter=',')
    for row in csv_reader:
        email = row[0]
        url = "{}/{}/{}".format(apiBaseUri, userUri, urllib.parse.quote(email))
        r = requests.delete(url, headers=headers)
        print("Request: {} --- Result: {}".format(url, r.status_code))
