def swap(arr, i, j):   # swapping of array
    temp = arr[i]      # value in arr at index i is stored in temp variable
    arr[i] = arr[j]    # value stored at index j moved to index i location in an arr
    arr[j] = temp      # temp value is stored in arr at index j
arr = [3, 1, 2, 5, 4]
for i in range(0, len(arr)):  # iteration of arr from 0 upto nth location n=length of arr
    for j in range(i+1, len(arr)):  # iteration from location i+1 to nth location of arr
        if arr[i] < arr[j]:     #  if a[i] is less than a[j]( if first element is less than second element for sorting in decending order swap both)
            swap(arr, i, j)     #  arr will be swaped from location j as location i
print(arr)    # prints the sorted array
