class Solution {
    public int findKthLargest(int[] nums, int k) {
        PriorityQueue<Integer> pqueue = new PriorityQueue<>(nums.length);
        
        for(int val: nums)
            pqueue.add(-val);
        int ans = 0;
        while(k-1 != 0) {
            pqueue.poll();
            k--;
        }
        return -pqueue.peek();
    }
}