def print_pattern():

    for i in range (5,0,-1):
        for j in range(1,i+1):
            print("*",end="")
        print("\n")    

    for i in range(1,6):
        for j in range(1,i+1):
            print("*",end="")
        print("\n")
    
            
    
   
    

def main():
    n=int(input())
    print_pattern()
    
main()
