/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
class Solution {
    public List<Integer> distanceK(TreeNode root, TreeNode target, int k) {
        Map<TreeNode, TreeNode> parentMap = new HashMap<>();
        Map<TreeNode, Boolean> visited = new HashMap<>();
        List<TreeNode> queue = new ArrayList<>();
        queue.add(root);
        while(queue.size() != 0) {
            TreeNode node = queue.remove(0);
            if(node.left != null) {
                queue.add(node.left);
                parentMap.put(node.left, node);
            }
            if(node.right != null) {
                queue.add(node.right);
                parentMap.put(node.right, node);
            }
        }
        
        int dist = 0;
        List<TreeNode> newqueue = new ArrayList<>();
        newqueue.add(target);
        visited.put(target, true);
        while(!newqueue.isEmpty()) {
            int size = newqueue.size();
            if(dist == k)
                break;
            
            dist++;
            for(int i=0; i< size; i++) {
                TreeNode node = newqueue.remove(0);
                if(node.left != null && visited.get(node.left) == null) {
                    newqueue.add(node.left);
                    visited.put(node.left, true);
                }
                if(node.right != null && visited.get(node.right) == null) {
                    newqueue.add(node.right);
                    visited.put(node.right, true);
                }
                if(parentMap.get(node) != null && visited.get(parentMap.get(node)) == null) {
                    newqueue.add(parentMap.get(node));
                    visited.put(parentMap.get(node), true);
                }                    
            }
        }
        List<Integer> res = new ArrayList<>();
        for(TreeNode node: newqueue)
            res.add(node.val);
        
        return res;
    }
}