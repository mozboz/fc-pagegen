import codecs
import os
from pybars import Compiler
from firstContactSheets import loadSectionDataFromSheet
from locationUtils import getEmptyLocationDataObject, compileLocationDataToObject
from testData import getTestData, Test_Cell

# Get data from spreadsheet, render with a template, and write out to file
# Account from the credentials must have access ot the file
def renderSheet(locationRoot, credentialsFileName, sheetKey, locationName):

    #todo move out to config file
    allDataTab = "allDataTab"

    range = "B1:I200"
    cols = 8
    rows = 200
    startRow = 1

    locationDataRaw = loadSectionDataFromSheet(sheetKey, allDataTab, range, credentialsFileName)

    languages = getLanguages(locationDataRaw, rows, cols)

    writtenSheets = []

    for languageColumn in languages:
        locationData = getEmptyLocationDataObject(locationName)

        compileLocationDataToObject(locationDataRaw, locationData, languageColumn, rows, cols, startRow)

        renderedLocation = renderTemplate("templates/index.html", locationData)

        outputFileName = getFileNameAndCreatePath(locationRoot, languages[languageColumn], locationName)

        with codecs.open(outputFileName, "w", encoding="utf-8") as f:
            f.write(renderedLocation)

        writtenSheets.append({"location" : locationName, "language" : languages[languageColumn]})

    return writtenSheets

def getLanguages(locationDataRaw, rows, cols):
    languages = {}
    for colIndex in range(0,cols):
        if (locationDataRaw[colIndex].value.strip()):
            languages[colIndex] = locationDataRaw[colIndex].value

    return languages

# Given the webroot, a language and a location name, check the directory for language exists, and return
# full path for a file in the format:
#      {webRoot}/{language}/{location}.html
def getFileNameAndCreatePath(webRoot, language, location):
    dir = webRoot + '/' + language
    if (not os.path.isdir(dir)):
        os.mkdir(dir, 0775)

    return dir + '/' + location.lower() + '.html'

# Render a given dataset into a handlebars template from a file
def renderTemplate(templateFileName, nameValueData):

    with codecs.open(templateFileName, encoding='utf-8') as f:
        templateString = f.read()

    handlebarsTemplate = Compiler().compile(templateString)

    # remember functionality of helpers and partials
    # see https://github.com/wbond/pybars3

    from pybarscustom import _equal, _urlify

    helpers = {'equal': _equal, 'urlify': _urlify}

    render = handlebarsTemplate(nameValueData, helpers=helpers)

    return render
