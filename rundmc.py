import json
from oauth2client.client import SignedJwtAssertionCredentials
import gspread
from pybars import Compiler

def main():
    locationData = loadNameValueDataFromSheet("Test HTML Generation", "A2:B14")

    print renderTemplate("templates/testTemplate.html", locationData)

def loadNameValueDataFromSheet(sheetName, cellRange):

    # This file must be generated. See http://gspread.readthedocs.org/en/latest/oauth2.html
    json_key = json.load(open('firstcontacttest-a5b639f44275.json'))
    scope = ['https://spreadsheets.google.com/feeds']

    credentials = SignedJwtAssertionCredentials(json_key['client_email'], json_key['private_key'], scope)

    gc = gspread.authorize(credentials)

    wks = gc.open(sheetName).sheet1

    cell_list = wks.range(cellRange)

    rowLength = 2
    rows = len(cell_list) / rowLength

    locationData = {}

    for rowIndex in range(0,rows):
        print "name: " + cell_list[rowIndex * rowLength + 0].value
        print "value: " + cell_list[rowIndex * rowLength + 1].value
        locationData[cell_list[rowIndex * rowLength + 0].value] = cell_list[rowIndex * rowLength + 1].value

    return locationData

def renderTemplate(templateFileName, nameValueData):
    handlebarsCompiler = Compiler()

    import codecs
    f = codecs.open(templateFileName, encoding='utf-8')
    templateString = f.read()

    handlebarsTemplate = handlebarsCompiler.compile(templateString)

    # remember functionality of helpers and partials
    # see https://github.com/wbond/pybars3
    output = handlebarsTemplate(nameValueData)

    return output

main()