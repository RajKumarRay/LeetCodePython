# Question Link:
# https://leetcode.com/problems/find-missing-elements/description/


class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        nums.sort()
        minm=nums[0]
        new_list=[(minm:=j) for i in range(0,len(nums)) if nums[i]>minm for j in range(nums[i-1]+1,nums[i])]
        return new_list

