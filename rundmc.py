import json
from oauth2client.client import SignedJwtAssertionCredentials
import gspread
from pybars import Compiler

# This file must be generated. See http://gspread.readthedocs.org/en/latest/oauth2.html
json_key = json.load(open('firstcontacttest-a5b639f44275.json'))
scope = ['https://spreadsheets.google.com/feeds']

credentials = SignedJwtAssertionCredentials(json_key['client_email'], json_key['private_key'], scope)

gc = gspread.authorize(credentials)

wks = gc.open("Test HTML Generation").sheet1

cell_list = wks.range('A1:B4')

# Data acquired from spreadsheet. Render into template here
print cell_list



# Get a compiler
compiler = Compiler()

# Compile the template
source = u"{{>header}}{{#list people}}{{firstName}} {{lastName}}{{/list}}"
template = compiler.compile(source)

# Add any special helpers
def _list(this, options, items):
    result = [u'<ul>']
    for thing in items:
        result.append(u'<li>')
        result.extend(options['fn'](thing))
        result.append(u'</li>')
    result.append(u'</ul>')
    return result
helpers = {'list': _list}

# Add partials
header = compiler.compile(u'<h1>People</h1>')
partials = {'header': header}

# Render the template
output = template({
    'people': [
            {'firstName': "Yehuda", 'lastName': "Katz"},
            {'firstName': "Carl", 'lastName': "Lerche"},
            {'firstName': "Alan", 'lastName': "Johnson"}
    ]}, helpers=helpers, partials=partials)

print(output)

