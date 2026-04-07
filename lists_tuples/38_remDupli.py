var = [17 , 28 , 14 , 14 , 17]
k = 0 

for i in range(4):
    if (var[i] != var[i+1]):
        var[k] = var[i]
        k = k+1

var[k] = var[i]
print(var)
for i in range(0,k):
    print(var[i])