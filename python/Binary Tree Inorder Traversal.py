class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        traversal = []
        self.nodeTrav(root, traversal)
        return traversal
    
    def nodeTrav(self, node, trav):
        if node:
            self.nodeTrav(node.left, trav)
            trav.append(node.val)
            self.nodeTrav(node.right, trav)
            