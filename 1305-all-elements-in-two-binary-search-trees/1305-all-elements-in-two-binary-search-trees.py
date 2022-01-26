# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# FIRST APPROACH
class Solution:
    def traverse(self, node, trav):
        if node == None:
            return
        self.traverse(node.left, trav)
        trav.append(node.val)
        self.traverse(node.right, trav)
        
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        trav1, trav2 = [], []
        i, j = 0, 0
        self.traverse(root1, trav1)
        self.traverse(root2, trav2)
        ans = []
        while i < len(trav1) and j < len(trav2):
            if trav1[i] <= trav2[j]:
                ans.append(trav1[i])
                i += 1
            else:
                ans.append(trav2[j])
                j += 1
        while i < len(trav1):
            ans.append(trav1[i])
            i += 1
        while j < len(trav2):
            ans.append(trav2[j])
            j += 1
        return ans
        