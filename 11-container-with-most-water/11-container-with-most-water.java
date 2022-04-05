class Solution {
    public int maxArea(int[] height) {
        int p1 = 0, p2 = height.length-1;
        int maxArea = 0;
        while(p1 < p2) {
            maxArea = Math.max(maxArea, Math.min(height[p1], height[p2]) * (p2 - p1));
            
            if(height[p1] <= height[p2]) 
                p1++;
            else
                p2--;
        }
        return maxArea;
    }
}