def fibonocci(n):
    if n==0:
        return []
    if n==1:
        return [0]
    if n==2:
        return [0,1]
    output=[0,1]
    for i in range(2,n):
        output.append(output[i-1]+output[i-2])
    return output
print(fibonocci(9))
