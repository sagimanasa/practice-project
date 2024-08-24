def even_odd(arr):
    even=0
    odd=0
    for i in arr:
        if i%2==0:
            even=even+1
        else:
            odd=odd+1
    return even,odd
arr=[1,3,4,6,8,9,0]
print(even_odd(arr))
