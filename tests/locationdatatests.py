# Unit test style tests
import unittest
import json
import json_delta
from locationUtils import *
# --- Handlebars tests

# Test that equals helper works properly

class TestLocationDataFunctions(unittest.TestCase):

    def test_setup_data(self):

        name = "lesbos"
        emptyStruct = getEmptyLocationData(name)
        expectedStruct = {g.LOCATION_DETAILS_KEY: {"name": name}, g.SECTIONS_KEY: []}
        self.assertEqual(emptyStruct, expectedStruct);

    # Test that some raw data that we have in an array gets parsed into exactly the JSON we're expecting.
    def test_load_raw_data(self):

        name = "lesbos"
        locationData = getEmptyLocationData(name)

        data = ['MOLYVOS',	'SECTION_TITLE',	'Molyvos: vital arrival info',
        'MOLYVOS',	'CRITICAL',	'X',
        'MOLYVOS',	'PARAGRAPH',	'Welcome to the Greek island of Lesvos. From wherever you land on the island, you will need to travel to the capital, Mytilene. In Mytilene you will be registered as arriving in Greece. You need to be registered to continue your journey on a ferry or plane, take taxis or stay in hotels. You cannot move around Greece legally without completing the registration process.',
        'MOLYVOS',	'PARAGRAPH',	'Near Mytilene there are registration centres where the police will record personal information from you and your family members or those traveling with you. You may be asked for fingerprints as well. This does not prevent your onward journey. Please cooperate with the police if you are requested to provide fingerprints.Once your registration is completed, you will receive a registration document from the police with your information.',
        'MOLYVOS',	'PARAGRAPH',	'This police note is valid for 6 months, but is only valid in Greece. It is recommended that you make a copy of the document in case you lose or damage it. There are photocopiers available for use at the registration centres.',
        'MOLYVOS',	'TITLE',	'Travel from Molyvos to Mytilene:',
        'MOLYVOS',	'LISTITEM',	'The registration centres are between 65-70km from in a city called . It is a 1.5 hour bus journey or approximately 16 - 20 hour walk.',
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

        compileLocationDataToJSON(fakeCellData, locationData)

        with open("tests/expectedData.json", "r") as fp:
            j = json.load(fp)

        #print "Location:\n" + str(locationData) + "\n\n"

        # print "JSON File:\n" + str(j).replace("u\"","\"").replace("u\'","\'") + "\n\n"

        #print json_delta.diff(locationData, j)

        # self.assertEqual(locationData, str(j).replace("u\"","\"").replace("u\'","\'")   )
        self.assertEqual(locationData, j)
        # self.assertTrue(True)



class Test_Cell:
    def __init__(self, value):
        self.value = value