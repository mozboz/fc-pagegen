from fcglobals import globals as g

# locationData is a dict to represent a JSON doc to write data parsed from rawData
def compileLocationDataToJSON(rawData, locationData):

    rowLength = 3
    rows = len(rawData) / rowLength

    d = {}
    # first roll up by sectionId into dict d
    for rowIndex in range(0,rows):
        sectionId = rawData[rowIndex * rowLength + 0].value
        itemType = rawData[rowIndex * rowLength + 1].value
        itemValue = rawData[rowIndex * rowLength + 2].value

        # print sectionId + str(type(sectionId)) + itemType + str(type(itemType)) + itemValue + str(type(itemValue))

        if (sectionId.strip() and itemType.strip() and itemValue.strip()):
            d.setdefault(sectionId, []).append({"type": itemType, "value": itemValue})

    # process items in each section
    for key in d:
        # set defaults
        o = {}
        o[g.SECTION_TITLE_KEY] = key
        o[g.CRITICAL_KEY] = g.HANDLEBARS_FALSE
        o[g.SECTION_ITEMS_KEY] = []

        # Loop through items, if meta item set as property of the object, otherwise just add to list of section items
        for item in d[key]:
            if (item["type"] not in g.ALL_TYPES):
                print "Bad data: Section: " + key + ", itemType: " + item["type"] + ", value: " + item["value"]
            else:
                # print "Adding: Section: " + key + ", itemType: " + item["type"] + ", value: " + item["value"]
                if (item["type"] in g.SECTION_META_INFO):
                    o[item["type"]] = item["value"]
                else:
                    o[g.SECTION_ITEMS_KEY].append(item)

        locationData[g.SECTIONS_KEY].append(o)


def getEmptyLocationData(locationName):

    locationData = {g.LOCATION_DETAILS_KEY: {"name": locationName}, g.SECTIONS_KEY: []}

    return locationData
