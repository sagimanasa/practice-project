def fibonocci(n):
    if n==0:
        return []
    if n==1:
        return[0]
    if n==2:
        return[0,1]
    result=[0,1]
    for value in range(2,n):
        result.append(result[value-1]+result[value-2])
    return result
print(fibonocci(10))