arr1 = [3, 6, 9, 1, 20, 19]
x = arr1[0]
print(x)
for i in arr1:
    print(i)
    if i>x:
       print(i)
       x = i
       print(x)
print(x)
