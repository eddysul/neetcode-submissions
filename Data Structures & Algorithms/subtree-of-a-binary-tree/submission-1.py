# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # Essentially when you find the node in main Root that matches head of subRoot, you perform isSameTree
        
        def dfs(root):
            if not root:
                print(f"No matching root")
                return False

            if root.val == subRoot.val and isSameTree(root, subRoot):
                print(f"Found target: Root -> {root.val}, Subroot: {subRoot.val}")
                return True

            left = dfs(root.left)
            right = dfs(root.right)
            return left or right

        def isSameTree(p, q):
            if not p and not q:
                return True
            
            if not p or not q:
                return False
            
            if p.val != q.val:
                return False
            
            left = isSameTree(p.left, q.left)
            right = isSameTree(p.right, q.right)
        
            return left and right
        
        return dfs(root)
        
        
