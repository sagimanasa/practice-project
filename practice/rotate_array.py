def swap(arr,i,j):
    temp=arr[i]
    arr[i]=arr[j]
    arr[j]=temp
def reverse(arr,i,j):
    while i<j:
        swap(arr,i,j)
        i=i+1
        j=j-1
def rotate_array(arr,n):
    a=n%len(arr)
    reverse(arr,0,a-1)
    reverse(arr,a,len(arr)-1)
    reverse(arr,0,len(arr)-1)
arr=[4,5,1,2,3]
n=2
rotate_array(arr,n)
print(arr)

#output:[1,2,3,4,5]