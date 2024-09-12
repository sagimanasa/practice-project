def prime_fact(n):
    factors=[]
    i=2
    while i<=n:
        if n%i==0:
            factors.append(i)
            n=n//i
            #print(n)
        else:
            i=i+1
    return factors
n=56
print(prime_fact(n))
