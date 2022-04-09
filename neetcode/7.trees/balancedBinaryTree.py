# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # Naive way
        # O(n) * n = O(n^2)
        """
        def calHeight(root):
            if not root:
                return 0
            return 1 + max(calHeight(root.left), calHeight(root.right))
        
        if not root:
            return True
        leftHeight = calHeight(root.left)
        rightHeight = calHeight(root.right)
        return abs(leftHeight - rightHeight) <= 1 and self.isBalanced(root.left) and self.isBalanced(root.right)
        """
        
        # Using DFS, calculate height as the same time
        def dfs(root):
            if not root:
                return [True, 0]
            
            left, right = dfs(root.left), dfs(root.right)
            isBalanced = left[0] and right[0] and abs(left[1] - right[1]) <= 1
            return [isBalanced, 1 + max(left[1], right[1])]
        
        return dfs(root)[0]