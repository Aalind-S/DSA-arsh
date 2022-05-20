class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        
        
        while head is not None and head.val == val:
            head = head.next
        ptr = head
        while ptr:
            if ptr.next and ptr.next.val == val:
                ptr.next = ptr.next.next
            else:
                ptr = ptr.next
        return head
