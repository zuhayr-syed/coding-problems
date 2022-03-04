class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        reverse = tail = head
        if (head == None): 
            return
        else:
            head = head.next
        while (head != None):
            tmp = head.next
            head.next = tail
            tail = head
            head = tmp
        reverse.next = None
        return tail