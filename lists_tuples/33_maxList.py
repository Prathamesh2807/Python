n = int(input("enter the number of ele in list u want : "))

var = []
for i in range(n):
    item = int(input("enter the amount : "))
    var.append(item)

max = var[0]
for i in range(n):
    if (var[i] > max): max = var[i]

print(f"the max in list is : " , max)

