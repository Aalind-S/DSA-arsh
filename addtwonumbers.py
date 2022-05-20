class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        answer = ListNode()
        node = answer
        carry = 0
        #new LL to store our answer
        # node pointing to answer
        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0
            
            total = v1 + v2 + carry
            value = total%10
            
            carry = total // 10
            node.next = ListNode(value)
            node = node.next
            
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        
        return answer.next
        
            
