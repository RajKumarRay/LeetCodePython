# Question Link:
# https://leetcode.com/problems/remove-zeros-in-decimal-representation/description/

class Solution:
    def removeZeros(self, n: int) -> int:
        nstr=str(n)
        nstrp=nstr.replace('0','')
        return int(nstrp)