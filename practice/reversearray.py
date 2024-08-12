def swap(arr,i,j):
    temp=arr[i]
    arr[i]=arr[j]
    arr[j]=temp
def reverse_array(arr):
    i=0
    j=len(arr)-1
    while i<j:
        #print(i)
        #print(j)
        swap(arr,i,j)
        i=i+1
        #print(i+1)
        j=j-1
        #print(j-1)
arr=[5,4,3,2,1]
reverse_array(arr)
print(arr)
