import math #importing math function because floor operation comes under math function
from merge import merge #importing the merge file
from copy import copy #importing the copy file
def divide(arr,i,j): #creating divide function
    print(i,j)
    if i==j: #if i and j indexes became same then it returns
       return
    mid=math.floor(i+(j-i)/2) #creating mid function to divide tha array into subarrays useing floor operation the floor operation gives approximate value
    print(mid)
    divide(arr,i,mid) #i divides the array from starting to middle value
    divide(arr,mid+1,j)#it fivides mid next value to j
    x=merge(arr[i:mid+1],arr[mid+1:j+1]) #it will combine the subarrays into one array using merge operation
    print(x)
    copy(arr,x,i)#it will copy the array from merge array and replaces it into original array
arr=[3,6,25,34,5,8,15,11]
divide(arr,0,len(arr)-1)#giving the starting and ending values of array to be divided
print(arr)#prints the final modified array
