#
# @lc app=leetcode id=104 lang=python3
#
# [104] Maximum Depth of Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # define a depth first saerch function that check each node
        def dfs(root, depth):
            # if node is none, return the depth of this portion of the tree
            if not root: return depth
            # if not none, reurn the max of the same porcess for left and right
            return max(dfs(root.left, depth + 1), dfs(root.right, depth + 1))

        # RETURN the function with given root and start depth of 0
        return dfs(root, 0)
      
# @lc code=end

