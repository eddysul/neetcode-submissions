# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Key is to find a linear, efficient way of finding nth node from end
        
        count = 0
        curr = head
        while curr:
            curr = curr.next
            count += 1
        
        dummy = ListNode(0, head)
        ptr = dummy
        target = count - n
        while target > 0:
            ptr = ptr.next
            target -= 1

        print(ptr.val)
        ptr.next = ptr.next.next
        return dummy.next