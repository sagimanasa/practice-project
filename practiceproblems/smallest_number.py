def small_num(arr):
    result = arr[0]
    for value in arr:
        if value < result:
            result = value
    return result
arr = [3, 8, 6, 10]
print(small_num(arr))
#output:3
