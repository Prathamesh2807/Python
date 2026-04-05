num = int(input("enter the number : "))
rev = 0
while (num > 0):
    d = num % 10 #last digit
    rev = rev * 10 + d
    num = num // 10

print("reverse no of is : " , rev)