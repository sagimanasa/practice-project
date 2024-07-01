def fact(n):
    if n==0:
       return 1
    x = n*fact(n-1)
    return x
print(fact(3))
