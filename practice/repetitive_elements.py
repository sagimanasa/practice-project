# duplicate elements position
#
# def repetitive_element(arr):
#     result=[]
#     for i  in range(len(arr)):
#         for j in range(i+1,len(arr)):
#             if arr[i]==arr[j]:
#                 result.append(i)
#     return result
# arr=[1,2,3,4,2,5,6,2,7]
# print(repetitive_element(arr))

#output:[1,1,4]


#duplicate elements
def repetitive_element(arr,n):
    for i in range(0,n-1):
        for j in range(i+1,n):
            if arr[i]==arr[j]:
                print(arr[i])
arr=[1,2,3,4,5,2,4,6,7,8,7]
n=len(arr)
repetitive_element(arr,n)

#output:2
#       4
#       7