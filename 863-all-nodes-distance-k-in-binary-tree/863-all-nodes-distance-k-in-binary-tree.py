# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        parentMap = {root: None}
        queue = [root]
        
        while queue:
            node = queue.pop(0)
            if node.left != None:
                queue.append(node.left)
                parentMap[node.left] = node
            if node.right != None:
                queue.append(node.right)
                parentMap[node.right] = node
        
        visited = {target: True}
        queue = [(target, 0)]
        ans = []
        while queue:
            node, dist = queue.pop(0)
            if dist == k:
                ans.append(node.val)
            if node.left != None:
                if node.left not in visited:
                    queue.append((node.left, dist+1))
                    visited[node.left] = True
            if node.right != None:
                if node.right not in visited:
                    queue.append((node.right, dist+1))
                    visited[node.right] = True
            if node != root and parentMap[node] not in visited:
                queue.append((parentMap[node], dist+1))
                visited[parentMap[node]] = True
            
        return ans
            
            