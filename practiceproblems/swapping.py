def swap(arr, i, j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp
arr = [2, 3, 4, 5]
for i in range(0, len(arr)):
    for j in range(i+1, len(arr)):
        print(i, j)
