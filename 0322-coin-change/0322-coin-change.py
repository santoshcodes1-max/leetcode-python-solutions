class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n=len(coins);
        INF=float('inf');
        #Bottom-Up Approach (Tabulation)+ Space optimizations 
        dp=[[inf]*(amount+1) for _ in range(2)];
        for i in range(n+1):
            dp[i%2][0]=0;
        for i in range(1, n+1):
            for j in range(amount+1):
                tem=dp[(i-1)%2][j];
                if(j>=coins[i-1]):
                    tem=min(tem,dp[i%2][j-coins[i-1]]+1)
                dp[i%2][j]=tem;
        return -1 if dp[n%2][amount]==float('inf')else dp[n%2][amount] ;
        # #Bottom-Up Approach (Tabulation)
        # dp=[[inf]*(amount+1) for _ in range(n+1)];
        # for i in range(n+1):
        #     dp[i][0]=0;
        # for i in range(1, n+1):
        #     for j in range(amount+1):
        #         tem=dp[i-1][j];
        #         if(j>=coins[i-1]):
        #             tem=min(tem,dp[i][j-coins[i-1]]+1)
        #         dp[i][j]=tem;

         #top down Approach (memoization)
        # dp=[[-1]*(amount+1) for _ in range(n+1)];     
        # def solve(i,j):
        #     if j==0:
        #         dp[i][j]=0    
        #         return 0
        #     if i==0:    return float('inf')
        #     if dp[i][j]!= -1:   return dp[i][j]
        #     tem=solve(i-1,j)# not taken
        #     if(j>=coins[i-1]):
        #         tem=min(tem,solve(i,j-coins[i-1])+1);
            
        #     dp[i][j]=tem;
        #     return dp[i][j];
        # solve(n,amount);
   
        # return -1 if dp[n][amount]==float('inf')else dp[n][amount] ;

        