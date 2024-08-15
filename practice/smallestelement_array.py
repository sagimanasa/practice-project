# arr=[6,1,9,3,0,2]
# min=arr[0]
# for i in arr:
#     if i<min:
#         min=i
# print(min)
#


def smallest_element(arr,n):
    min=arr[0]
    #print(min)
    for i in range(1,n):
        if arr[i]<min:
            #print(i)
            min=arr[i]
            #print(min)
    return min
arr=[6,1,9,3,0,2]
n=len(arr)
print(smallest_element(arr,n))
# output:0