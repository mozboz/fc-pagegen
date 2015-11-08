from tests.uitests import TestHandleBarsHelpers
from tests.locationdatatests import TestLocationDataFunctions
from firstContactRendering import renderSheet, renderTemplate
from firstContactSheets import getMasterSheet
import unittest

# unittest.main()

print renderTemplate("templates/test_template.html", {'languageShortCode': 'en'})
