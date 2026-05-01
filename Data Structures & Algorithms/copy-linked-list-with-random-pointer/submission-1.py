"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # Can't create a node if its not copied yet. So can't create random pointer as you go
        # Why can't we build a new list while iterating from old list?
        # We can't immediately assign a random pointer's address b/c it might point to a node that hasn't been created yet
        # So we can use a hashmap to store the random pointer's address as it is efficient O(1) look up
        oldToCopy = {None: None}        
        cur = head # ptr for original list

        while cur:
            copy = Node(cur.val)
            oldToCopy[cur] = copy
            cur = cur.next
        
        # Now we have old nodes pointed to copy nodes with only values filled  
        # Time to fill in ptrs

        cur = head
        while cur:
            oldToCopy[cur].next = oldToCopy[cur.next]
            oldToCopy[cur].random = oldToCopy[cur.random]
            cur = cur.next
        
        return oldToCopy[head]
        

        
        
