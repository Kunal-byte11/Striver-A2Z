num = int(input("Enter the number"))
ld = 0
result = 0
inital = num


while num > 0:
    ld = num % 10
    result = result*10 + ld
    num = num // 10

if inital == result :
    print("Palindrome")

else:
    print("Non Palindrome")

