# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        
        i = 1
        curr = head
        prevLeft = None

        # Move curr to the left node
        while i < left:
            prevLeft = curr
            curr = curr.next
            i += 1

        leftNode = curr

        # Find node after right
        while i < right:
            curr = curr.next
            i += 1

        postRight = curr.next

        # Reverse from leftNode up to postRight
        curr = leftNode
        prev = postRight

        while curr != postRight:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp

        # Connect left side to reversed section
        if prevLeft:
            prevLeft.next = prev
        else:
            head = prev

        return head

