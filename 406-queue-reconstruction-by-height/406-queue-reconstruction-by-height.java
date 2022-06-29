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
        List<int[]> res = new LinkedList<>();
        for(int[] curr: people) {
            res.add(curr[1], curr);
        }
        return res.toArray(new int[people.length][]);
    }
}