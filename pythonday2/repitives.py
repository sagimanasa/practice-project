def Find_rep(arr): #function creation
    map = {} #empty dictionary is initialized
    for i in arr: #iteration of arr
        if i in map: #if i value i in arr is located in map then increment the count of that value
            map[i] = map[i]+1 #count of  value i will be increased by 1
        else:
            map[i] = 1 #if arr value i in not there in map then value i is stored as key in map with value as 1
        #print(i)
    a = [] #empty array
    for key in map: #iteration of mapfunction
        if map[key] == 1: #if map key  count is 1 then
           a.append(key) # key will be added to arr
    return a #it returns non repeated keys stored  in a(array/list)
print(Find_rep([1, 3, 2, 2, 4, 5, 5]))
