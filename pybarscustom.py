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