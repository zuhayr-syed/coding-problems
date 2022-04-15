class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        front = addList = ListNode(0)
        carry = 0
        while(l1 or l2 or carry != 0):
            sums = 0
            if l1:
                sums += l1.val
                l1 = l1.next
            if l2:
                sums += l2.val
                l2 = l2.next
            if carry > 0:
                sums += carry
                carry = 0
            if sums > 9:
                sums -= 10
                carry += 1
            addList.next = ListNode(sums)
            addList = addList.next
        return front.next