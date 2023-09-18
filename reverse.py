
def reverse(n):

    
    reverse=0
    while n>0:
        reverse=(reverse*10)+(n%10)
        n=n//10
    return reverse    
    
    
def main():
    n=int(input())
    output = reverse(n)
    print(output)
    
main()
