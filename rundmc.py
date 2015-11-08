#!/usr/bin/env python
from firstContactRendering import renderSheet
from firstContactSheets import getMasterSheet

locationRoot = "www/locations"

# This file must be generated. See http://gspread.readthedocs.org/en/latest/oauth2.html
credentialsFileName = 'google-drive-creds.json'

masterSheetKeyLive = "1_UrWtrxqGQF4Kd8Q1ZVEPz2F_quyW8YpA4BCrsV0byw"
masterSheetKeyDemo = "1lAUfDjwsoVPajFUInvAY-6uDnfmEuQcXCWNUQzJZPiw"

masterSheetKey = masterSheetKeyDemo

activeSheets = getMasterSheet(masterSheetKey, credentialsFileName)

allStatuses = []

for id in activeSheets:
    sheetStatuses = renderSheet(locationRoot, credentialsFileName, id, activeSheets[id])
    allStatuses.extend(sheetStatuses)

print allStatuses
