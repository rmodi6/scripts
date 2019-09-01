// https://leetcode.com/problems/champagne-tower/

class Solution {
    public static double champagneTower(int poured, int query_row, int query_glass) {
        double[][] dp = new double[query_row + 1][query_glass + 1];
        dp[0][0] = poured;
        for(int i = 1; i <= query_row; i++) {
            for(int j = 0; j <= i && j <= query_glass; j++) {
                dp[i][j] = overflow(dp, i-1, j-1, query_glass) + overflow(dp, i-1, j, query_glass);
            }
        }
        return dp[query_row][query_glass] < 1 ? dp[query_row][query_glass] : 1.0;
    }

    public static double overflow(double[][] dp, int i, int j, int query_glass) {
        if(j < 0 || j > i) return 0.0;
        double value = (dp[i][j]-1)/2.0;
        return value < 0 ? 0.0 : value;
    }

    public static void main(String[] args) {
        System.out.println(champagneTower(10, 3, 1));
    }
}