# arr=[3,2,1,5,0]
# x=arr[0]
# for value in arr:
#     if value<x:
#        x=value
# print(x)

# def small(arr):
#     x=arr[0]
#     for value in arr:
#         if value<x:
#             x=value
#     return x
# arr=[3,2,1,5,0]
# print(small(arr))

def smallfunc(arr,small, index):
    print("step1: index :"+str(index)+" small :"+str(small))
    if len(arr)==index:
        print("step2: index :" + str(index) + " small :" + str(small))
        return small
    if small>arr[index]:
        print("step3: index :" + str(index) + " small :" + str(small))
        return smallfunc(arr,arr[index],index+1)
    else:
        print("step4: index :" + str(index) + " small :" + str(small))
        return smallfunc(arr, small, index + 1)
arr=[3,2,1,5,0,-1,12]
print(smallfunc(arr,arr[0],1))

# def largefun(arr,large,index):
#     if len(arr)==index:
#         return large
#     if large<arr[index]:
#         return largefun(arr,arr[index],index+1)
#     else:
#         return largefun(arr,large,index+1)
# arr=[2,5,1,6,3,8]
# print(largefun(arr,arr[0],1))



