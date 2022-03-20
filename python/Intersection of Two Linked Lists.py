class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        p1 = headA
        p2 = headB
        
        if (p1 == None or p2 == None):
            return None
        
        while (p1 != p2):
            if (p1.next == None):
                p1 = headB
            else:
                p1 = p1.next
            if (p2.next == None):
                p2 = headA
            else:
                p2 = p2.next
                
        return p1