class Solution {
public:
    int minEatingSpeed(vector<int>& piles, int h) {
        int left = 1, right = *max_element(piles.begin(), piles.end());
        while(left != right) {
            int mid = (left+right)/2;
            int hours = 0;
            for(auto pile: piles) {
                hours += pile / mid + (pile % mid != 0);
            }
            if(hours <= h) {
                right = mid;
            }
            else {
                left = mid+1;
            }
        }
        return left;
    }
};