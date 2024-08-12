def create(arr,map):
    for i in arr:
        if i not in map:
            map[i]=1
def subarray(map,arr):
    for i in arr:
        if i not in map:
            return False
    return True
arr=[1,2,3,4,5,6,7]
a=[1,2,8]
b=[4,5,6]
map={}
create(arr,map)
x=subarray(map,b)
print(x)
