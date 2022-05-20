class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        def recur(l1, l2):
            if not l1 or not l2:
                return l1 or l2
            if l1.val < l2.val:
                l1.next = recur(l1.next, l2)
                return l1
            else:
                l2.next = recur(l1, l2.next)
                return l2
        return recur(list1, list2)
