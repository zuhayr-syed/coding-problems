class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root == None:
            return True
        else:
            return self.nodeCheck(root.left, root.right)
        
    def nodeCheck(self, left, right):
        if left == None and right == None:
            return True
        elif left == None or right == None:
            return False
        elif left.val == right.val:
            leftCheck = self.nodeCheck(left.left, right.right)
            rightCheck = self.nodeCheck(right.left, left.right)
            return leftCheck and rightCheck
        else:
            return False