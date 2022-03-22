class Solution {
    public String getSmallestString(int n, int k) {
        char[] result = new char[n];
        for(int i=0; i<n; i++)
            result[i] = 'a';
        k -= n;
        
        while(k>0) {
            result[--n] = (char)(Math.min(25, k) + 'a');
            k -= Math.min(25, k);
        }
        return new String(result);
    }
}