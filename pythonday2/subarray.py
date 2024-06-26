# subarray
def create_map(arr, map): #create_map function creation
    #print("Entered create map")
    for i in arr: #iteration of arr
        if i not in map: #if  index i value is not present in map function
            map[i] = 1 #if arr value i in not there in map then value i is stored as key in map with value as 1

def sub_array(map, arr):# sub_array function creation
    for i in arr: #iteration of arr
        if i not in map: # if  i value is not located in map function
            return False #then it will show given arr is not a subarray
    return True #if all values in an array are present in map then it shows given arr is a subarray
base_arr = [1, 3, 5, 7, 8]
arr1 = [1, 5, 7]
arr2 = [1, 5, 7, 9]
arr3 = [1, 5]
arr4 = [7, 8]
map = {}
create_map(base_arr, map) # comparision of base_arr with map function
x=sub_array(map, arr1)
print(sub_array(map, arr1))
print(sub_array(map, arr2))
print(sub_array(map, arr3))
print(sub_array(map, arr4))