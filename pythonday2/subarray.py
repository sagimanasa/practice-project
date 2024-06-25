# subarray
def create_map(arr, map):
    #print("Entered create map")
    for i in arr:
        if i not in map:
            map[i] = 1

def sub_array(map,arr):
    for i in arr:
        if i not in map:
            return False
    return True
base_arr=[1,3,5,7,8]
arr1=[1,5,7]
arr2=[1,5,7,9]
arr3=[1,5]
arr4=[7,8]
map={}
create_map(base_arr,map)
print(sub_array(map,arr1))
print(sub_array(map,arr2))
print(sub_array(map,arr3))
print(sub_array(map,arr4))