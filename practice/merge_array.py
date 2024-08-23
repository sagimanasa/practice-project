def merge_array(arr1,arr2):
    result=[]
    a=0
    b=0
    while a<len(arr1):
        result.append(arr1[a])
        a=a+1
    while b<len(arr2):
        result.append(arr2[b])
        b=b+1
    return result
arr1=[1,2,3,4]
arr2=[5,6,7,8]
print(merge_array(arr1,arr2))