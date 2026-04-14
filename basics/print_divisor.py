# #brute Force
# n = int(input("Enter the number:"))

# result = []

# for i in range(1 , n +1):
#     if n % i == 0:
#         result.append(i)

# print(result)
# Tc = o(n)
# SC = O(k) k is total no of factor

# optimal soln
# n = int(input("Enter the number"))

# result = []
# for i in range ( 1 , n//2):
#     if n % i ==0:
#         result.append(i)

# result.append(n)

# print(result)

# TC = O(n/2) ~ o(n)
# # SC = O(k)

# # best solution 

# from math import sqrt
# num = int(input("enter no"))
# result = []

# for i in range(1, int(sqrt(num) ) +1):
#     if num % i == 0:
#         result.append(i)

#         if num // i != i:
#             result.append(num//i)

# result.sort()
# # print(result)

# # Tc = O(√n)
# # sc=O(k) k is factors in result
