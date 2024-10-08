import json

json_file_path = "D:\\Learn_SDET\\Python\\Codes\\Learn_Python\\ReadWriteToJsonFileAndParsing\\json_file.json"


with open(json_file_path, "r") as reader:
    data = json.load(reader)
    print("Data type after parsing string is --> {}".format(type(data)))

    print("Name in dictionary is             --> {}".format(data["name"]))
    print("Second course in dictionary is    --> {}".format(data["language"][1]))
