class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def dfs(root, depth):
            if (root):
                return max(dfs(root.left, depth + 1), dfs(root.right, depth + 1))
            else:
                return depth
        return dfs(root, 0)