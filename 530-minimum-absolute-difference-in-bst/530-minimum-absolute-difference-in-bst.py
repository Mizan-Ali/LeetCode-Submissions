# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        global trav
        trav = []
        def solve(node):
            global trav
            if node == None:
                return
            solve(node.left)
            trav.append(node.val)
            solve(node.right)
        solve(root)
        diff = trav[1] - trav[0]
        for i in range(1, len(trav)-1):
            diff = min(diff, trav[i+1] - trav[i])
        return diff