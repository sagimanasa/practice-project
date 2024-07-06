def merge(arr1,arr2):
    output=[]
    l1=0
    l2=0
    while l1<len(arr1) and l2<len(arr2):  #  l1 index value should be less than length of arr1 (and) l2 index value sholud be less than length of arr2
        if arr1[l1]<arr2[l2]:  # if l1 index value is less than l2 index value
            output.append(arr1[l1])  #  add the l1 value in output array
            l1=l1+1  #  l1 index value
        else:
            output.append(arr2[l2])  #  if not add the l2 index value to the output
            l2=l2+1

    while l1<len(arr1):  #  if there is no values in the arr2 to check we have to append the remaining arr2 values
        output.append(arr1[l1])
        l1 = l1 + 1

    while l2<len(arr2): # if there is no values in the arr1 to check we have to append the remaining arr1 values
        output.append(arr2[l2])
        l2 = l2 + 1
    return output

arr1=[3,6,25,34]
arr2=[5,8,11,15]
#print(merge(arr1,arr2))
