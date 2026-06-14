text = input("enter the text : ")

with open("sample.txt","a") as file:
    file.write("\n"+text)