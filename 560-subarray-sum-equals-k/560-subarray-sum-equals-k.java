class Solution {
    public int subarraySum(int[] nums, int k) {
        int[] sum = new int[nums.length + 1];
        sum[0] = 0;
        int count = 0;
        for(int i=1; i<=nums.length; i++) {
            sum[i] = sum[i-1] + nums[i-1];
        }
        for(int i=0; i<nums.length; i++) {
            for(int j=i+1; j<=nums.length; j++) {
                if((sum[j] - sum[i]) == k) {
                    count += 1;
                }
            }
        }
        return count;
    }
}