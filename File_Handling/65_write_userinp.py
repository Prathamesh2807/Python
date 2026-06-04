user_txt = input("enter the text : ")

with open("user_output.txt" , "w") as file:
    file.write(user_txt)