arr=[3,6,2,20,19,21,45]
x=arr[0]
y=arr[0]
for i in arr:
    #print(i)
    if i>x:
       y=x
       #print(x)
       x=i
       #print(y)
    if i>x and i<y:
        y=i
print(y)