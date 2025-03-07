my_str1 = 'abcdef'
my_str2 = 'defghia'

# Output : 4
# (i.e. matching characters :- a, d, e, f)

count = 0

for i in my_str1:
    for j in my_str2:
        if i == j:
            count += 1

print(count)
