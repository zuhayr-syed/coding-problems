class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        traversal = []
        if root:
            return self.nodeTraversal(root, traversal)
        else:
            return traversal
    
    def nodeTraversal(self, node, trav):
        if node:
            self.nodeTraversal(node.left, trav)
            self.nodeTraversal(node.right, trav)
            trav.append(node.val) 
        return trav