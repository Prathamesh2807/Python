num = int(input("enter the number of which you want to calci factorial : "))

fact = 1 
for i in range(num , 1 , -1):
    fact = fact * i

print(f"factorial of {num} is : " , fact)
