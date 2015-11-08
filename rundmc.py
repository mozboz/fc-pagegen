#!/usr/bin/env python
from firstContactRendering import renderSheet
from firstContactSheets import getActiveLocationsFromMasterSheet

locationRoot = "www/locations"

# This file must be generated. See http://gspread.readthedocs.org/en/latest/oauth2.html
credentialsFileName = 'google-drive-creds.json'

masterSheetKeyLive = "1_UrWtrxqGQF4Kd8Q1ZVEPz2F_quyW8YpA4BCrsV0byw"
masterSheetKeyDemo = "1lAUfDjwsoVPajFUInvAY-6uDnfmEuQcXCWNUQzJZPiw"

masterSheetKey = masterSheetKeyDemo

activeLocations = getActiveLocationsFromMasterSheet(masterSheetKey, credentialsFileName)

allStatuses = []
locations = []
languages = []

for id in activeLocations:
    sheetStatuses, renderedLanguages = renderSheet(locationRoot, credentialsFileName, id, activeLocations[id])
    allStatuses.extend(sheetStatuses)
    locations.append(activeLocations[id])
    languages = list(set(languages) | set(renderedLanguages))

print allStatuses
print locations
print languages
