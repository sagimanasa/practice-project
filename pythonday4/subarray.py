def create(arr,map):
    for i in arr:
        if i not in map:
            map[i]=1
def subarray(map,arr):
    for i in arr:
        if i not in map:
            return False
    return True
base_arr=[2,3,6,7,9,10]
a1=[2,3,4]
a2=[2,9,10]
a3=[3,6,8]
map={}
create(base_arr,map)
x=subarray(map,a3)
print(x)

