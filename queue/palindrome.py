def palindrome(arr,i,j):
    print(i)
    print(j)
    if i == j:
        print(i)
        print(j)
        return True
    if arr[i] == arr[j]:
       print("Index: ",str(i))
       print(j)
       x=palindrome(arr,i+1,j-1)
       print(i)
       print(j)
       return x
    return False
arr=[1,2,3,4,3,2,1]
print(arr)
print(palindrome(arr,0,len(arr)-1))
