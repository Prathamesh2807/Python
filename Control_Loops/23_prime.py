isprime = int(input("enter the number : "))
factors = 0
for i in range(1,isprime+1):
    if (isprime % i == 0) :
        factors = factors +1

if (factors == 2): print("prime number ")
else : print("composite")


