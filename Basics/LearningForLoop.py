print("****************** Printing Range ******************")
for i in range(5):
    print(i)

print("****************** Printing Range from to ******************")
for i in range(1, 10, 2):
    print(i)

my_list = ["name", 1, 2.9, False]
print("****************** Printing List ******************")
for i in my_list:
    print(i)

print("****************** Printing Sum ******************")
total = 0
for i in range(1, 5):
    total = total + i
print("Sum is --> {}".format(total))
