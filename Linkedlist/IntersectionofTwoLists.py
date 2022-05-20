class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        ptr1, ptr2 = headA, headB
        while ptr1 != ptr2:
            if ptr1:
                ptr1 = ptr1.next
            else:
                ptr1 = headB
            if ptr2:
                ptr2 = ptr2.next
            else:
                ptr2 = headA
                
        return ptr1
