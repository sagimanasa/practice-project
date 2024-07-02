def add(n):
    if n==0:
       return 0
    x= add(n-1)+n
    return x
print(add(10))