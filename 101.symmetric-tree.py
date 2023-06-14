#
# @lc app=leetcode id=101 lang=python3
#
# [101] Symmetric Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    # function that gets the left and right of the root and continues down
    def isMirror(self, left, right):
        # if both are none (symmetric)
        if not left and not right:
            return True
        # if one is none (not symmetric)
        if not left or not right:
            return False
        # if both are numbers, check if equal and do the same process for left and right
        return left.val == right.val and self.isMirror(left.left, right.right) and self. isMirror(left.right, right.left)


    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        # reutrn the function that will go recursivly and check for the equality of same place nodes
        return self.isMirror(root.left, root.right)
        
        
        
# @lc code=end

