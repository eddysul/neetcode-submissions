# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # This involves BFS or DFS traversal simultaneously
        # We are passing information DOWN as we go
        # We pass boolean checking if values are same
        if not p and not q:
            print(f"Both p and q are null")
            return True
        
        if not p or not q:
            print(f"P: {p.val if p else 'None'}, Q: {q.val if q else 'None'}")
            return False

        if p.val != q.val:
            print(f"P: {p.val} and Q: {q.val} are not equal")
            return False

        left = self.isSameTree(p.left, q.left)
        right = self.isSameTree(p.right, q.right)

        print(f"Left: {p.val}, Right: {q.val}")

        return left and right