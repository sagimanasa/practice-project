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
    temp=arr[i] #value in arr at index i is stored in temp variable
    arr[i]=arr[j] # value stored at index j will be moved to index i location in arr
    arr[j]=temp#temp value is stored at location index j
# arr=[1,2,3,4,5]
# swap (arr,0,3)
# print(arr)
# swap (arr,1,4)
# print(arr)
# swap (arr,2,0)
# print(arr)
arr=[3,1,2,5,4] #array values
for i in range(0,len(arr)): #iteration of arr upto nth location of arr
    for j in range(i+1,len(arr)): #iteration of j from location i+1  to nth location of arr
        print(i,j) #finally prints the swapped values
    #print("end of inner")/
#print("end")




