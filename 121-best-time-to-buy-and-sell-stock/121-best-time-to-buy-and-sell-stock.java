class Solution {
    public int maxProfit(int[] prices) {
        int minsofar = Integer.MAX_VALUE, maxsofar = Integer.MIN_VALUE;
        for(int i=0; i<prices.length; i++) {
            minsofar = minsofar > prices[i] ? prices[i] : minsofar;
            maxsofar = prices[i] - minsofar > maxsofar ? prices[i] - minsofar: maxsofar;
        }
        return maxsofar;
    }
}