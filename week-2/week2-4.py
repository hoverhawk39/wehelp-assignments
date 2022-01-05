def twoSum(nums, target):
    num=len(nums)
    for i in range(num):
        a1=target-nums[i]
        if a1>0:
            for j in range(i+1,num):
                if nums[j] == a1:
                    ans=[]
                    ans.extend([i,j])
                    return ans

result=twoSum([2, 11, 7, 15], 9)
print(result)