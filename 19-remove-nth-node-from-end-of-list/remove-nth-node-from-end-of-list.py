class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        length = 0
        curr = head

        while curr:
            length += 1
            curr = curr.next
        
        # We're removing the first node
        if length == n:
            return head.next
        
        i = 0
        curr = head
        prev = None

        while i != length - n:
            i += 1
            prev = curr
            curr = curr.next
        
        prev.next = curr.next
        
        return head