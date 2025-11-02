# Question
# https://leetcode.com/problems/maximum-product-of-three-elements-after-one-replacement/


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        count_zero=sum([1 for i in nums if i==0 ])
        num_len=len(nums)
        if count_zero > num_len-2 :
            return 0

        new_nums=[abs(i) for i in nums]
        new_nums.sort(reverse=True)
        new_nums=new_nums[:2]
        return new_nums[0]*new_nums[1]*100000
        




