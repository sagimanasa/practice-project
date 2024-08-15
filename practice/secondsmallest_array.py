def second_smallest(arr,n):
    x=arr[0]
    y=arr[0]
    for i in range(1,n):
        if arr[i]<x:
            y=x
            x=arr[i]
        if arr[i]<x and arr[i]<y:
            y=arr[i]
    return y
arr=[9,8,6,3,21,1]
n=len(arr)
print(second_smallest(arr,n))
# output:3

