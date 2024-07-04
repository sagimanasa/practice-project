def sum(arr):
    x=[]
    a=0
    for value in arr:
        #print(value)
        a=a+value
        #print(a)
        x.append(a)
        #print(x)
    return x
arr=[3,4,9,1,7]
x=sum(arr)
print(x)

# print("##############")
# def sum(arr):
#     a=0
#     for value in arr:
#         print(value)
#         a=a+value
#         print(a)
#     return a
# arr=[3,6,1,9,12]
# print(sum(arr))

