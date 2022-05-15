# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        depth, maxdepth = 0, 0
        ans = 0
        queue = [(root, depth)]
        
        while queue:
            node, depth = queue.pop(0)
            
            if node.left == None and node.right == None:
                if depth > maxdepth:
                    maxdepth = depth
                    ans = node.val
                elif depth == maxdepth:
                    ans += node.val
            if node.left:
                queue.append((node.left, depth+1))
            if node.right:
                queue.append((node.right, depth+1))
        return ans
                