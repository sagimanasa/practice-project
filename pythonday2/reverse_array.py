# def swap(arr,i,j):#function creation
#         temp=arr[i] #value in arr at index i is stored in temp variable
#         arr[i]=arr[j]#value stored at index j will be moved to index i location in arr
#         arr[j]=temp ##value in arr at index j is stored in temp variable
from swap_array import swap
def reverse_array(arr):#reverse function creation
    i=0
    j=len(arr)-1
    while i<j: # if value at index i is less than value at index j
        swap(arr,i,j) # swap the values at index i location to index j location
        i=i+1 #index i will be increased to next index value
        print(i)
        j=j-1 #index j will be decreased to before index value
        print(j)
a=[1,2,3,4,5] #array
print(a)
reverse_array(a)# reverse the array a
print(a)
