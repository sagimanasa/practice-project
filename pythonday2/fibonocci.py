def fibonocci(n):#fibonocci function creation
    if n==0: #base function if n value is 0 it returns empty array
        return []
    if n==1:#if n value is 1 it returns starting index value
        return [0]
    if n==2:#if n value is 2 it returns first two index values
        return [0,1]
    output=[0,1]
    for i in range(2,n):
        output.append(output[i-1]+output[i-2])#to find next index value we have to add i-1 index value and i-2 index value
    return output
print(fibonocci(20))#it prints the fibonocci series upto 20 





