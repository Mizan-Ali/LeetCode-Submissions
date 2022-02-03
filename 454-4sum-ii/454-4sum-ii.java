class Solution {
    public int fourSumCount(int[] nums1, int[] nums2, int[] nums3, int[] nums4) {
        Map<Integer, Integer> hmap = new HashMap<>();
        for(int i: nums1) {
            for(int j: nums2) {
                int sum = i+j;
                if (hmap.containsKey(i+j)) {
                    hmap.put((i+j), hmap.get(i+j)+1);
                }
                else {
                    hmap.put((i+j), 1);
                }
            }
        }
        int c = 0;
        for(int i: nums3) {
            for(int j: nums4) {
                int negative = -(i+j);
                if (hmap.containsKey(negative)) {
                    c += hmap.get(negative);
                }
                    
            }
        }
        return c;
    }
}