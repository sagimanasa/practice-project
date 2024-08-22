def code_conversion(arr):
    result=0
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if arr[j]<arr[i]:
                result=result+1
    return result
arr=[6,3,5,2,9,1]
print(code_conversion(arr))


