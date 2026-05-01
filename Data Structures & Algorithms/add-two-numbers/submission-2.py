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
        
        # Approach 2: Create nodes as you add (so as you go)
        # Keys
            # Get the sum of both 
            # sum // 10 is carry -> add to next sum
            # sum % 10 is rem -> create node
        # Repeat until there is no more node in either l1 or l2 or carry = 0

        sum_node = ListNode(0)
        dummy = sum_node

        carry = 0
        while l1 or l2 or carry:
            l1_val = l1.val if l1 else 0
            l2_val = l2.val if l2 else 0
            total = l1_val + l2_val + carry
            carry = total // 10
            rem = total % 10

            print(f"Total: {total}, Carry: {carry}, Rem: {rem}")

            node = ListNode(rem)
            dummy.next = node
            dummy = dummy.next

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        print(dummy.val)
        
        return sum_node.next
        
    


