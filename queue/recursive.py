def recursive(arr,i):
    if i<0:
        #print(i)
        return
    print(arr[i])
    print("Index : "+str(i))
    recursive(arr,i-1)
    #print(i)
    print(arr[i])
arr=[1,2,3,4,5]
recursive(arr,len(arr)-1)
