# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # Look at 1 node and its immediate children at each time
        # We want to know eventually heights of left and right subtree
        # So we are passing, returning heights UP
        # When we hit leaf, we get left and right subtree and compare then if True push up
        # At any point if left and right subtrees have different distance we return False
        # Our helper function is for returning height of trees

        # Main function variable should return the boolean of whether tree is balanced or not
        isBalanced = True
        if not root:
            return isBalanced

        def getHeight(node):
            nonlocal isBalanced

            if not node:
                return 0
            
            left = getHeight(node.left)
            right = getHeight(node.right)

            if abs(left-right) > 1:
                isBalanced = False

            return 1+max(left,right)

        getHeight(root)
        return isBalanced
        
        