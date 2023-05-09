#
# My solution with no help (same as LeetCode Solution)
#
#
class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        while val in nums:
            nums.remove(val)

        print(len(nums))
        print(nums)
        return len(nums)

# nums = [0,1,2,2,3,0,4,2]
# val = 2
# Solution().removeElement(nums, val)
                


