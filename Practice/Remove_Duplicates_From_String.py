my_string = "geeksforgeeks"
# Output : geksfor
no_use_string = ""
output_string = ""

for i in my_string:
    if i not in no_use_string:
        no_use_string = no_use_string + i

print(no_use_string)
