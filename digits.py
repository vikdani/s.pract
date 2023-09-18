def print_digits(n):
    while n>0:
        print(n%10)
        n=n//10
        
    
def main():
    n=int(input("enter num"))
    print_digits(n)
    
main()
