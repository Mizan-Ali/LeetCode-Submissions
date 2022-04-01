class Solution {
    public void moveZeroes(int[] nums) {
        int left = 0, right = 0;
        int n = nums.length;
        for(int i=0; i<n; i++) {
            if(nums[i] == 0) {
                left = i;
                break;
            }
        }
        right = left;
        while(right < n) {
            if(nums[right] == 0) {
                right++;
            }
            else {
                int temp = nums[left];
                nums[left] = nums[right];
                nums[right] = temp;
                
                left++;
                right++;
            }
        }
    }
}