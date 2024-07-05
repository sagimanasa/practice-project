def even_odd(arr): #creating even_odd function
    even = []#creating empty array
    odd = []
    for value in arr:#iteration of an array
        print(value)
        if value % 2 == 0:#dividing the values of array to know whether even or odd
            even.append(value)
        else:
            odd.append(value)
    return even,odd
arr = [1, 2, 3, 4, 5, 6]
even,odd= even_odd(arr)
#odd = even_odd(arr)
print(even,odd)
#print(odd)
