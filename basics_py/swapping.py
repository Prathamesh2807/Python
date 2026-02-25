a = int(input("enter the 1st number : "))
b = int(input("enter the second number : "))

print(f"orignal values : {a} , {b}")
temp = a
a=b
b=temp

print(f"after swapping : {a} , {b}")