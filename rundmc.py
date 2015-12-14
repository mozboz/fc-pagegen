#!/usr/bin/env python
import codecs
from firstContactRendering import renderSheet, renderTemplate
from firstContactSheets import getActiveLocationsFromMasterSheet

webRoot = "www"
locationRoot = webRoot + "/locations"
indexPageFileName = webRoot + "/index.html"

# This file must be generated. See http://gspread.readthedocs.org/en/latest/oauth2.html
credentialsFileName = 'google-drive-creds.json'

masterSheetKeyLive = "1_UrWtrxqGQF4Kd8Q1ZVEPz2F_quyW8YpA4BCrsV0byw"
masterSheetKeyDemo = "1lAUfDjwsoVPajFUInvAY-6uDnfmEuQcXCWNUQzJZPiw"

masterSheetKey = masterSheetKeyLive

# Where information is contained in the master sheet.
masterSheetConfiguration = {"range": "B3:E100", "rowCount" : 98, "rowWidth": 4, "nameColumn" : 0, "isActiveColumn" : 1, "sheetIDColumn" : 3}

activeLocations = getActiveLocationsFromMasterSheet(masterSheetKey, credentialsFileName, masterSheetConfiguration)

print activeLocations

allStatuses = []
locations = []
languages = []

# Render all locations, each location having one or more languages.
for id in activeLocations:
    locationName = activeLocations[id]
    sheetStatuses, renderedLanguages = renderSheet(locationRoot, credentialsFileName, id, locationName)
    allStatuses.extend(sheetStatuses)
    if (len(renderedLanguages) > 0):
        locations.append(activeLocations[id])
        # add only new languages through a set union
        languages = list(set(languages) | set(renderedLanguages))

print allStatuses
print locations
print languages

# Render the home page with menu for each language and location
mainPageHtml = renderTemplate("templates/landing_page.html",
    {"languageShortCodes" : languages ,"locations" : locations }
)

with codecs.open(indexPageFileName, "w", encoding="utf-8") as f:
    f.write(mainPageHtml)
