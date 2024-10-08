my_string = "My name in kartik"

print("Value at index 1 is                   --> {}".format(my_string[1]))
print("Value from 1st index to 4th index is  --> {}".format(my_string[1:5]))
print("Reverse string is                     --> {}".format(my_string[::-1]))
print("Is kartik is present in string        --> {}".format("kartik" in my_string))

split_string = my_string.split(" ")
print("Splitting string                      --> {}".format(split_string))
print("Value in 1st index in split string is --> {}".format(split_string[1]))
