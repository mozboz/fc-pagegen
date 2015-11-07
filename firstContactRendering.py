import codecs
import os
from pybars import Compiler
from firstContactSheets import loadSectionDataFromSheet
from locationUtils import getEmptyLocationData, compileLocationDataToJSON
from testData import getTestData, Test_Cell

# Get data from spreadsheet, render with a template, and write out to file
# Account from the credentials must have access ot the file
def renderSheet(locationRoot, credentialsFileName, sheetKey, locationName, sheetTab, language):
    locationDataRaw = loadSectionDataFromSheet(sheetKey, sheetTab, "A2:C200", credentialsFileName)

    # locationDataRaw = getTestData()

    locationData = getEmptyLocationData(locationName)

    compileLocationDataToJSON(locationDataRaw, locationData)

    renderedLocation = renderTemplate("templates/index.html", locationData)

    outputFileName = getFileNameAndCreatePath(locationRoot, language, locationName)

    with codecs.open(outputFileName, "w", encoding="utf-8") as f:
        f.write(renderedLocation)


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
