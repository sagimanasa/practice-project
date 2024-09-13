def anagram(str1,str2):
    if sorted(str1)==sorted(str2):
            return True
    return False
str1="manu" # this will return false
str2="honey"
# str1="listen" # this returns true
# str2="silent"
print(anagram(str1,str2))


def anagram(str1,str2):
    if len(str1)!=len(str2):
        return False
    else:
        str1=sorted(str1)
        str2=sorted(str2)
    if str1==str2:
        return True
    return False
str1="silent"
str2="listen"
print(anagram(str1,str2))


