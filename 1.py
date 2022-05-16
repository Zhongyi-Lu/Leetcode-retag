class Solution:
    def numTrees(self, n: int) -> int:
        dp = [1] * (n+1)
        for i in range(2, n+1):
            temp = 0
            mid = (i-1)//2
            for j in range(mid+1):
                temp += dp[j]*dp[i-1-j]*2
            if (i-1) % 2 == 0:
                temp -= dp[mid]*dp[mid]
            dp[i] = temp

        return dp[-1]
