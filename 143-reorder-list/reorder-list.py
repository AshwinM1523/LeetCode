# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        middle = slow.next
        prev = slow.next = None

        while middle is not None:
            next_node = middle.next
            middle.next = prev
            prev = middle
            middle = next_node

        end = prev

        cur = head
        while end and cur:

            tmp1, tmp2 = cur.next, end.next
            cur.next = end
            end.next = tmp1
            cur, end = tmp1, tmp2
        
        return head