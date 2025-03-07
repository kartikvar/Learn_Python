my_string = "Geeks for Geeks"

my_list = my_string.split(" ")
print(my_list)

new_string = ""
for i in my_list:
    if new_string == "":
        new_string = new_string + i
    else:
        new_string = new_string + "-" + i

print(new_string)