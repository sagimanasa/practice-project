def largest_element(arr,n):
    max=arr[0]
    for i in range(1,n):
        if arr[i]>max:
            max=arr[i]
    return max
arr=[9,7,10,11,20,3,5,17]
n=len(arr)
print(largest_element(arr,n))
# output:20
