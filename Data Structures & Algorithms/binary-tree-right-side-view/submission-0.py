# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # Base Case
        res = []
        if not root:
            return res

        q = deque()
        q.append(root)

        while q:
            # Get length of current level
            qlen = len(q)
            level = []

            # iterate through each level
            for i in range(qlen):
                current = q.popleft()
                level.append(current.val)

                if current.left:
                    q.append(current.left)
                if current.right:
                    q.append(current.right)
                       
            res.append(level[-1])
        return res

        
