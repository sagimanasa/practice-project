arr1=[1,2,3,4,5]
print(arr1)
output=[]
print("start of loop")
for i in arr1:
    print(i)
    if i>3:
        print("inside if")
        output.append(i)
    else:
        print("Inside else")
        pass
    print("end of iteration")
print("end of loop")
print(output)
