length = 10
a = 0
b = 1
print(a, end=" ")
print(b, end=" ")
my_list = []

for i in range(2, length):
    c = a + b
    a = b
    b = c
    print(c, end=" ")