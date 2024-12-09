# def camel_case(n):
#     words=n.split( )
#     result=words[0].lower()
#     for word in words[1:]:
#         result=result+word[0].upper() + word[1:].lower()
#     return result
# n="my name is manasa"
# print(camel_case(n))
#output:myNameIsManasa

def camel_case(s):
    return s.title()
s="iam writing code"
print(camel_case(s))
#ouput:Iam Writing Code