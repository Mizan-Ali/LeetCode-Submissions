class Solution {
    List<List<Integer>> ans = new ArrayList<>();
    
    public void solve(int idx, int[] nums, ArrayList<Integer> partial) {
        if(idx == nums.length) {
            ans.add(new ArrayList(partial));
            return;
        }
        // pick
        partial.add(nums[idx]);
        solve(idx+1, nums, partial);
        partial.remove(partial.size()-1);
        
        // skip
        solve(idx+1, nums, partial);
    }
    
    public List<List<Integer>> subsets(int[] nums) {
        solve(0, nums, new ArrayList<Integer>());
        return ans;
    }
}