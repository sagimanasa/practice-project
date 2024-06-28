def swap(arr,i,j):
    temp=arr[i]
    arr[i]=arr[j]
    arr[j]=temp
    print(arr)
def reverse(arr,i,j):
    while i<j:
        swap(arr,i,j)
        i=i+1
        print(i)
        j=j-1
        print(j)
def rotate(arr,n):
    b=n% len(arr)
    reverse(arr,0,b-1)
    reverse(arr,b,len(arr)-1)
    reverse(arr,0,len(arr)-1)
arr=[2,4,3,5]
n=7
rotate(arr,n)
print(arr)


