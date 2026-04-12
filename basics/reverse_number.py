num = int(input("Enter number:-"))

ld = 0 
result = 0

while num >0:
    ld = num % 10
    result =  result * 10 + ld
    num  = num//10

print("reversed number", result)
