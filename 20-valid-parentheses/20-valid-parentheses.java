class Solution {
    public boolean isValid(String s) {
        List<Character> stack = new ArrayList<>();
        
        for(int i=0; i<s.length(); i++) {
            if(stack.size() == 0) {
                stack.add(s.charAt(i));
                continue;
            }
            char top = stack.get(stack.size()-1);
            if(s.charAt(i) == ')') {
                if(top == '(') {
                    stack.remove(stack.size()-1);
                }
                else {
                    stack.add(s.charAt(i));
                }
            }
            else if(s.charAt(i) == ']') {
                if(top == '[') {
                    stack.remove(stack.size()-1);
                }
                else {
                    stack.add(s.charAt(i));
                }
            }
            else if(s.charAt(i) == '}') {
                if(top == '{') {
                    stack.remove(stack.size()-1);
                }
                else {
                    stack.add(s.charAt(i));
                }
            }
            else {
                stack.add(s.charAt(i));
            }
        }
        if(stack.size() == 0) {
            return true;
        }
        else {
            return false;
        }
    }
}
