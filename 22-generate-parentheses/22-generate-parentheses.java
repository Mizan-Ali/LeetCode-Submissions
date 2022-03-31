class Solution {
    public void generate(ArrayList<String> res, String combination, int left, int right) {
        if(left == 0 && right == 0) {
            res.add(combination);
            return;
        }
        else if(left > right) {
            return;
        }
        if(left > 0) {
            generate(res, combination+"(", left-1, right);
        }
        if(right > 0) {
            generate(res, combination+")", left, right-1);
        }
    }
    
    public List<String> generateParenthesis(int n) {
        ArrayList<String> res = new ArrayList<String>();
        generate(res, "(", n-1, n);
        return res;
    }
}