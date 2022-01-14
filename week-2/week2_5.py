def maxZeros(nums):
    max_cnt = 0
    zero_cnt = 0
    for n in nums:
        if n == 0:
            zero_cnt += 1
        if zero_cnt > max_cnt:
            max_cnt = zero_cnt
        if n == 1:
            zero_cnt = 0
    print(max_cnt)

maxZeros([0, 1, 0, 0]) #2
maxZeros([1, 0, 0, 0 ,0 ,1, 0, 1, 0, 0]) #4
maxZeros([1, 1, 1, 1, 1]) #0
maxZeros([0, 0, 0, 1, 1]) #3