# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # this is recursive, so if left subtree is not BST then whole tree isn't
        # same with right
        # so at each node, we can recursively go left and right to check whether each subtree is recursive or not

        # At node, check if left is less than, check if right is greater than
        # So I believe we can use a dfs approach with pre-order traversal

        # the value we pass back up is whether this specific part of BST is valid or not

        res = True
        left, right = -float("inf"), float("inf")

        def dfs(node, left, right):
            if not node:
                return True
            
            if not (left < node.val < right):
                return False

            
            return dfs(node.left, left, node.val) and dfs(node.right, node.val, right)

        return dfs(root, left, right)


