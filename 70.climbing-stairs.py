#
# @lc app=leetcode id=70 lang=python3
#
# [70] Climbing Stairs
#

# @lc code=start
class Solution:
    def climbStairs(self, n: int) -> int:

        one,two=1,1
        for i in range(n-1):
            temp=one+two
            one=two
            two=temp
        return two



# take 3 as example 
# (i) in for loop will go 0,1,2
# one = 1  1  2
# two = 1  2  3 (last digit here will be the number of steps always)
#temp = 2  3  5
        
# @lc code=end

