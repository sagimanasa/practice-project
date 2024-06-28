def find(arr,s):
    x=set()#empty set creation
    for i in arr:#iteration
        x.add(i) #coverting array into set
    for i in arr: #iteration
        j=s-i
        if j in x: #if j value is located in x
            return True #returns true if j value present in x
    return False #if j value not there in x then it returns false
arr=[1, 2, 4, 9]#array values
s=2 #initializing s as 2
print(find(arr, s)) #returns either true or false


