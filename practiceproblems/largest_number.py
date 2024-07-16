def largest_num(arr):
    result = arr[0]
    for value in arr:
        if value > result:
            result = value
    return result
arr = [8, 5, 3, 10]
print(largest_num(arr))
#output=10
