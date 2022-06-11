arr = [9, 1, 5, 9, 4, 2, 7, 2, 9, 5, 3, 2, 3, 4, 7, 10]
arr2 = []

for item in arr :
    count = 0
    for x in arr :
        if x == item :
            count += 1
    arr2.append(count)

similar = set()
index = 0
while index < len(arr):
     if arr2[index] != 1:
         similar.add(arr[index])
     index += 1

print(similar)
