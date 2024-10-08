my_tuple = (1, 1.2, "Name")
print("Tuple is                            --> {}".format(my_tuple))
print("Last digit in Tuple is              --> {}".format(my_tuple[-1]))
print("Reversed Tuple is                   --> {}".format(my_tuple[::-1]))
print("Value at first index is            --> {}".format(my_tuple[0]))

print("Tuple length is                     --> {}".format(len(my_tuple)))

my_num_tuple = [3, 2, 19, 5, 10]
my_num_tuple.sort()
print("Sorted Tuple is                     --> {}".format(my_num_tuple))

my_num_tuple.reverse()
print("Reverse Tuple is                    --> {}".format(my_num_tuple))

my_copied_num_tuple = my_num_tuple.copy()
print("Copied Tuple is                     --> {}".format(my_copied_num_tuple))

my_num_tuple.clear()
print("Tuple after clearing is             --> {}".format(my_num_tuple))
