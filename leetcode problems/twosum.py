#two sum in leetcode
def two_sum(nums,target):#define function named two sum
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            if nums[i]+nums[j]==target:#check if the sum of the pair is equal to target
                return [i,j]
    return None#if no solution found it returns none
nums=[2,7,11,15]
target=9
result=two_sum(nums,target)
print(result)
#output:[0,1]