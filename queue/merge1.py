def merge1(arr1, arr2): #defining the merge function
    result = [] #final merged array will be stored here
    l1 = len(arr1)-1 #l1 starting at end index of arr1
    l2 = len(arr2)-1 #l2 starting at end index of arr2
    while l1 >= 0 and l2 >= 0: #the l1 index should not be greater than 0 index of arr1 and l2 index should not be greater than 0 index of arr2
        if arr1[l1]<arr2[l2]: #if l1 value is less than l2 value
            result.append(arr2[l2])#the l2 value is stored in the result
            l2 = l2-1#and moving the l2 into before location
        else:
            result.append(arr1[l1])#if l1 is greater value then
            l1 = l1-1
    while l1 >= 0:
            result.append(arr1[l1])
            l1 = l1-1
    while l2 >= 0:
            result.append(arr2[l2])
            l2 = l2-1
    return result
arr1=[3, 6, 25, 34]
arr2=[5, 8, 11, 15]
print(merge1(arr1, arr2))
