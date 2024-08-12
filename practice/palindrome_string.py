def is_palindrome(s):
        i=0
        j=len(s)-1
        while i<j:
            #print(i) #0,1
            #print(j) #5,4
            if s[i]!=s[j]:
                return False
            i=i+1
            #print(i+1) #2
            j=j-1
            #print(j-1) #3
        return True
s="manasm"
print(is_palindrome(s))
