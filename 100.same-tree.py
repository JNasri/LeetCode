#
# Solution using Recursion
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        # if p and q are both none (equal) 
        if not p and not q:
            return True
        # if only one of them is none (not equal)
        if not p or not q:
            return False
        # if both not none but the value isn't the same (not equal)
        if p.val != q.val:
            return False 

        # go through the same process with the left and right of both trees
        return self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right)

