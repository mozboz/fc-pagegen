import json
from oauth2client.client import SignedJwtAssertionCredentials
import gspread

# This file must be generated. See http://gspread.readthedocs.org/en/latest/oauth2.html
json_key = json.load(open('firstcontacttest-a5b639f44275.json'))
scope = ['https://spreadsheets.google.com/feeds']

credentials = SignedJwtAssertionCredentials(json_key['client_email'], json_key['private_key'], scope)

gc = gspread.authorize(credentials)

wks = gc.open("Test HTML Generation").sheet1

cell_list = wks.range('A1:B4')

# Data acquired from spreadsheet. Render into template here
print cell_list

