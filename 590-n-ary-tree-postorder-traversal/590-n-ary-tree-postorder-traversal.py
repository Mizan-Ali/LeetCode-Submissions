"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def recurse(self, node, trav):
        if node == None:
            return
        for child in node.children:
            self.recurse(child, trav)
        trav.append(node.val)
    def postorder(self, root: 'Node') -> List[int]:
        if root == None:
            return None
        trav = []
        self.recurse(root, trav)
        return trav