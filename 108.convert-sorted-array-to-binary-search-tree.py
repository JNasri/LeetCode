#
# @lc app=leetcode id=108 lang=python3
#
# [108] Convert Sorted Array to Binary Search Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: list[int]) -> Optional[TreeNode]:
        # get the number of elements in the list
        total_nums = len(nums)
        # if its empty return None 
        if not total_nums:
            return None
        # make the root of the current recursion the middle number in the list
        root = total_nums//2
        # return a new TreeNode object with the root being nums[root] and the same function called for the left side of root and right side of root
        return TreeNode(
        nums[root],
        self.sortedArrayToBST(nums[:root]), self.sortedArrayToBST(nums[root + 1 :]))

        
# @lc code=end

