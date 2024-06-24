arr1 = [10, 20, 30]
print(arr1[0])
arr1.append(40)
print(arr1)
arr2 = [50, 60, 70]
arr1.extend(arr2)
print(arr1)
arr1.append(arr2)
print(arr1)
for i in range(len(arr2)):
    print(arr2[1])
arr2.remove(60)
print(arr2)
for i in range(len(arr2)):
    print(arr2[0:1])
print(arr1.index(30))
arr3 = ["a", "b", "c"]
i = len(arr3)
for x in range(i):
    print(arr3[x])
    print(arr3.index("c"))
    print(arr3[0:1])
