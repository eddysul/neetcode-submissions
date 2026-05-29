# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # in tree level order traversal, when visiting a node, we add its children in the queue
        res = []
        
        if not root:
            return res
        
        q = deque([root])


        while q:
            level = len(q)
            levelNodes = []

            for i in range(level):
                current = q.popleft()
                levelNodes.append(current.val)
            
                print(current.val)
                
                if current.left:
                    q.append(current.left)
                if current.right:
                    q.append(current.right)

            res.append(levelNodes)

        print(res)
        return res


       
