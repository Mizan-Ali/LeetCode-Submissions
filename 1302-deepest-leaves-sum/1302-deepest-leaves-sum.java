/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public int depth = 0;
    public int maxdepth = 0;
    public int result = 0;
    public void deepestSum(TreeNode node) {
        if (node.left == null && node.right == null) {
            if(depth > maxdepth) {
                maxdepth = depth;
                result = node.val;
            }
            else if(depth == maxdepth) {
                result += node.val;
            }
            return;
        }
        if(node.left != null) {
            depth++;
            deepestSum(node.left);
            depth--;
        }
        if(node.right != null) {
            depth++;
            deepestSum(node.right);
            depth--;
        }
    }
    public int deepestLeavesSum(TreeNode root) {
        deepestSum(root);
        return result;
    }
}