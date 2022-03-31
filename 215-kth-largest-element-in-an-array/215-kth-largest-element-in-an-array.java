class Solution {
    public int findKthLargest(int[] nums, int k) {
        PriorityQueue<Integer> pqueue = new PriorityQueue<>(k+1);
        
        for(int val: nums) {
            pqueue.add(val);
            
            if (pqueue.size() > k)
                pqueue.poll();
            
        }
        return pqueue.poll();
        
    }
}