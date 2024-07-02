def even_count(arr,index):
    print("step1: index :" + str(index))
    if len(arr)==index:
        print("step2: index :" + str(index))
        return 0
    if arr[index]%2==0:
       print("step3: index :" + str(index))
       return 1+even_count(arr,index+1)

    else:
        print("step4: index :" + str(index))
        return even_count(arr,index+1)

arr=[8,1,2,3,4,5,6,7,10,12]
print(even_count(arr,0))