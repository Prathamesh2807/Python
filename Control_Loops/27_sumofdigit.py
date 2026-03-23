num = int(input("enter the digit : "))
sum = 0 
while (num>0):
    sum = sum + num%10
    num = num // 10

print("the sum of digits is : " , sum)