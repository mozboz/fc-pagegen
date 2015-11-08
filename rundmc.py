#!/usr/bin/env python
from firstContactRendering import renderSheet

locationRoot = "www/locations"

# This file must be generated. See http://gspread.readthedocs.org/en/latest/oauth2.html
credentialsFileName = 'google-drive-creds.json'

locationName = "Lesbos"
sheetKey = "1HKRD8HnkbLNLRJ6UUwq70xW8kBLyZOUGbVsAh3t4GKE"

writtenSheets = renderSheet(locationRoot, credentialsFileName, sheetKey, locationName)

print writtenSheets