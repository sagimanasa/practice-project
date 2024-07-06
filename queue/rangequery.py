from array_sum import sum
def rangequery(presum, start, end):
     print(start)
     print(end)
     output = presum[end]-presum[start-1]
     print(output)
     return output
arr = [3, 5, 2, 7, 9, 6]
presum = sum(arr)
print(presum)
print(rangequery(presum, 2, 3))
