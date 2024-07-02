def even(arr):
    x = 0
    for value in arr:
        if value % 2 == 0:
            x = x + 1
    return x
arr = [0, 1, 2, 3, 4, 5, 6, 12, 14]
print(even(arr))
