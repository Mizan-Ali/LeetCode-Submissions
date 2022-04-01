class Solution {
    public int fib(int n) {
        int a = 0;
        int b = 1;
        int ans = 0;
        if(n == 0 || n == 1)
            return n;
        
        for(int i=1; i<n; i++) {
            ans = a + b;
            a = b;
            b = ans;
        }
        return ans;
    }
}