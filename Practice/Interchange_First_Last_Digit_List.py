my_list = [1, 4, 2, 6]

print("List before interchange --> {}".format(my_list))

my_list[0], my_list[-1] = my_list[-1], my_list[0]

print("List after interchange --> {}".format(my_list))
