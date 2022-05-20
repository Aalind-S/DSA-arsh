class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        node = head
        res = []
        while node:
            res.append(node.val)
            node = node.next
        num = 0
        N = len(res)
        for i in range(N-1, -1, -1):
            num += res[i]*2**(N - i - 1)
        return num
