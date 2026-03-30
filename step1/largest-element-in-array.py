arr = [3,7,2,9,4]

n=len(arr)


largest_value = float("-inf")

for i in range(n):
    largest_value = max(largest_value, arr[i])

print(largest_value)

#tc=O(n)
#sc= o(1)