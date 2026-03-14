# Input the coordinates of the three given vertices
x1 = int(input("Enter the x-coordinate of the first vertex: "))
y1 = int(input("Enter the y-coordinate of the first vertex: "))

x2 = int(input("Enter the x-coordinate of the second vertex: "))
y2 = int(input("Enter the y-coordinate of the second vertex: "))

x3 = int(input("Enter the x-coordinate of the third vertex: "))
y3 = int(input("Enter the y-coordinate of the third vertex: "))

# Determine the unique x and y coordinates
if x1 == x2:
    x4 = x3
elif x1 == x3:
    x4 = x2
else:
    x4 = x1

if y1 == y2:
    y4 = y3
elif y1 == y3:
    y4 = y2
else:
    y4 = y1

# Print the coordinates of the fourth vertex
print(f"The coordinates of the fourth vertex are: ({x4}, {y4})")