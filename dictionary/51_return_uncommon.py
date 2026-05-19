seta = {1,2,3,4}
setb = {3,4,5,6}

result = seta ^ setb
print(result) 

result = (seta | setb) - (seta & setb)