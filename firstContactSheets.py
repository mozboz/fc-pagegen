import json
from oauth2client.client import SignedJwtAssertionCredentials
import gspread

# Load a given range from a Google Sheet
# returns data in a one dimensional list
def loadRangeFromSheet(sheetKey, sheetTab, cellRange, credentialsFileName):

    jsonKey = json.load(open(credentialsFileName))
    scope = ['https://spreadsheets.google.com/feeds']

    credentials = SignedJwtAssertionCredentials(jsonKey['client_email'], jsonKey['private_key'], scope)

    gc = gspread.authorize(credentials)

    wks = gc.open_by_key(sheetKey).worksheet(sheetTab)

    cellList = wks.range(cellRange)

    return cellList

# Parse master sheet to get all active sheet IDs (dict key) and names (dict value)
def getActiveLocationsFromMasterSheet(sheetKey, credentialsFileName, masterSheetConfiguration):

    data = loadRangeFromSheet(sheetKey, "Locations", masterSheetConfiguration['range'], credentialsFileName)

    activeSheets = {}

    rowCount = masterSheetConfiguration['rowCount']
    rowWidth = masterSheetConfiguration['rowWidth']

    for rowIndex in range(0,rowCount):
        if (data[rowIndex*rowWidth + masterSheetConfiguration['isActiveColumn']].value == "Y"):
            activeSheets[
                data[rowIndex*rowWidth + masterSheetConfiguration['sheetIDColumn']].value
            ] =\
                data[rowIndex*rowWidth + masterSheetConfiguration['nameColumn']].value

    return activeSheets

