class Solution {
    public int findKthLargest(int[] nums, int k) {
        PriorityQueue<Integer> pqueue = new PriorityQueue<>(nums.length);
        
        for(int val: nums)
            pqueue.add(-val);
        int ans = 0;
        while(k != 0) {
            ans = pqueue.poll();
            k--;
        }
        return -ans;
    }
}