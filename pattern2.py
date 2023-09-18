def print_pattern():
    
  
    
    i=1
    
    while i<=n:
        j=n
        while j>=i:
            print("*",end="")   
            j=j-1
        print()
        i=i+1
       

def main():
    global n
    n=int(input())
    print_pattern()
    
main()

    
