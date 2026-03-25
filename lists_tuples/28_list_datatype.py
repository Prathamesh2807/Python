list1 = []

for i in range(3):
    name = str(input("enter your name : "))
    list1.append(name)

print(type(list1))
print(list1[0])
print(list1)

for i in range(3):
    print(f"the element {i+1} is : ",list1[i])