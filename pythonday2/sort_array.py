def swap(arr,i,j):#swapping of array
    temp=arr[i] #i value stored in temp
    arr[i]=arr[j] #j stored in i location
    arr[j]=temp #the again temp value will comes to j
arr=[3,1,2,5,4]
for i in range(0,len(arr)):
    for j in range(i+1,len(arr)):
        if arr[i]<arr[j]:
            swap(arr,i,j)
print(arr)

