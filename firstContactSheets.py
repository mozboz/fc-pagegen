import json
from oauth2client.client import SignedJwtAssertionCredentials
import gspread

# Load a given range from a Google Sheet
def loadRangeFromSheet(sheetKey, sheetTab, cellRange, credentialsFileName):

    jsonKey = json.load(open(credentialsFileName))
    scope = ['https://spreadsheets.google.com/feeds']

    credentials = SignedJwtAssertionCredentials(jsonKey['client_email'], jsonKey['private_key'], scope)

    gc = gspread.authorize(credentials)

    wks = gc.open_by_key(sheetKey).worksheet(sheetTab)

    cellList = wks.range(cellRange)

    return cellList

# parse master sheet to get all active sheet IDs and names
def getMasterSheet(sheetKey, credentialsFileName):

    data = loadRangeFromSheet(sheetKey, "Locations", "A3:D100", credentialsFileName)

    rows = 98
    cols = 4

    nameIndex = 0
    activeIndex = 1
    IDIndex = 3

    activeSheets = {}

    for rowIndex in range(0,rows):
        if (data[rowIndex*cols + activeIndex].value == "Y"):
            activeSheets[data[rowIndex*cols + IDIndex].value ] = data[rowIndex*cols + nameIndex].value

    return activeSheets

