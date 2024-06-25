def Find_rep(arr): #function creation
    map={}
    for i in arr:
        if i in map:
            map[i]=map[i]+1 #count
        else:
            map[i]=1
        #print(i)
    a=[]
    for key in map:
        if map[key]==1:
           a.append(key) # adding non repititive values
    return a
print(Find_rep([1,3,2,2,4,5,5]))