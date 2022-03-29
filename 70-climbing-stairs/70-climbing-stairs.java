class Solution {
    Map<Integer, Integer> dp = new HashMap<>();
    public int climbStairs(int n) {
        if(n == 1 || n == 2) 
            return n;
        if(dp.containsKey(n) == false)
            dp.put(n, climbStairs(n-1) + climbStairs(n-2));
        return dp.get(n);
    }
}