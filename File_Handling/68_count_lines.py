with open("sample.txt","r") as file:
    content = file.readlines()

line_count = len(content)
print(line_count)
