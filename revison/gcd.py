n1 = int(input("Enter the Number"))
n2 = int(input("Enter the number:"))

while n2 != 0:
    temp = n1%n2
    n1 = n2
    n2 = temp

print(n1)