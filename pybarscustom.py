# -*- coding: utf-8 -*-
import codecs
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

# See the template HTML for comments on partials
def _languageRadioPartial():
    return loadFileToUnicodeString('templates/radioPartial.html')

def _locationPartial():
    return loadFileToUnicodeString('templates/locationPartial.html')

def loadFileToUnicodeString(fileName):
    with codecs.open (fileName, "r", "utf-8") as f:
        s=f.read()
    return s


def _getLanguageTitleInNativeLanguage(this, shortCode):

    languageMap = { 'en' : u"English",
                    'gr' : u"ελληνικά",
                    'ar' : u'\u0644\u0639\u064e\u0631\u064e\u0628\u0650\u064a\u0629\u200e\u006d',
                    'fa' : u'\u0627\u0631\u0633\u06cc',
                    'ur' : u'\u0627\u064f\u0631\u062f\u064f\u0648'
                    }

    if (languageMap.has_key(shortCode)):
        return languageMap[shortCode]
    else:
        return "Unknown Language"

