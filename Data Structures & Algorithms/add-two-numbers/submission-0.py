# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # Approach 1 Brute Force
        # Iterate l1 and get total
        # Iterate l2 and get total
        
        d1 = 0
        n1 = 0
        while l1:
           n1 += l1.val * 10**d1
           l1 = l1.next
           d1 += 1
        
        d2 = 0
        n2 = 0
        while l2:
            n2 += l2.val * 10**d2
            l2 = l2.next
            d2 += 1
        
        target = n1+n2

        target_node = ListNode(0)
        res = target_node
        str_target = str(target)
        for char in reversed(str_target):
            node = ListNode(int(char))
            target_node.next = node
            target_node = target_node.next
        return res.next
        
        



