class Solution {
    public int sumOfBeauties(int[] nums) {
        int n = nums.length;
        int ans = 0;
        int[] prefix_max = new int[n];
        int[] suffix_min = new int[n];
        prefix_max[0] = nums[0];
        suffix_min[n-1] = nums[n-1];
        
        for(int i=1; i<n; i++) {
            prefix_max[i] = Math.max(nums[i-1], prefix_max[i-1]);
        }
        for(int i=n-2; i>=0; i--) {
            suffix_min[i] = Math.min(nums[i+1], suffix_min[i+1]);
        }
        
        
        for(int i=1; i<n-1; i++) {
            if(prefix_max[i] < nums[i] && nums[i] < suffix_min[i]) {
                  ans += 2;
            }
            else if(nums[i-1] < nums[i] && nums[i] < nums[i+1]) {
                 ans += 1;
            }
        }
        return ans;       
            
        
    }
}