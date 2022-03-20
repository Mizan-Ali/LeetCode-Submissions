class Solution {
    public int minDominoRotations(int[] tops, int[] bottoms) {
        int a = tops[0], b = bottoms[0];
        int n = tops.length;
        
        for(int i=1; i < n; i++) {
            if(a != tops[i] && a != bottoms[i]) {
                a = -1;
            }
            if(b != tops[i] && b != bottoms[i]) {
                b = -1;
            }
        }
        if(a == -1 && b == -1) 
            return -1;
        
        Integer ans1 = Integer.MAX_VALUE;
        Integer ans2 = Integer.MAX_VALUE;
        if(a != -1) {
            int topC=0, bottomC=0;
            for(int i=0; i<n; i++) {
                if(tops[i] == a) 
                    topC++;
                if(bottoms[i] == a)
                    bottomC++;
            }
            ans1 = n - Math.max(topC, bottomC);
        }
        if(b != -1) {
            int topC=0, bottomC=0;
            for(int i=0; i<n; i++) {
                if(tops[i] == b) 
                    topC++;
                if(bottoms[i] == b)
                    bottomC++;
            }
            ans2 = n - Math.max(topC, bottomC);
        }
        return Math.min(ans1, ans2);
    }
}