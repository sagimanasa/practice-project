def second_largest(arr,n):
    x=arr[0]
    y=arr[0]
    for i in range(1,n):
        if arr[i]>x:
            y=x
            x=arr[i]
        if arr[i]>x and arr[i]<y:
            y=arr[i]
    return y
arr=[9,17,2,7,15,21]
n=len(arr)
print(second_largest(arr,n))
# output:17


