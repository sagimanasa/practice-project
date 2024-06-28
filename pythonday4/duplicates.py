def dup(arr):
    map={}
    print(map)
    for i in arr:
        print(i)
        if i in map:
            map[i]=map[i]+1
            #print(i)
        else:
            map[i]=1
            #print(i)
    maxkey=arr[0]
    for key in map:
        print(map)
        print(key)
        if map[key]>map[maxkey]:
           maxkey=key
           print(maxkey)
    return maxkey
arr=[1, 1, 2, 2, 2, 3, 3, 5, 4, 1, 1]
print(dup(arr))
