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

#    locationDataRaw = loadSectionDataFromSheet(sheetTitle, "A2:C100", credentialsFileName)

    locationDataRaw = getTestData()

    locationData = getEmptyLocationData(locationName)

    compileLocationDataToJSON(locationDataRaw, locationData)

    output = renderTemplate("templates/index.html", locationData)

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

    from pybarscustom import _equal, _urlify

    helpers = {'equal': _equal, 'urlify': _urlify}

    output = handlebarsTemplate(nameValueData, helpers=helpers)

    return output

def getTestData():

    data = ['MOLYVOS',	'SECTION_TITLE',	'Molyvos: vital arrival info',
            'MOLYVOS',	'CRITICAL',	'X',
            'MOLYVOS',	'PARAGRAPH',	'Welcome to the Greek island of Lesvos. From wherever you land on the island, you will need to travel to the capital, Mytilene. In Mytilene you will be registered as arriving in Greece. You need to be registered to continue your journey on a ferry or plane, take taxis or stay in hotels. You cannot move around Greece legally without completing the registration process.',
            'MOLYVOS',	'PARAGRAPH',	'Near Mytilene there are registration centres where the police will record personal information from you and your family members or those traveling with you. You may be asked for fingerprints as well. This does not prevent your onward journey. Please cooperate with the police if you are requested to provide fingerprints.Once your registration is completed, you will receive a registration document from the police with your information.',
            'MOLYVOS',	'PARAGRAPH',	'This police note is valid for 6 months, but is only valid in Greece. It is recommended that you make a copy of the document in case you lose or damage it. There are photocopiers available for use at the registration centres.',
            'MOLYVOS',	'TITLE',	'Travel from Molyvos to Mytilene:',
            'MOLYVOS',	'LISTITEM',	u'The registration centres are between 65-70km from in a city called . It is a 1.5 hour bus journey or approximately 16 - 20 hour walk.',
            'MOLYVOS',	'LISTITEM',	'Local organisations, NGOs such as the IRC, MSF, Save the Children, Mercy Corps and the UN are operating free bus services to Mytilene, stopping at the registration centres. Once arriving in Molyvos, you will be directed to a location where you can find the bus service.',
            'MOLYVOS',	'LISTITEM',	'Please be aware that there could be a significant wait for the bus, depending on the number of arrivals and the number of buses. Depending on when you arrive, this may include staying the night at the bus station. We kindly ask for your patience.',
            'MOLYVOS',	'LISTITEM',	'You are permitted to walk to Mytilene. For a reasonably fit person, this trip could take about 2 days. Please be advised that the walk is along a highway with sharp turns and many hills. If you attempt to walk, do not walk in the middle of the road, and watch for cars. ',
            'REGISTRATION',	'SECTION_TITLE',	'Registration',
            'REGISTRATION',	'TITLE',	'How to register',
            'REGISTRATION',	'LISTITEM',	'Nationals from can be registered in. Any personal identification documents available need to be presented at the point of registration. The registration process includes review of identification documentation, questions, fingerprinting and photo. Upon completion a police note is provided which allows those individuals listed to stay in Greece for maximum of 6 months before requiring renewal. Each adult registers separately and any children below the age of 18 are registered on their parents police note.',
            'REGISTRATION',	'LISTITEM',	'Nationalities not listed above, must be registered in Moria, with or without a passport, and successful registration results in receipt of a police note that allows them to stay in Greece for a maximum of one month. This registration can be renewed at one month.',
            'REGISTRATION',	'LISTITEM',	'All nationalities must be registered prior to applying for asylum in Greece.',
            'REGISTRATION',	'LISTITEM',	'In Moria there is an office for asylum requests that is open Monday through Friday 9:00 am-3:00 pm. Processing of asylum requests can take approximately 1.5 - 3 months. If asylum is granted, refugees will receive travel documents which permits travel abroad or residence in Greece for up to 3 years. For more information please contact: 22510 32323 (Languages available English-Greek)',
            'REGISTRATION',	'TITLE',	'Registration point locations']

    fakeCellData = [ Test_Cell(x) for x in data ]

    return fakeCellData

class Test_Cell:
    def __init__(self, value):
        self.value = value

main()