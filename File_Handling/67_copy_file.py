with open("sample.txt" , "r") as file :
    data = file.read()

with open("copy.txt","w") as file:
    file.write(data)