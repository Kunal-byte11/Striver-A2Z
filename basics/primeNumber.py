# n = int(input("Enter the Number"))

# is_prime = True

# for i in range(2, n):
#     if n % i == 0:
#         is_prime = False
#         break

# if is_prime and n > 1:
#     print("Prime Number")

# else:
#     print("Number is not prime")

# TC = O(n)
# SC=O(1)

# optmal solution


n = int(input("Enter the NUmber"))
 
from math import sqrt

is_prime = True

for i in range(2, int(sqrt(n))+1):
    if n % i == 0:
        is_prime = False
        break

if is_prime and n>1:
    print("Number is Prime")

else:
    print("Number is not Prime")

# Tc(√n) ~ O(n)
# sc=O(1)