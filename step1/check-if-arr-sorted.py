arr = [1, 2, 2, 3, 4]

for i in range (len(arr)-1):
    if arr[i] >  arr[i+1]:
        print( False)

        break

print (True)