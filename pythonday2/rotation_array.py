def swap(arr,i,j):
    temp=arr[i] ##value in arr at index i is stored in temp variable
    arr[i]=arr[j]#value stored at index j will be moved to index i location in arr
    arr[j]=temp##value in arr at index j is stored in temp variable
def reverse(arr,i,j):#reverse function creation
    #print(i,j)
    while i<j: # if value at index i is less than value at index j
        swap(arr,i,j)# swap the values at index i location to index j location
        #print(arr)
        i=i+1#index i will be increased to next index value
        j=j-1#index i will be decreased to before index value
def rotate(arr,r):#rotate function creation
    #print(n)
    a= r % len(arr)#hash function is used to find a value
    #print(a)
    reverse(arr,0,a-1)#reversing the array values from starting index value to a-1 index value
    #print(arr)
    reverse(arr,a,len(arr)-1)#reversing the array values from a index value to len(arr) index value
    #print(arr)
    reverse(arr,0,len(arr)-1)#reversing the array values from starting index value  to len(arr) index value
arr=[1,2,3,4,5]#array creation
n=6
rotate(arr,n)#rotating the array with given n number of times
print(arr)



