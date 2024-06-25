# arr=[1,2,3,4,5]
# len_arr=len(arr)
# x=1
# y=2
# temp=x
# x=y
# y=temp
# temp=a[0]
# a[0]=a[3]
# a[3]=temp
# print(a)
# for i in range(0,b-1):
#     a[i],a[i+1]=a[i+1],a[i]
# print(a)
def swap(arr,i,j): #swapping of two values
    temp=arr[i]
    arr[i]=arr[j]
    arr[j]=temp
# arr=[1,2,3,4,5]
# swap (arr,0,3)
# print(arr)
# swap (arr,1,4)
# print(arr)
# swap (arr,2,0)
# print(arr)
arr=[3,1,2,5,4] #array values
for i in range(0,len(arr)): #iteration
    for j in range(i+1,len(arr)):
        print(i,j)
    #print("end of inner")
#print("end")




