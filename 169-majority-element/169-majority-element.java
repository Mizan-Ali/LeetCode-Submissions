import java.util.Map.Entry;
class Solution {
    public int majorityElement(int[] nums) {
        float n = nums.length;
        Map<Integer, Integer> count = new HashMap<>();
        
        for(int val: nums) {
            if(count.containsKey(val)) {
                count.put(val, count.get(val)+1);
                if(count.get(val) >= n/2) {
                    return val;
                }
            }
            else {
                count.put(val, 1);
            }
        }
        for(Entry<Integer, Integer> keyval: count.entrySet()) {
            // System.out.println(keyval.getKey() + " : " + keyval.getValue());
            if(keyval.getValue() >= n/2) {
                return keyval.getKey();
            }
        }
        return 0;
    }
}