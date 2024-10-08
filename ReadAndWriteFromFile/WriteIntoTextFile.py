read_text_file = "D:\\Learn_SDET\\Python\\Codes\\Learn_Python\\ReadAndWriteFromFile\\read_text_file.txt"
write_text_file = "D:\\Learn_SDET\\Python\\Codes\\Learn_Python\\ReadAndWriteFromFile\\write_text_file.txt"

with open(read_text_file, "r") as reader:
    data = reader.readlines()
    print(data)
    with open(write_text_file, "w") as writer:
        for i in reversed(data):
            writer.write(i+"\n")
