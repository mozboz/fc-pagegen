import codecs
import os
from pybars import Compiler
import sys
from firstContactSheets import loadRangeFromSheet
from locationUtils import getEmptyLocationDataObject, compileLocationDataToObject

# Get data from spreadsheet, render with a template, and write out to file
# Account from the credentials must have access ot the file
def renderSheet(locationRoot, credentialsFileName, sheetKey, locationName):

    #todo move out to config file
    # tab in the sheet where all data for all languages is compiled to
    allDataTab = "allDataTab"

    range = "B1:I200"
    cols = 8
    rows = 200
    startRow = 1

    sheetStatuses = []
    successfullyRenderedLanguages = []

    try:
        locationDataRaw = loadRangeFromSheet(sheetKey, allDataTab, range, credentialsFileName)

        languages = getLanguages(locationDataRaw, rows, cols)

        # catch errors so we have some chance of completing large batches in case of strange errors
        for languageColumn in languages:
            try:
                language = languages[languageColumn]
                locationData = getEmptyLocationDataObject(locationName)

                #locationData object is updated here with the data from each language
                compileLocationDataToObject(locationDataRaw, locationData, languageColumn, rows, cols, startRow)

                renderedLocation = renderTemplate("templates/index.html", locationData)

                outputFileName = getFileNameAndCreatePath(locationRoot, language, locationName)

                with codecs.open(outputFileName, "w", encoding="utf-8") as f:
                    f.write(renderedLocation)

                sheetStatuses.append({"location" : locationName, "language" : language, "status" : "success"})
                successfullyRenderedLanguages.extend(language)
            except:
                sheetStatuses.append({"location" : locationName, "language" : language, "status" : "error: " + repr(sys.exc_info()[0]) + repr(sys.exc_info()[1])})


    except:
        sheetStatuses.append({"location" : locationName, "status" : "Fail loading sheet: " + repr(sys.exc_info()[0]) + repr(sys.exc_info()[1]) + " key: " + sheetKey})

    return (sheetStatuses, languages.values())

# Get the languages from the first row of a data range
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

    compiler = Compiler()

    with codecs.open(templateFileName, encoding='utf-8') as f:
        templateString = f.read()

    handlebarsTemplate = compiler.compile(templateString)

    # remember functionality of helpers and partials
    # see https://github.com/wbond/pybars3

    from pybarscustom import _equal, _urlify, _languageRadioPartial, _getLanguageTitleInNativeLanguage

    helpers = {'equal': _equal, 'urlify': _urlify, 'getLanguageTitle' : _getLanguageTitleInNativeLanguage}

    languageRadioPartial = compiler.compile(_languageRadioPartial())

    partials = { 'languageRadio' : languageRadioPartial}

    render = handlebarsTemplate(nameValueData, helpers = helpers, partials = partials)

    return render
