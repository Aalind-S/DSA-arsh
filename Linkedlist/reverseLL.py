class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        prev = None
        while curr: 
            dummy = curr.next
            curr.next = prev
            prev = curr
            curr = dummy
        return prev
