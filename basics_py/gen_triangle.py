import math as m
a = int(input("enter the first num : "))
b = int(input("enter the sec num : "))
c = int(input("enter the third num : "))
s = (a+b+c)/2

area = m.sqrt(s*(s-a)*(s-b)*(s-c))
print("the area of the general triangle is : ",area)