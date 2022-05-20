def multiplyTwoList(head1, head2):
    # Code here
    num1 = num2 = 0
    slow , fast = head1, head2
    while slow:
        num1 = 10*num1 + slow.data
        slow = slow.next
    while fast:
        num2 = 10*num2 + fast.data
        fast = fast.next
    return (num1*num2)%MOD
