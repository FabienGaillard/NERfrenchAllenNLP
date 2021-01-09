import numpy as np

"""
    List of all the labels we previously created
"""

labels = [
    "I-LOC",  # location
    "I-PER",  # Person
    "I-ORG",  # organisation
    "I-DAT",  # date
    "I-ART",  # article number
    "I-CMP",  # account number
    "I-DMD",  # application number
    "I-SAI",  # dimensions
    "I-LRG",  # dimensions
    "I-SUP",  # dimensions
]

#############
#   UTILS   #
#############

"""
    Purpose : checks if a string represents an int
    input : string to be tested
    output : True if string does represent an integer else False
"""


def isInt(s):
    try:
        int(s)
        return True
    except ValueError:
        return False


# Same thing for floats


def isfloat(value):
    try:
        float(value)
        return True
    except ValueError:
        return False


#############
# FUNCTIONS #
#############

"""
    purpose : adding named entities to a dict
    input : named entity, 
            named entity predicted label (to know to which array in the dict we're appending it to), 
            the dictionary we're adding it to
    output : none
"""


def add_entity(entity, label, data):
    if label == "I-LOC":
        data["location"].append(entity)
    if label == "I-PER":
        data["person"].append(entity)
    if label == "I-ORG":
        data["organisation"].append(entity)
    if label == "I-DAT":
        data["date"].append(entity)
    if label == "I-ART":
        data["article"].append(entity)
    if label == "I-CMP":
        data["account"].append(entity)
    if label == "I-DMD":
        data["application"].append(entity)
    if label == "I-SAI":
        data["height"].append(entity)
    if label == "I-LRG":
        data["width"].append(entity)
    if label == "I-SUP":
        data["surface"].append(entity)


"""
    purpose : get the right entity out of the all the possible entities recognized, return the one that appears the most
    input : array of entity
    output : correct entity
"""


def get_location(data):
    entity_array = data["location"]
    most_times_equals = 0
    entity = ""
    indexes_to_delete = []
    # simple double loop to find the max occurences
    for i in range(0, len(entity_array)):
        nbr_times_equal = 0
        for j in range(0, len(entity_array)):
            # if they're both the same entities (likely when looking for the adress, we might scrape the relevent one a few times)
            if entity_array[i].lower() == entity_array[j].lower() and i != j:
                nbr_times_equal = nbr_times_equal + 1
                if nbr_times_equal > most_times_equals:
                    most_times_equals = nbr_times_equal
                    entity = entity_array[i]
    return entity


def get_application(data):
    entity_array = data["application"]
    for i in range(0, len(entity_array)):
        try:
            first, last = entity_array[i].split("/")
            print("First : " + first + "   last : " + last)
        except ValueError:
            err = 0
        else:
            if isInt(first) and isInt(last):
                return entity_array[i]
    return "NA"


def get_height(data):
    entity_array = data["height"]
    for i in range(0, len(entity_array)):
        try:
            height = entity_array[i].split(" ")
        except ValueError:
            err = 0
        else:
            for j in range(0, len(height)):
                try:
                    first, last = height[j].split(",")
                except ValueError:
                    err = 0
                else:
                    if isInt(first) and isInt(last):
                        return height[j]
    return "NA"


def get_width(data):
    entity_array = data["width"]
    for i in range(0, len(entity_array)):
        try:
            width = entity_array[i].split(" ")
        except ValueError:
            err = 0
        else:
            for j in range(0, len(width)):
                try:
                    first, last = width[j].split(",")
                except ValueError:
                    err = 0
                else:
                    if isInt(first) and isInt(last):
                        return width[j]
    return "NA"


def get_surface(data):
    entity_array = data["surface"]
    for i in range(0, len(entity_array)):
        try:
            surface = entity_array[i].split(" ")
        except ValueError:
            err = 0
        else:
            for j in range(0, len(surface)):
                if surface[j].strip() == "m\u00b2":
                    if isInt(surface[j - 1]):
                        return surface[j - 1]
    return "NA"


def get_date(data):
    entity_array = data["date"]
    for i in range(0, len(entity_array)):
        try:
            day, month, year = entity_array[i].split("/")
        except ValueError:
            err = 0
        else:
            if isInt(day) and isInt(month) and isInt(year):
                date = day + "/" + month + "/" + year
                return date
    return "NA"
