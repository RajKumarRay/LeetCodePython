# Question Link:
# https://leetcode.com/problems/maximum-alternating-sum-of-squares/


class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        nums=[abs(i) for i in nums]
        nums.sort(reverse=True)
        nums_len=len(nums)
        if nums_len & 1:
            nums_len=nums_len//2+1
        else:
            nums_len=nums_len//2

        # sum_pos=0
        # for i in range(0,nums_len):
        #     sum_pos+=nums[i]*nums[i]
        # sum_neg=0
        # for i in range(nums_len,len(nums)):
        #     sum_neg+=nums[i]*nums[i]
        # return sum_pos-sum_neg



        # Use of Iterators.
        # sum_pos=sum(nums[i]*nums[i] for i in range(0,nums_len))
        # sum_neg=sum(nums[i]*nums[i] for i in range(nums_len,len(nums)))
        # return sum_pos-sum_neg



        # Use of Lambda.
        sum_pos=sum(map(lambda x:x*x,nums[:nums_len]))
        sum_neg=sum(map(lambda x:x*x,nums[nums_len:len(nums)]))
        return sum_pos-sum_neg