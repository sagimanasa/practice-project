def subarray_sum(arr):
    result=0
    for i in arr:
        result=result+i
    return result
arr=[1,3,5,7]
print(subarray_sum(arr))
