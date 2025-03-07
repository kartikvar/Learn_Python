# find second largest number --> my_list = [2, 5, 10, 9, 3, 1, 20, 72, 6]
# interchange first and last digit
# print duplicate number from --> my_list = [10, 20, 30, 20, 20, 30, 40, 50, -20, 60, 60, -20, -20]
# 4 pyramid patterns
# remove duplicate from string --> my_string = "geeksforgeeks". Output is geksfor


for i in range(5, 0, -1):
    for j in range(1, 6):
        if j < i:
            print(" ", end=" ")
        else:
            print("*", end=" ")
    print()
