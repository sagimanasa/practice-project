def even_count(arr):
    count=0
    for i in arr:
        if i%2==0:
            count=count+1
    return count
arr=[1,7,8,4,5,16]
print(even_count(arr))