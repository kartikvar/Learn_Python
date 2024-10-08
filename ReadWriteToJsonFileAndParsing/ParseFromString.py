import json

courses = '{ "name": "rahulshetty", "language": ["Java", "Python"]}'

my_dict = json.loads(courses)
print("Data type after parsing string is --> {}".format(type(my_dict)))

print("Name in dictionary is             --> {}".format(my_dict["name"]))
print("Second course in dictionary is    --> {}".format(my_dict["language"][1]))
# for i in my_dict.items:
#     print("Items in dictionary are --> {}".format(i))
