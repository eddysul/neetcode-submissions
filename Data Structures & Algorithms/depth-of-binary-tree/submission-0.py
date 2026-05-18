# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        def dfs(node, depth):
            if not node:
                return depth
            
            left = dfs(node.left, 1 + depth)
            right = dfs(node.right, 1 + depth)

            return max(left, right)

        return dfs(root, 0)
