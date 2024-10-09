my_list = [14, 5, 19, 3, 6, 92]
my_even_list = []
my_odd_list = []

for i in my_list:
    if i % 2 == 0:
        my_even_list.append(i)
    else:
        my_odd_list.append(i)

print("Even list is --> {}".format(my_even_list))
print("Odd list is  --> {}".format(my_odd_list))
