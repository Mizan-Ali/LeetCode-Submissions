class Solution {
    public String kthLargestNumber(String[] nums, int k) {
        // sort on the basis of length
        Arrays.sort(nums, new Comparator<String>() {
            @Override
            public int compare(String s1, String s2) {
                if(s2.length() < s1.length()) {
                    return -1;
                }
                else if(s2.length() > s1.length()) {
                    return 1;
                }
                else {
                    for(int i=0; i<s1.length(); i++) {
                        int s1Val = s1.charAt(i);
                        int s2Val = s2.charAt(i);
                        
                        if(s1Val == s2Val) 
                            continue;
                        else if(s1Val > s2Val) {
                            return -1;
                        }
                        else {
                            return 1;
                        }
                    }
                    return 0;
                }
                    
            }
        });
        
        return nums[k-1];
    }
}