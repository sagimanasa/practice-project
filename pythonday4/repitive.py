def repititive(arr):
    map={}
    for i in arr:
        if i in map:
           map[i] = map[i]+1
        else:
            map[i] = 1
    x = []
    for key in map:
        if map[key] == 1:
            x.append(key)
        return x
print(repititive([1, 2, 3, 2, 4, 3, 5, 6, 2]))





