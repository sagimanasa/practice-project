def find_max(arr): #function creation
    map={} #dic creation
    for i in arr: #iteration
        if  i in map:
            map[i]=map[i]+1 #to find count
        else:
            map[i]=1
    maxkey= arr[0]
    for key in map:
        if map[key]>map[maxkey]: #to find highest count of duplicate values
            maxkey=key
    return maxkey
input1 = [1,2,1,3,1,4,2,4,5]
input2 = [1,2,1,3,1,4,2,2,2,4,5]
input3 = [1,2,1,3,1,4,2,2,2,4,5,4,5,6,4,4,4]
input4 = [1,2,1,3,1,4,2,2,2,4,5,3,3,3,3,3]
print(find_max(input4))