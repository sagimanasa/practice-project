def is_palindrome(number):
    num=str(number)
    left=0
    right=len(num)-1
    while left < right:
        if num[left]!=num[right]:
            return False
        left+=1
        right-=1
    return True
number=121
print(is_palindrome(number))
