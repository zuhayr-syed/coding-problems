class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p == None and q == None:
            return True
        elif p == None or q == None:
            return False
        elif p.val == q.val:
            return self.sameNode(p.left, q.left) and self.sameNode(p.right, q.right)
        else:
            return False
    
    def sameNode (self, p, q):
        if (p == None and q == None):
            return True
        elif (p == None or q == None):
            return False
        elif (p.val == q.val):
            return self.sameNode(p.left, q.left) and self.sameNode(p.right, q.right)
        else:
            return False