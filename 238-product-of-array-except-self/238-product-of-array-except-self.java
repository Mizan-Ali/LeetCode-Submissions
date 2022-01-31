class Solution {
    public int[] productExceptSelf(int[] nums) {
        int[] ans = new int[nums.length];
        int product = 1;
        int n = nums.length;
        for(int i=0; i<n; i++) {
            if(i==0) {
                ans[i] = nums[i];
                continue;
            }
            ans[i] = ans[i-1] * nums[i];
        }
        for(int a: ans) {
            System.out.print(a + " ");
        }
        product = 1;
        for(int i=n-1; i>0; i--) {
            ans[i] = ans[i-1] * product;
            product *= nums[i];
        }
        ans[0] = product;
        return ans;
    }
}