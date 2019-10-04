// https://leetcode.com/problems/get-equal-substrings-within-budget/

class Solution {
    public int equalSubstring(String s, String t, int maxCost) {
        int[] dp = new int[s.length()];
        for (int j = 0; j < s.length(); j++) {
            int cost = Math.abs(s.charAt(j) - t.charAt(j));
            dp[j] = cost;
        }
        int maxLength = 0;
        int length = 0;
        int cumulativeCost = 0;
        int i = 0;
        for (int j = 0; j < s.length(); j++) {
            cumulativeCost += dp[j];
            length = j-i+1;
            if (cumulativeCost <= maxCost && length > maxLength) {
                maxLength = length;
            } else {
                while (i <= j && cumulativeCost > maxCost) {
                cumulativeCost -= dp[i++];                    
                }
            }
        }
        return maxLength;
    }
}