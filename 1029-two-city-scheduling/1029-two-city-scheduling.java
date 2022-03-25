class Solution {
    public int twoCitySchedCost(int[][] costs) {
        Arrays.sort(costs, new ProfitComparator());
        int ans = 0;
        for(int i=0; i<costs.length; i++) {
            if(i < costs.length/2) {
                ans += costs[i][0];
            }
            else {
                ans += costs[i][1];
            }
        }
        return ans;
    }
    
    public class ProfitComparator implements Comparator<int[]> {
    @Override
    public int compare(int[] one, int[] two) {
        int profit1 = one[1]-one[0];
        int profit2 = two[1]-two[0];
        
        return profit2 - profit1;
    }
}
}

