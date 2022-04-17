# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        stack = []
        dummy = TreeNode()
        curr = dummy
        
        while len(stack) != 0  or root != None:
            while root != None:
                stack.append(root)
                root = root.left
            root = stack.pop()
            curr.right = root
            
            curr = root
            root = root.right
            
            curr.left = None
        return dummy.right
                