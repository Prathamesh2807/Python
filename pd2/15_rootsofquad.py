import math as m 

a = int(input("enter a : "))
b = int(input("enter b : "))
c = int(input("enter c : "))

disc = b**2 - 4*a*c 

if (a==0):
    print("invalid quad")
elif (disc > 0 ):
    root1 = (-b + m.sqrt(disc))/ 2*a 
    root2 = (-b - m.sqrt(disc))/ 2*a 
    print(f"{root1} and {root2} are the roots")

elif (disc == 0):
    root = -b /2*a
    print(f"the roots are equal and are = {root}")

else :
    print("complex roots are the there {x + iy}")
    x = -b /(2*a)
    y = m.sqrt(-disc)/(2*a)
    root1 = x + (y * 1j)
    root2 = x - (y * 1j)
    print("the roots are : " , root1 , "&" , root2 )

