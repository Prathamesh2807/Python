var = []
n  = int(input("enter the no of stu : "))
for i in range (n):
    name = str(input("enter name  : "))
    var.append(name)
    print(f"the {i+1} element is : ", var[i])