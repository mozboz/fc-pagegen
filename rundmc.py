#!/usr/bin/env python
import codecs
import json
from oauth2client.client import SignedJwtAssertionCredentials
import gspread
from locationUtils import getEmptyLocationData, compileLocationDataToJSON
from pybars import Compiler

# Get data from spreadsheet, render with a template, and write out to file
def main():

    # This file must be generated. See http://gspread.readthedocs.org/en/latest/oauth2.html
    credentialsFileName = 'firstcontacttest-a5b639f44275.json'

    # An email address of a Google account will be generated in the above process, give that account
    # edit access to a Google Sheet with this name:
    sheetTitle = "Test HTML Generation"

    locationName = "Lesbos"

    locationDataRaw = loadSectionDataFromSheet(sheetTitle, "A2:C100", credentialsFileName)

    locationData = getEmptyLocationData(locationName)

    compileLocationDataToJSON(locationDataRaw, locationData)

    output = renderTemplate("templates/testTemplate.html", locationData)

    outputFileName = "lesbos.html"

    # print output

    with codecs.open(outputFileName, "w", encoding="utf-8") as f:
        f.write(output)


# Load a given two column range from a spreadsheet into a dictionary
def loadSectionDataFromSheet(locationData, sheetName, cellRange, credentialsFileName):

    json_key = json.load(open(credentialsFileName))
    scope = ['https://spreadsheets.google.com/feeds']

    credentials = SignedJwtAssertionCredentials(json_key['client_email'], json_key['private_key'], scope)

    gc = gspread.authorize(credentials)

    wks = gc.open(sheetName).sheet1

    cell_list = wks.range(cellRange)

    return cell_list

# Render a given dataset into a handlebars template from a file
def renderTemplate(templateFileName, nameValueData):

    f = codecs.open(templateFileName, encoding='utf-8')
    templateString = f.read()

    handlebarsTemplate = Compiler().compile(templateString)

    # remember functionality of helpers and partials
    # see https://github.com/wbond/pybars3

    from pybarscustom import _equal

    helpers = {'equal': _equal}

    output = handlebarsTemplate(nameValueData, helpers=helpers)

    return output



main()