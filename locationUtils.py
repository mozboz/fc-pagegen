from fcglobals import globals as g

# locationData is a dict to represent a JSON doc to write data parsed from rawData
def compileLocationDataToObject(rawData, locationData, valueColumn, rows, columns, startRow):

    d = {}
    # first roll up by sectionId into dict d
    for rowIndex in range(1,rows):
        sectionId = rawData[rowIndex * columns + 0].value
        itemType = rawData[rowIndex * columns + 1].value
        itemValue = rawData[rowIndex * columns + valueColumn].value

        # print sectionId + str(type(sectionId)) + itemType + str(type(itemType)) + itemValue + str(type(itemValue))

        if (sectionId.strip() and itemType.strip() and itemValue.strip()):
            d.setdefault(sectionId, []).append({"type": itemType, "value": itemValue})

    # process items in each section
    for key in d:
        # set defaults
        newSection = {}
        newSection[g.SECTION_TITLE_KEY] = key
        newSection[g.CRITICAL_KEY] = g.HANDLEBARS_FALSE
        newSection[g.SECTION_ITEMS_KEY] = []

        # Loop through items, if meta item set as property of the object, otherwise just add to list of section items
        for item in d[key]:
            if (item["type"] not in g.ALL_TYPES):
                print "Bad data: Section: " + key + ", itemType: " + item["type"] + ", value: " + item["value"]
            else:
                # print "Adding: Section: " + key + ", itemType: " + item["type"] + ", value: " + item["value"]
                if (item["type"] in g.SECTION_META_INFO):
                    newSection[item["type"]] = item["value"]
                else:
                    newSection[g.SECTION_ITEMS_KEY].append(item)

        locationData[g.SECTIONS_KEY].append(newSection)


def getEmptyLocationDataObject(locationName):

    locationData = {g.LOCATION_DETAILS_KEY: {"name": locationName}, g.SECTIONS_KEY: []}

    return locationData
