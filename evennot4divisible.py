def print_output(n):
    """Print all even numbers from 1 to n except the ones divisible by 4
    use the help of continue statement to leverage this  """
    
    for i in range (1,n+1):
        if i%4==0:
            continue
        if i%2==0:
            print(i)
                    
           
   
    
    
    
    
    
    
    
    
    """Dont change anything below. If changed click on reset."""
def main():
    n=int(input())
    print_output(n)
    
main()