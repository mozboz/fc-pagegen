#!/usr/bin/env python
from firstContactRendering import renderSheet
from firstContactSheets import getMasterSheet

locationRoot = "www/locations"

# This file must be generated. See http://gspread.readthedocs.org/en/latest/oauth2.html
credentialsFileName = 'google-drive-creds.json'


locationName = "Lesbos"
sheetKey = "1HKRD8HnkbLNLRJ6UUwq70xW8kBLyZOUGbVsAh3t4GKE"

masterSheetKey = "1_UrWtrxqGQF4Kd8Q1ZVEPz2F_quyW8YpA4BCrsV0byw"

# writtenSheets = renderSheet(locationRoot, credentialsFileName, sheetKey, locationName)

# print writtenSheets

activeSheets = getMasterSheet(masterSheetKey, credentialsFileName)

allWrittenSheets = {}

for id in activeSheets:
    writtenSheets = renderSheet(locationRoot, credentialsFileName, id, activeSheets[id])
    allWrittenSheets.update(writtenSheets)
