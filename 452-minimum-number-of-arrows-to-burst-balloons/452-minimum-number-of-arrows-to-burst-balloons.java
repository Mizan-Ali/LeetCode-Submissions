class Solution {
    public int findMinArrowShots(int[][] points) {
        // sort in ascending order and check how many of them overlap
        Arrays.sort(points, new Comparator<int[]>() { 
            @Override
            public int compare(int[] a1, int[] a2) {
                if(a1[1] > a2[1]) 
                    return 1;
                else if(a1[1] < a2[1])
                    return -1;
                else {
                    if(a1[0] > a2[0])
                        return 1;
                    else if(a1[0] < a2[0])
                        return -1;
                    else 
                        return 0;
                }
            }
        });
        int n = points.length;
        int count = 1;
        int end = points[0][1];
        for(int i=1; i<n; i++) {
            if(points[i][0] > end) {
                count++;
                end = points[i][1];
            }
            else {
                // do nothing
            }
        }
        return count;
    }
}