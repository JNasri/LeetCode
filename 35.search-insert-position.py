#
# My solution with no help (same as LeetCode Solution)
#
#
class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:

        # if we found the target, return its index
        if target in nums:
            return nums.index(target)
        # if not, add it, sort it, and return its index 
        else:
            nums.append(target)
            nums.sort()
            return nums.index(target)





        


