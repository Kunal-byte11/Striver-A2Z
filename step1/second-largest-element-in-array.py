arr = [10, 5, 20, 8]

l_value = float("-inf")
s_value = float("-inf")

for i in range(len(arr)):
    if arr[i] > l_value:
        s_value = l_value
        l_value = arr[i]

    elif arr[i] > s_value and arr[i] != l_value:
        s_value = arr[i]

print(s_value)
        





