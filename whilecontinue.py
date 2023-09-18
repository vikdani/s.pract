def series(n):
    i=1
    while i<=n:
        if i%5==0:
            i=i+1
            continue
        print(i)
        i=i+1
def main():
    n=int(input("Enter no"))
    series(n)
    
main()
