class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(root):
            if (root):
                tmp = TreeNode(0)
                tmp = root.right
                root.right = root.left
                root.left = tmp
                dfs(root.left)
                dfs(root.right)
            else:
                return
        dfs(root)
        return root