a = int(input("enter the number of stu in class 1 : ")) 
b = int(input("enter the number of stu in class 2 : ")) 
c = int(input("enter the number of stu in class 3 : ")) 

desks_a = (a%2) + (a / 2) 
desks_b = (b%2) + (b / 2) 
desks_c = (c%2) + (c / 2) 
sum = desks_a + desks_b + desks_c
print(f"no of desks needed for class 1 is : {desks_a}")
print(f"no of desks needed for class 1 is : {desks_b}")
print(f"no of desks needed for class 1 is : {desks_c}")
print(f"the total no of desks will be {sum}")