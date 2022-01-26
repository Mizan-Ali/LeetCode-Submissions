# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# FIRST APPROACH
class Solution:
    def traverse(self, node):
        global trav
        if node == None:
            return
        self.traverse(node.left)
        trav.append(node.val)
        self.traverse(node.right)
        
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        global trav
        trav = []
        self.traverse(root1)
        print(trav)
        self.traverse(root2)
        # trav = sorted(trav, key=lambda x: x.val)
        return sorted(trav)