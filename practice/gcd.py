# def gcd(a,b):
#     if a==0:
#         return b
#     return gcd(a,b%a)
# a=10
# b=8
# print(gcd(10,8))

def gcd(a,b):
    if b==0:
        return a
    return gcd(b,a%b)
a=9
b=2
print(gcd(a,b))
# output:1