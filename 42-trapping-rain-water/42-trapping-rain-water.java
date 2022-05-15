class Solution {
    public int trap(int[] height) {
        int n = height.length;
        int[] left = new int[n];
        int[] right = new int[n];
        int maxSoFar = height[0];
        left[0] = maxSoFar;
        for(int val: height)
            System.out.print(val + " ");
        System.out.print("\n");
            
        for(int i=1; i<n; i++) {
            left[i] = Math.max(maxSoFar, height[i]);
            System.out.print(left[i] + " ");
            maxSoFar = left[i];
        }
        maxSoFar = height[n-1];
        right[n-1] = height[n-1];
        for(int i=n-2; i>=0; i--) {
            right[i] = Math.max(maxSoFar, height[i]);
            maxSoFar = right[i];
        }
        
        System.out.print("\n");
        
        for(int val: right)
            System.out.print(val + " ");
        
//         for(int val: left)
//             System.out.println(val);
        int res = 0;
        for(int i=0; i<n; i++)
            res += (Math.min(left[i], right[i]) - height[i]);
        
        return res;
    }
}