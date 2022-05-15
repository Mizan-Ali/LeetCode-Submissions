# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        queue = [(root, 0)]
        levelMap = defaultdict(int)
        while queue:
            node, level = queue.pop(0)
            levelMap[level] += node.val
            if node.left:
                queue.append((node.left, level+1))
            if node.right:
                queue.append((node.right, level+1))
        max_level = max(levelMap.keys())
        
        return levelMap[max_level]