def swap(arr,i,j):
    temp=arr[i]
    arr[i]=arr[j]
    arr[j]=temp
def reverse(arr):
    i=0
    j=len(arr)-1
    while i<j:
        swap(arr,i,j)
        i=i+1
        j=j-1
    return arr
arr=[5,6,3,2,1,4]
print(reverse(arr))
