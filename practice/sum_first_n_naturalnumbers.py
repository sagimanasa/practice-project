# num=5
# sum=0
# for i in range(num+1):
#     sum+=i
# print(sum)
#
# #output:15

#using recursion
def recursion(n):
    if n==0:
        return n
    return n+recursion(n-1)
n=5
print(recursion(n))
