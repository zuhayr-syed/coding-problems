class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if root1 and root2:
            tree = TreeNode(root1.val + root2.val)
            tree.left = self.mergeTrees(root1.left, root2.left) 
            tree.right = self.mergeTrees(root1.right, root2.right) 
            return tree
        else:
            return root1 or root2