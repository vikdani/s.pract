def print_series(n):
    """ Print the following series 
    1 8 27 64 125 to n (including) . Note print all the numbers in a seperate line """
    
   
    
    for i in range (1,n+1):
        if i*i*i>n:
            break
        print(i*i*i)
        
    
    
    
    
    
    
    
    """Dont change anything below. If changed click on reset."""
def main():
    n=int(input())
    print_series(n)
    
main()