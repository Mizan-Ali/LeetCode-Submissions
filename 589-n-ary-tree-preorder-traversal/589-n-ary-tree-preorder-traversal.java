/*
// Definition for a Node.
class Node {
    public int val;
    public List<Node> children;

    public Node() {}

    public Node(int _val) {
        val = _val;
    }

    public Node(int _val, List<Node> _children) {
        val = _val;
        children = _children;
    }
};
*/

class Solution {
    public void recurse(Node node, List<Integer> trav) {
        if(node == null) {
            return;
        }
        trav.add(node.val);
        for(Node child: node.children) {
            recurse(child, trav);
        }
    }
    public List<Integer> preorder(Node root) {
        List<Integer> trav = new ArrayList<Integer>();
        if(root == null) {
            return trav;
        }
        recurse(root, trav);
        return trav;
    }
}