num = int(input("Enter number:-"))
ld = 0
result = 0
inital = num


while num > 0:
    ld = num % 10
    

    result = result*10 + ld

    num = num//10

if   inital ==  result :
    print("It is a palindrome", inital , result)

else:
    print("It is not a palindrome", inital, result)

# tc = > O(n) and SC = > O(1)

