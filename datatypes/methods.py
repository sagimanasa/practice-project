# # zip() function
names = ["manasa", "hasmitha"]
ages = [21, 15]
print(list(zip(names, ages)))  # [('manasa',21),('hasmitha',15)]
print(".................")
names = ["manasa", "hasmitha"]
ages = [21, 15]
zipped = list(zip(names, ages))
new_names, new_ages = zip(*zipped)
print(new_names)  # ('manasa','hasmitha')
print(new_ages)  # (21,15)
print("...................")
list1 = [1, 2, 3]
list2 = [1, 2, 3]
for elem1, elem2 in zip(list1, list2):
    print(elem1, elem2)
# output:1 1
#       2 2
#       3 3
print("....................")
# enumerate() Function
x = ('apple', 'banana', 'cherry')
y = enumerate(x)
# print(list(y)) ##[(0,'apple'),(1,'banana'),(2,'cherry')]
# print(tuple(y)) ##((0,'apple'),(1,'banana'),(2,'cherry'))
# print(dict(y)) ##{0:'apple',1:'banana',2:'cherry'}
fruitlist = ["Grapes", "Apple", "Banana", "Kiwi"]
newlist = list(enumerate(fruitlist))
print(newlist)
fruitLst = ["Grapes", "Apple", "Banana", "Kiwi"]
print("The newly created list:")
for index, fruit in enumerate(fruitLst):
     print(f"Index: {index}, Value: {fruit}")
# output: the newly created list:
#         Index: 0, Value: Grapes
#         Index: 1, Value: Apple
#         Index: 2, Value: Banana
#         Index: 3, Value: Kiwi
