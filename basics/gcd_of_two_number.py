n1 = int(input("Enter number"))
n2 = int(input("Enter number"))

while n2 != 0:
    temp = n1 % n2
    n1 = n2
    n2 = temp

print("GCD" , n1)