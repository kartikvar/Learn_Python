# Required Arguments Method
print("------------------------------ Required Arguments Method ------------------------------")


def required_arguments_method(name):
    print("Hi! {}, How are you?".format(name))


required_arguments_method("Kartik")

# Keywords Arguments
print("------------------------------ Keywords Arguments Method ------------------------------")


def keywords_arguments_method(a, b):
    return a + b


print("Sum is --> {}".format(keywords_arguments_method(b=3, a=2)))

# Default Arguments Method
print("------------------------------ Default Arguments Method ------------------------------")


def default_arguments_method(name, age, school="ACS"):
    print("Name is    --> {}".format(name))
    print("Age is     --> {}".format(age))
    print("School is  --> {}".format(school))


default_arguments_method("kartik", 24)

# Variable Length Arguments
print("------------------------------ Default Arguments Method ------------------------------")


def variable_length_arguments_method(*salary):
    print("Data type of salary is --> {}".format(type(salary)))
    for i in salary:
        print("Salary is --> {}".format(i))


variable_length_arguments_method(100)
variable_length_arguments_method(100, 200)
