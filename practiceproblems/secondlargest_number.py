def second_small(arr):
    result1=arr[0]
    result2=arr[0]
    for value in arr:
        if value>result1:
            result2=result1
            result1=value
        if value<result1 and value>result2:
            result2=value
    return result2
arr=[3,6,8,10,9]
print(second_small(arr))