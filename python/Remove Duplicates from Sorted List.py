class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None: 
            return head
        tmp = head
        check = head.val
        while (tmp.next != None):
            if tmp.next.val == check:
                tmp.next = tmp.next.next
            else:
                tmp = tmp.next
                check = tmp.val
        return head