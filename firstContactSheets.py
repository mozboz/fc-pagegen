import json
from oauth2client.client import SignedJwtAssertionCredentials
import gspread

# Load a given range from a Google Sheet
def loadSectionDataFromSheet(sheetKey, sheetTab, cellRange, credentialsFileName):

    jsonKey = json.load(open(credentialsFileName))
    scope = ['https://spreadsheets.google.com/feeds']

    credentials = SignedJwtAssertionCredentials(jsonKey['client_email'], jsonKey['private_key'], scope)

    gc = gspread.authorize(credentials)

    wks = gc.open_by_key(sheetKey).worksheet(sheetTab)

    cellList = wks.range(cellRange)

    return cellList

