n = int(input("ENter Number"))

for i in range(0,n):
    for j in range (0 , i+1):
        print("*", end ="")

    print()

for i in range (1,n):
    for j in range(0,n-i):
        print("*", end="")
    print()