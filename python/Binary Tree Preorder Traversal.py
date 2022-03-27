class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        order = []
        if root:
            return self.nodeOrder(root, order)
        else:
            return order
    
    def nodeOrder(self, node, order):
        if node:
            order.append(node.val)
            if node.left:
                self.nodeOrder(node.left, order)
            if node.right:
                self.nodeOrder(node.right, order)
            return order