
def _equal(this, options, left, right):
    if left == right:
        return options['fn'](this)
    else:
        return ''