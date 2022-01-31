class Solution {
    public int maximumWealth(int[][] accounts) {
        int ans=0;
        for(int[] arr: accounts) {
            int temp=0;
            for(int each: arr) {
                temp += each;
            }
            ans = temp>ans?temp:ans;
        }
        return ans;
    }
}