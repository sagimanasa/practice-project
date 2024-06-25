def find_max(arr): #function creation
    map={} #map  initialization
    for i in arr: #iteration
        if  i in map: #if  value i in arr is located in map then increment the count of that value
            map[i]=map[i]+1 # then count of  value i  will be incresed by 1
        else:
            map[i]=1 #if arr value i in not there in map then value i is stored as key in map with value as 1
    maxkey= arr[0] # key with max count value will be stored in maxkey, initially the first element of arr is stored
    for key in map:
        if map[key]>map[maxkey]: #if  value of key in map is more than value of maxkey in map
            maxkey=key #then key  will be stored in maxkey
    return maxkey #final maxkey is returned
input1 = [1,2,1,3,1,4,2,4,5]
input2 = [1,2,1,3,1,4,2,2,2,4,5]
input3 = [1,2,1,3,1,4,2,2,2,4,5,4,5,6,4,4,4]
input4 = [1,2,1,3,1,4,2,2,2,4,5,3,3,3,3,3]
print(find_max(input4))# it will find most repeated values in given input