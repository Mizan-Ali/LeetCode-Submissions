class Solution {
    public int maximumUnits(int[][] boxTypes, int truckSize) {
        // sort on the basis of index 1
        Arrays.sort(boxTypes, new Comparator<>() {
            @Override
            public int compare(int[] box1, int[] box2) {
                return box2[1] - box1[1];
            }
        });
        int maxUnits = 0;
        for(int[] box: boxTypes) {
            if(box[0] <= truckSize) {
                truckSize -= box[0];
                maxUnits += (box[0] * box[1]);
            }
            else {
                maxUnits += (truckSize * box[1]);
                truckSize = 0;
            }
            
            if(truckSize == 0)
                break;
        }
        return maxUnits;
    }
}