my_list = [10, 20, 30, 20, 20, 30, 40, 50, -20, 60, 60, -20, -20]
unique_list = []
duplicate_list = []

for i in my_list:
    if i not in unique_list:
        unique_list.append(i)
    elif i not in duplicate_list:
        duplicate_list.append(i)

print(duplicate_list)
