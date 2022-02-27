# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict
# We just have to find the deepest level(n) and apply formula 2**n 
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        hmap = defaultdict(list)
        def traverse(node):
            queue = [(root, 0, 0)] # (node, level, index)
            while queue:
                node, level, idx = queue.pop(0)
                hmap[level].append(idx)
                
                if node.left == None and node.right == None:
                    continue
                if node.left != None and node.right == None:
                    queue.append((node.left, level+1, 2*idx+1))
                if node.right != None and node.left == None:
                    queue.append((node.right, level+1, 2*idx+2))
                if node.left != None and node.right != None:
                    queue.append((node.left, level+1, 2*idx+1))
                    queue.append((node.right, level+1, 2*idx+2))
            # print(hmap)
        traverse(root)
        return max([hmap[i][-1]-hmap[i][0] for i in hmap]) + 1