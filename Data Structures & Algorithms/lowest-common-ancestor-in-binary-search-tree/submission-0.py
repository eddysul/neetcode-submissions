# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # if there is a split, where p and q are in different subtrees, the root or where the split happens is the lca
        # if both are less than root or cur value look left
        # if both are greater, look right subtree
        # edge case: where one node is equal to root node
        # if its equal, return that node
        # we are guaranteed to find our result, b/c p and q are guaranteed to be in tree, so at most its the root
        cur = root
        
        while cur:
            if p.val > cur.val and q.val > cur.val:
                cur = cur.right
            elif p.val < cur.val and q.val < cur.val:
                cur = cur.left
            else: # guaranteed to fall here, b/c this covers either cur equals the LCA or is a split
                return cur
