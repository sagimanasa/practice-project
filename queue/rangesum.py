def rangesum(arr,startindex,endindex):
    outputsum=0
    print(outputsum)
    #i=startindex
    while startindex <= endindex:
        #print(i)
        outputsum=outputsum+arr[startindex]
        print(outputsum)
        startindex=startindex+1
    return outputsum
arr=[3,4,9,1,7]
print(rangesum(arr,0,1))
