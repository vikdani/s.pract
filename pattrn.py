def print_pattern():
    """ Function to print the pattern """
    
    for i in range (1,6,1):

        n=""
        for j in range(10,16-i,1):
            n=n+"*"
        print(n)         
    
    for i in range (5,0,-1):

        n=""
        for j in range(10,16-i,1):
            n=n+"*"
        print(n) 
   
    
    
    """Dont change anything below. If changed click on reset."""
def main():
    n=int(input())
    print_pattern()
    
main()
