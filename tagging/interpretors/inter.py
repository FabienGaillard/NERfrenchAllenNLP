import json
import labels as lbl  # contains redundant
import difflib  # debugging
import numpy as np

"""
    the purpose of this function is to read a prediction output, collect the dected NE and output them in a json 
    input : predictions with [TOKEN LABEL]
    output : json file
"""
data = {
    "location": [],
    "person": [],
    "organisation": [],
    "date": [],
    "article": [],
    "account": [],
    "application": [],
    "height": [],
    "width": [],
    "surface": [],
}


def reader(filename):
    f = open(filename, "r")  # reading the predictions
    i = 0
    lines = f.readlines()
    while i < len(lines):  # read all the lines
        line = lines[i].split(
            " "
        )  # splitting by space since we have predictions with the TOKEN[SPACE]LABEL shape
        temp = ""
        if (
            line[1].strip() in lbl.labels
        ):  # if the predicted LABEL is a label and not just an O, we (in theory) are reading a named entity
            current_label = line[1].strip()
            while True:
                temp = temp + line[0] + " "
                if i + 1 > len(lines):  # if we're not out of bounds
                    break
                else:
                    i = i + 1  # moving on to the next word
                line = lines[i].split(" ")
                if (
                    line[1].strip() != current_label
                ):  # if we're outside of the label, we break out of the loop because the entity is most likely ended (unless there is an NER problem)
                    break
            lbl.add_entity(temp, current_label, data)
        i = i + 1


reader("predictions.txt")
print(json.dumps(data, indent=4))
# print(data["location"][5].lower() == data["location"][7].lower())
# print(lbl.get_location(data))
# print(lbl.get_application(data))
# print(lbl.get_width(data))
# print(lbl.get_surface(data))
print(lbl.get_date(data))