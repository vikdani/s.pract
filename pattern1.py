
for i in range (1,6,1):

    n=""
    for j in range(10,16-i,1):
        n=n+"*"
    print(n)  


for i in range (1,6,1):
    n=""
    for k in range(1,6-i):
        print(" ",end="")
        
    for j in range(6,6-i,-1):
        n=n+"*"
    print(n)   