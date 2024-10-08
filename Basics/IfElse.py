expected_title = "My_Title"

if expected_title == "My_Title":
    print("Test Case Passed")
else:
    print("Test Case Failed")

num_to_test = int(input("Enter the number --> "))
if num_to_test < 10:
    print("Small Number")
elif 10 <= num_to_test < 20:
    print("Medium Number")
else:
    print("Large Number")
