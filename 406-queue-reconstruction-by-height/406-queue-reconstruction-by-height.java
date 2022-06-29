class Solution {
    public int[][] reconstructQueue(int[][] people) {
        Arrays.sort(people, new Comparator<int[]>() {
            @Override
            public int compare(int[] a1, int[] a2) {
                if(a1[0] != a2[0]) 
                    return a2[0] - a1[0];
                else
                    return a1[1] - a2[1];
            }
        });
        int[][] res = new int[people.length][2];
        for(int[] curr: people) {
            int idx = curr[1];
            if(res[idx] == new int[2]) {
                res[idx] = curr;
            }
            else {
                // right shift
                int[] temp = res[idx];
                while((idx < res.length-1) && (res[idx] != new int[2])) {
                    int[] temp1 = res[idx+1];
                    res[idx+1] = temp;
                    temp = temp1;
                    idx++;
                }
                res[curr[1]] = curr;
            }
        }
        return res;
    }
}