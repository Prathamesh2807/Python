import random as r 
freq = int(input("enter the frequency of random no : "))
list = []

for i in range(freq):  # 0 ---> 19
    element = r.randint(1,20)
    list.append(element)

print(list)