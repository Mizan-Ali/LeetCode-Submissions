# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leaves_sum(self, node):
        if node.left == None and node.right == None:
            if self.depth > self.maxdepth:
                self.maxdepth = self.depth
                self.result = node.val
            elif self.depth == self.maxdepth:
                self.result += node.val
            return
        if node.left:
            self.depth += 1
            self.leaves_sum(node.left)
            self.depth -= 1
        if node.right:
            self.depth += 1
            self.leaves_sum(node.right)
            self.depth -= 1
        
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        self.depth, self.maxdepth, self.result = 0, 0, 0
        self.leaves_sum(root)
        return self.result