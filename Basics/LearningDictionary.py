my_dict = {
    "name": "Kartik",
    "age": 25,
    "place": "Noida"
}

print("My dictionary is                  --> {}".format(my_dict))
print("Name in dictionary is             --> {}".format(my_dict["name"]))

print("Items in dictionary is            --> {}".format(my_dict.items()))
print("Keys in dictionary is             --> {}".format(my_dict.keys()))
print("Values in dictionary is           --> {}".format(my_dict.values()))

my_nested_dict = [
    {
        "name": "Kartik",
        "age": 25,
        "place": "Noida"
    },
    {
        "name": "Arun",
        "age": 26,
        "place": "Noida"
    }
]


print("My nested dictionary is           --> {}".format(my_nested_dict))
print("Name in nested dictionary is      --> {}".format(my_nested_dict[1]["name"]))

# print("Items in nested dictionary is     --> {}".format(my_nested_dict.)
# print("Keys in nested dictionary is      --> {}".format(my_nested_dict.keys()))
# print("Values in nested dictionary is    --> {}".format(my_nested_dict.values()))
my_blank_dict = {}
my_blank_dict["name"] = "Sammi"
my_blank_dict["age"] = 30
print("My balnk dictionary is            --> {}".format(my_blank_dict))
