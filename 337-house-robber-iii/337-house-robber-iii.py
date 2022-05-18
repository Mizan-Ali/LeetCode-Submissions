# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        dp = {}
        def solve(node):
            if node == None:
                return 0
            if node in dp:
                return dp[node]
            skip = solve(node.left) + solve(node.right)
            pick = node.val + g(node.left) + g(node.right)
            
            dp[node] = max(skip, pick)
            return dp[node]
            
        def g(node):
            if node == None:
                return 0
            return solve(node.left) + solve(node.right)
            

        return solve(root)