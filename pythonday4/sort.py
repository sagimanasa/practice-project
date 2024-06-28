def swap(arr,i,j):
    temp=arr[i]
    arr[i]=arr[j]
    arr[j]=temp
arr=[3,2,5,1]
for i in range(0,len(arr)):
    print(i)
    for j in range(i+1,len(arr)):
        print(j)
        if arr[i]>arr[j]:
            swap(arr,i,j)
print(arr)
