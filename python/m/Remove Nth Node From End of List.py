class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head.next == None:
            return None
        back = front = head
        while(front.next != None):
            front = front.next
            if n != 0:
                n -= 1
            else:
                back = back.next
        if n != 0:
            head = head.next
        else:
            back.next = back.next.next
        
        return head