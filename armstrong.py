def check_armstrong(n):

    temp=n
    count=0
    while temp>0:
        count=count+1
        temp=temp//10
    sum=0
    temp=n
    while temp>0:
        rem = temp % 10
        sum = sum + pow (rem,count)
        temp = temp//10
    if sum==n:
        print("true")
    else:
        print("false")    


   

def main():
    n=int(input("enter any number"))
    check_armstrong(n)
    
main()
