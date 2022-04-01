class Solution {
    ArrayList<String> rootToLeaf = new ArrayList<>();
    public void dfs(TreeNode node, String str) {
        if(node == null)
            return;
        if(node.left == null && node.right == null) {
            str += Integer.toString(node.val);
            rootToLeaf.add(str);
            return;
        }
        dfs(node.left, str+Integer.toString(node.val));
        dfs(node.right, str+Integer.toString(node.val));
    }
    public int sumNumbers(TreeNode root) {
        dfs(root, "");
        int ans = 0;
        for(String val: rootToLeaf) 
            ans += Integer.parseInt(val);
        return ans;
    }
}