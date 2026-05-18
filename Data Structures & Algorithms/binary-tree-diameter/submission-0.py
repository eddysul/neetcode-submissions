# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        maxDiameter = 0

        def getHeight(node, depth=0):
            nonlocal maxDiameter
            indent = "  " * depth

            if not node: # Base Case: we hit bottom of a branch 
                print(f"{indent} -> Hit Base Case (None): returning 0")
                return 0
            
            print(f"{indent} Entering Node {node.val}")
            # 1. Ask children for their straight line heights (moving UP)
            left = getHeight(node.left)
            right = getHeight(node.right)

            # 2. Sideways Tracker: Check if bent path breaks record
            maxDiameter = max(maxDiameter, left+right)
            print(f"Max Diameter: {maxDiameter}")

            print(f"{indent} Exiting node {node.val}: left={left}, right={right}")

            # 3. Pass our own straight-line height up to parent (UP)
            return 1 + max(left, right)
        
        getHeight(root)
        return maxDiameter
        
