class Solution {
    public int numRescueBoats(int[] people, int limit) {
        Arrays.sort(people);
        int i=0, j=people.length-1, c=0;
        
        while(i<=j) {
            if((people[i]+people[j]) <= limit) {
                i++;
                j--;
            }
            else {
                j--;
            }
            c++;
        }
        return c;
    }
}