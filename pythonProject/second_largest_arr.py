arr1 = [3, 6, 9, 1, 20, 19]
x = arr1[0]
print(x)
y = arr1[0]
print(y)
for i in arr1:
    print(i)
    if i > x:
        print(i)
        y=x
        print(y)
        x = i
    if i<x and i>y:
        y = i
print(y)
