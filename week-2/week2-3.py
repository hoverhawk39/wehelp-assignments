def maxProduct(nums):
    num = len(nums)
    r1,r2=[],[]
    for i in range(num):
        for j in nums:
            mul=nums[i]*j
            r1.append(mul)
        r2.append(nums[i]**2)
    # print(r1)
    # print(r2)
    for x in r2:
        r1.remove(x)
    max_ans=max(r1)
    print(max_ans)

maxProduct([5, 20, 2, 6])
maxProduct([10, -20, 0, 3])
maxProduct([-1, 2])
maxProduct([-1, 0, 2])
maxProduct([-1, -2, 0])