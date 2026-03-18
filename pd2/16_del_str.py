name = str(input("enter any string you like : "))
length = len(name)
print("the lenght of your string is : " , length)

NAME = ""
for i in range (0,length):
    if i % 3 != 0 :
        NAME = NAME + name[i]

print(NAME)