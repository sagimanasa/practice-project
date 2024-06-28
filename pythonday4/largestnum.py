arr=[3,6,9,19,11]
x=arr[0]
print(x)
for i in arr:
    print(i)
    if i>x:
       x=i
       print(i)
print(x)