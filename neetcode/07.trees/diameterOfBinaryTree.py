# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = 0
        
        def dfs(root):
            # Treat null node with height -1
            if not root:
                return -1
            
            nonlocal res
            left, right = dfs(root.left), dfs(root.right)
            
            # Diameter cal = left height + right height + 2 edges from each child to root
            # Store the current max diameter in 
            res = max(res, left + right + 2)
            
            # Calculate the height at root
            return 1 + max(left, right)
        
        dfs(root)
        return res