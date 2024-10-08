text_file_path = "D:\\Learn_SDET\\Python\\Codes\\Learn_Python\\ReadAndWriteFromFile\\read_text_file.txt"

with open(text_file_path, "r") as file:
    data = file.readlines()
    for i in data:
        print(i)
