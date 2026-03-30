n = int(input("Enter number:-"))

for i in range(0,n):
    for j in range(n, i ,-1):
        print(n-j+1,end="")
    print()