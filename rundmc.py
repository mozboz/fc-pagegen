#!/usr/bin/env python
import codecs
import json
from oauth2client.client import SignedJwtAssertionCredentials
import gspread
from pybars import Compiler

# Get data from spreadsheet, render with a template, and write out to file
def main():

    credentialsFileName = 'firstcontacttest-a5b639f44275.json'
    sheetTitle = "Test HTML Generation"
    locationData = loadNameValueDataFromSheet(sheetTitle, "A2:B14", credentialsFileName)

    output = renderTemplate("templates/testTemplate.html", locationData)

    outputFileName = "lesbos.html"

    # print output

    with codecs.open(outputFileName, "w", encoding="utf-8") as f:
        f.write(output)


# Load a given two column range from a spreadsheet into a dictionary
def loadNameValueDataFromSheet(sheetName, cellRange, credentialsFileName):

    # This file must be generated. See http://gspread.readthedocs.org/en/latest/oauth2.html
    json_key = json.load(open(credentialsFileName))
    scope = ['https://spreadsheets.google.com/feeds']

    credentials = SignedJwtAssertionCredentials(json_key['client_email'], json_key['private_key'], scope)

    gc = gspread.authorize(credentials)

    wks = gc.open(sheetName).sheet1

    cell_list = wks.range(cellRange)

    rowLength = 2
    rows = len(cell_list) / rowLength

    locationData = {}

    for rowIndex in range(0,rows):
        #print "name: " + cell_list[rowIndex * rowLength + 0].value
        #print "value: " + cell_list[rowIndex * rowLength + 1].value
        locationData[cell_list[rowIndex * rowLength + 0].value] = cell_list[rowIndex * rowLength + 1].value

    return locationData

# Render a given dataset into a handlebars template from a file
def renderTemplate(templateFileName, nameValueData):
    handlebarsCompiler = Compiler()

    f = codecs.open(templateFileName, encoding='utf-8')
    templateString = f.read()

    handlebarsTemplate = handlebarsCompiler.compile(templateString)

    # remember functionality of helpers and partials
    # see https://github.com/wbond/pybars3
    output = handlebarsTemplate(nameValueData)

    return output

main()