class Solution {
    public int findMaxConsecutiveOnes(int[] nums) {
        int max_length = 0;
        int current_ones = 0;
        
        for (int num : nums){
            if (num == 1) {
                current_ones += 1;
                max_length = Math.max(max_length, current_ones);                
            }
            else {
                current_ones = 0;
            }
        }
        
        return max_length;
        
    }
}
