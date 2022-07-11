from collections import defaultdict

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # level order traversal, save the last element in each level
        if root == None:
            return None
        
        levelOrder = defaultdict(list)
        queue = [(root, 0)]
        
        while queue:
            node, level = queue.pop(0)
            levelOrder[level].append(node.val)
            
            if node.left != None:
                queue.append((node.left, level+1))
            if node.right != None:
                queue.append((node.right, level+1))
                
        ans = []
        for level in levelOrder:
            ans.append(levelOrder[level][-1])
        return ans