from tests.uitests import TestHandleBarsHelpers
from tests.locationdatatests import TestLocationDataFunctions
from firstContactRendering import renderSheet, renderTemplate
from firstContactSheets import getActiveLocationsFromMasterSheet
import unittest

# unittest.main()

# test handlebars partial and helpers for home page
print renderTemplate("templates/landing_page.html", {'languageShortCode': ['en'], "locations" : ["Lesbos", "Notara 26"]})

# test rendering home page with test data
#print renderTemplate("templates/landing_page.html",
#        {'languageShortCodes' : [{'language'}]}
#)
