def print_series(n,m):
    """Print the following series from 1 to n if m is present stop printing the series 
    Note print all the numbers in a seperate line """
    
    for i in range (1,n+1):
        if i==m:
            break
        print(i)
   
    
    
    """Dont change anything below. If changed click on reset."""
def main():
    n=int(input())
    m=int(input())
    print_series(n,m)
    
main()
