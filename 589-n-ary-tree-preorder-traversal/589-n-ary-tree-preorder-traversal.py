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
        trav.append(node.val)
        for child in node.children:
            self.recurse(child, trav)
    def preorder(self, root: 'Node') -> List[int]:
        if root == None:
            return None
        trav = []
        self.recurse(root, trav)
        return trav