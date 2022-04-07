class Solution {
    public int lastStoneWeight(int[] stones) {
        PriorityQueue<Integer> heap = new PriorityQueue<Integer>(Collections.reverseOrder());
        for(int val: stones)
            heap.add(val);
        
        while(heap.size() >=2 ) {
            int y = heap.poll();
            int x = heap.poll();
            // System.out.println(y + " " + x);
            if(x == y)
                continue;
            else {
                heap.add(y - x);
            }
        }
        if(heap.size() == 1) {
            return heap.poll();
        }
        return 0;
    }
}


