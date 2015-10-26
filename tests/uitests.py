# Unit test style tests
from pybars import Compiler
from pybarscustom import _equal
import unittest

# --- Handlebars tests

# Test that equals helper works properly

class TestHandleBarsHelpers(unittest.TestCase):

    def test_equals(self):

        html = u'start {{#equal 1 0}}no{{/equal}} {{#equal 4 4}}yes{{/equal}} end'
        handlebarsTemplate = Compiler().compile(html)

        helpers = {'equal': _equal}

        output = handlebarsTemplate({}, helpers=helpers)

        self.assertEqual(output, 'start  yes end');





