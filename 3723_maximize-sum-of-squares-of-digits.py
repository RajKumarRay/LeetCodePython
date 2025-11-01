# Question Link:
# https://leetcode.com/problems/maximize-sum-of-squares-of-digits/


class Solution:
    def maxSumOfSquares(self, num: int, sum_val: int) -> str:
        max_val=0
        flag=0
        # for i in range(0,num):
        #     max_val+=9
        #     if max_val>=sum_val:
        #         flag=1
        #         break

        # strs=""
        # for i in range(0,num):
        #     minm=min(9,sum_val)
        #     strs+=str(minm)
        #     sum_val-=minm
        # return strs
        
        max_val=max(map(lambda i:9*(i+1),range(num)))
        if max_val>=sum_val:
                flag=1
        if flag==0:
            return ""

        strs1=str(min(9, sum_val))
        strs=[str(min(9, sum_val := sum_val - min(9, sum_val)))
                for _ in range(num-1)]
        strs1+=''.join(strs)
        return strs1


