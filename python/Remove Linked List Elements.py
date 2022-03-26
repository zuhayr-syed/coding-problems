class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        if head:
            tmp = head
            while (tmp != None):
                if tmp.val == val:
                    head = tmp.next
                    tmp = tmp.next
                elif tmp.next!= None and tmp.next.val == val:
                    tmp.next = tmp.next.next
                else:
                    tmp = tmp.next
            return head
        else:
            return head