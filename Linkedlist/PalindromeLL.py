class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        fast = slow = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
        prev = None
        #slow is at the middle
        #reversing the list
        while slow:
            dummy = slow.next
            slow.next = prev
            prev = slow
            slow = dummy
            
        start, mid = head, prev
        while mid:
            if start.val != mid.val:
                return False
            start = start.next
            mid = mid.next
        return True
