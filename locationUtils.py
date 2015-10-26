
# rawData is the input, locationData is a dict which is modified to include data parsed from rawData
def compileLocationDataToJSON(rawData, locationData):

    rowLength = 3
    rows = len(rawData) / rowLength

    for rowIndex in range(0,rows):
        sectionId = rawData[rowIndex * rowLength + 0].value
        itemType = rawData[rowIndex * rowLength + 1].value
        itemValue = rawData[rowIndex * rowLength + 2].value

        locationData['sections'].setdefault(sectionId, []).append({"type": itemType, "value": itemValue})

    return locationData

def getEmptyLocationData(locationName):

    locationData = {"location-details": {"name": locationName}, "sections": {}}

    return locationData

