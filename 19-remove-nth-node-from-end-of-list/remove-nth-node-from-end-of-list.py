# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        length = 0
        curr = head
        while curr != None:
            length += 1
            curr = curr.next

        count = length - n

        if count == 0:
            return head.next

        curr = head
        prev = None
        while count > 0:
            count -= 1
            prev = curr
            curr = curr.next

        prev.next = curr.next

        return head

        

