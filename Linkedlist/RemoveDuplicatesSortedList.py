class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        #will keep track of slow and slow.next
        #and check for the values
        while slow and slow.next:
            if slow.val == slow.next.val:
                slow.next = slow.next.next
                continue
            slow = slow.next
        return head
