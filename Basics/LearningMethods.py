def add_two_numbers(a, b):
    return a + b


print("Sum is --> {}".format(add_two_numbers(2, 3)))


def default_method(name, age, school="ACS"):
    print("Name is    --> {}".format(name))
    print("Age is     --> {}".format(age))
    print("School is  --> {}".format(school))


default_method("kartik", 24)
