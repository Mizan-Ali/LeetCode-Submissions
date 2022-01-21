class Solution {
    public int canCompleteCircuit(int[] gas, int[] cost) {
        int sumG = 0, sumC = 0;
        for(int i = 0; i < gas.length; i++) {
            sumG += gas[i];
            sumC += cost[i];
        }
        if(sumG < sumC) return -1;
        int total = 0, res = 0;
        for(int i=0; i<gas.length; i++) {
            total += gas[i] - cost[i];
            if(total < 0) {
                total = 0;
                res = i + 1;
            }
        }
        return res;
    }
}