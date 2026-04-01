num = int(input("enter the no of entries in list : "))

bill = []

for i in range(num):
    amt = int(input("enter the amount : "))
    bill.append(amt)

bill.sort()
print(bill)
print("the second largest amouutn is : " , bill[num-2])


