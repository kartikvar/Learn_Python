num = 153
len_num = len(str(num))
sum_num = 0

for i in str(num):
    sum_num = sum_num + pow(int(i), len_num)

if num == sum_num:
    print("it is Armstrong Number")
else:
    print("it is not Armstrong Number")
