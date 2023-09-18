def print_series(n):
    """Print all odd numbers from 1 to n (including)
    Note print all the numbers in a seperate line"""
    
   
    for i in range(1,n+1):
        if i%2==1:
            print(i)
    
    
    
    
    
    
    
    """Dont change anything below. If changed click on reset."""
def main():
    n=int(input())
    print_series(n)
    
main()
