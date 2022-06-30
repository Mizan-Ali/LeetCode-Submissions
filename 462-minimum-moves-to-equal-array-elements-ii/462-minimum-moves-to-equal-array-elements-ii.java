class Solution {
    public int minMoves2(int[] nums) {
        int n = nums.length;
        Arrays.sort(nums);
        int mid = n/2;
        int res = 0;
        for(int num: nums)
            res += Math.abs(num - nums[mid]);
        return res;       
    }
}