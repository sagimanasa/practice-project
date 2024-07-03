# def swap(arr,i,j):
#     temp=arr[i]
#     arr[i]=arr[j]
#     arr[j]=temp
from swap import swap
def reversearr(arr,i,j):
    if i>=j:
        return
    swap(arr,i,j)
    reversearr(arr,i+1,j-1)
arr=[1,2,3,4,5,6]
print(reversearr(arr,0,len(arr)-1))
print(arr)
