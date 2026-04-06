n = int(input("enter no of entries in list : "))
list = []

for i in range(n):
    num = int(input("enter the numbers : "))
    list.append(num)

even_list = []
odd_list = []

list.sort()

for i in range(n):
    if (list[i] % 2 == 0 ) :
        even_list.append(list[i])
    else :
        odd_list.append(list[i])

print(even_list)
print(odd_list)

