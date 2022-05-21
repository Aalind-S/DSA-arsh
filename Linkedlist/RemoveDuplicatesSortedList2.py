class Solution:
    def deleteDuplicates(self, head):
        fake = ListNode(0, head)
        prev = fake
        curr = head
        while curr:
            if curr.next and curr.val == curr.next.val:
                while curr.next and curr.val == curr.next.val:
                    curr = curr.next
                    prev.next = curr.next
            else:
                prev = prev.next
            curr = curr.next
        return fake.next
