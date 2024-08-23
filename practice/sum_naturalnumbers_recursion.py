def recursion(n):
    if n==0:
        return n
    return n+recursion(n-1)
n=6
print(recursion(n))
