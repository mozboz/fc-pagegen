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
def getActiveLocationsFromMasterSheet(sheetKey, credentialsFileName):

    data = loadRangeFromSheet(sheetKey, "Locations", "A3:D100", credentialsFileName)

    rows = 98
    rowWidth = 4

    # Index in the row of fields we're interested in getting
    nameIndex = 0
    activeIndex = 1
    IDIndex = 3

    activeSheets = {}

    for rowIndex in range(0,rows):
        if (data[rowIndex*rowWidth + activeIndex].value == "Y"):
            activeSheets[data[rowIndex*rowWidth + IDIndex].value ] = data[rowIndex*rowWidth + nameIndex].value

    return activeSheets

