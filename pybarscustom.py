import re

# handlebars block helper for equality of two items
def _equal(this, options, left, right):
    if left == right:
        return options['fn'](this)
    else:
        return ''

# make string safe for use as url or anchor, etc.
def _urlify(this, urlifyme):

    # Remove all non-word characters (everything except numbers and letters)
    s = re.sub(r"[^\w\s-]", '', urlifyme)

    # Replace all runs of whitespace with a single dash
    s = re.sub(r"\s+", '-', s)

    return s.lower()

# This is the HTML template for rendering the language controls
# {{langShortCode}} will get substituted with e.g. 'en'
# {{langChecked}} will get subsctituted with 'checked' if we want this option to be default
# ((langLabel}} will get substituted with the name of the language in that language. See languageMap function below
# for those strings
def _languageRadioPartial():

    return '''  <li class="radio-group__item">
        <input id="{{langShortCode}}" class="toggle" type="radio" name="lang" value="{{langShortCode}}" {{langChecked}}>
        <label for="{{langShortCode}}" class="btn btn--hollow">{{langLabel}}</label>
    </li>'''


def getLanguageTitleInNativeLanguage(shortCode):

    languageMap = { 'en' : 'English',
                    'gr' : 'ελληνικά',
                    'ar' : '\u0644\u0639\u064e\u0631\u064e\u0628\u0650\u064a\u0629\u200e\u006d',
                    'fa' : '\u0627\u0631\u0633\u06cc',
                    'ur' : '\u0627\u064f\u0631\u062f\u064f\u0648'
                    }

    if (languageMap.has_key(shortCode)):
        return languageMap[shortCode]
    else:
        return "Unknown Language"

