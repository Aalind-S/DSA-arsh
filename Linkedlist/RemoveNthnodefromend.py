class Solution(object):
    
    def removeNthFromEnd(self, head, n):
        dummy = ListNode(0, head)
        fake = dummy
        counter = 0
        front = head
        
        while counter < n and front:
            front = front.next
            counter += 1
        
        while front:
            front = front.next
            fake = fake.next
        
        fake.next = fake.next.next
        return dummy.next
