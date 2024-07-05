import math
def search(arr, element, i, j):
    if i>j:
        return False
    mid = math.floor(i+(j-i)/2)
    print(i,j)
    print(mid)
    if arr[mid] == element:
       print(arr[mid])
       return True

    elif element<arr[mid]:
       return search(arr,element,i,mid-1)

    elif element>arr[mid]:
         return search(arr,element,mid+1,j)
    else:
        return False

arr = [1, 2, 10, 16, 21]
print(search(arr, 1, 0, len(arr)-1))
