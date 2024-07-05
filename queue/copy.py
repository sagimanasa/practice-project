def copy(arr,temp,j):
    for i in temp:#taking indexes from temp with iteration
        arr[j]=i #modifying the i value in the array
        j=j+1 #and incrementing array index value what next to be modified
    return arr # returns the final modified array
arr=[3,1,10,9] #it is the original array
temp=[1,3] #it is the temporary array which is to be placed in the original array
#print(copy(arr,temp,2))
