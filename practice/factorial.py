def fact(n):
    if n==0:
        return 1
    x=n*fact(n-1)
    return x
n=5
print(fact(n))

# output:120