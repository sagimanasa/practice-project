
def gcd(a,b):
    if b==0:
        return a
    return gcd(b,a%b)
a=10
b=8
print(gcd(a,b))
# output:1