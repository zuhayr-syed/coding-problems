class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        paths = []
        if root:
            return self.nodePaths(root, paths, '')
        else:
            return paths
    
    def nodePaths(self, node, paths, entry):
        entry += str(node.val)
        if node.left:
            self.nodePaths(node.left, paths, entry+'->')
        if node.right:
            self.nodePaths(node.right, paths, entry+'->')
        if not node.left and not node.right:
            paths.append(entry)
        return paths