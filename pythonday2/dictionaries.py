dict={ }
dict["apple"]="fruit"
print(dict)
dict["10"]=5
print(dict)
dict["10"]=6
print(dict)
del dict["10"]
print(dict)
dict.update({"rose":"flower"})
print(dict)
dict.update({"10":5})
print(dict)
if dict["10"]==5:
   dict["10"]=6
print(dict)
dict1={'apple': 'fruit', 'rose': 'flower', '10': 6}
del dict["rose"]
dict["apple"]=100
print(dict)
dict.update({"rose":"flower"})
print(dict)
for key in dict:
      print(key,dict[key])
# for key,value in dict:
#       print(key,value)
if "mango" in dict:
      print("mango")
else:
      print("null")
if "rose" in dict:
      print("rose")
else:
      print("null")



