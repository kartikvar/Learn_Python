my_list = [2, 5, 10, 9, 3, 1, 20, 72, 6]
second_lar_num = 0

for i in my_list:
    if i is not max(my_list):
        if i > second_lar_num:
            second_lar_num = i
    else:
        continue

print("Second large number is --> {}".format(second_lar_num))
