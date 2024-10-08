my_list = [1, 1.2, "Name"]
print("List is                            --> {}".format(my_list))
print("Last digit in List is              --> {}".format(my_list[-1]))
print("Reversed List is                   --> {}".format(my_list[::-1]))
print("Value at first index is            --> {}".format(my_list[0]))

print("List length is                     --> {}".format(len(my_list)))

my_list.append("lastname")
print("List after appending is            --> {}".format(my_list))

my_list.insert(1, "True")
print("List after inserting at index 1 is --> {}".format(my_list))

my_list.remove("lastname")
print("List after removing value is       --> {}".format(my_list))

my_num_list = [3, 2, 19, 5, 10]
my_num_list.sort()
print("Sorted List is                     --> {}".format(my_num_list))

my_num_list.reverse()
print("Reverse List is                    --> {}".format(my_num_list))

my_copied_num_list = my_num_list.copy()
print("Copied List is                     --> {}".format(my_copied_num_list))

my_num_list.clear()
print("List after clearing is             --> {}".format(my_num_list))