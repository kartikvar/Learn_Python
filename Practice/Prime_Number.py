num = 11
flag = True

for i in range(2, num):
    if num % i == 0:
        flag = False
        break

if flag:
    print("Prime Number")
else:
    print("Not prime number")
