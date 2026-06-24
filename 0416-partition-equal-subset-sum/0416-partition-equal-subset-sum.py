class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        totalsum=sum(nums);
        if totalsum%2!=0:   return False;
        totalsum//=2;
        n=len(nums);
        # Bottom up approach tabulation + space 
        dp=[[-1]*(totalsum+1) for _ in range(2)];
        for i in range(n+1):
            dp[i%2][0]=1;
        for i in range(1,n+1):
            for j in range(totalsum+1):
                tem=dp[(i-1)%2][j];
                if(j>=nums[i-1]):
                    tem=1 if tem==1 or dp[(i-1)%2][j-nums[i-1]]==1 else 0;
                dp[i%2][j]=tem;
        return True if dp[n%2][totalsum]==1 else False;

        # Bottom up approach tabulation
        # dp=[[-1]*(totalsum+1) for _ in range(n+1)];
        # for i in range(n+1):
        #     dp[i][0]=1;
        # for i in range(1,n+1):
        #     for j in range(totalsum+1):
        #         tem=dp[i-1][j];
        #         if(j>=nums[i-1]):
        #             tem=1 if tem==1 or dp[i-1][j-nums[i-1]]==1 else 0;
        #         dp[i][j]=tem;
        # return True if dp[n][totalsum]==1 else False;


        #Top down approach (memorization)
        # dp=[[-1]*(totalsum+1) for _ in range(n+1)];
        # def helper(i,k)-> bool:
        #     if k==0:
        #         dp[i][k]=1;    
        #         return 1;
        #     if(i==0):   return 0;
        #     if(dp[i][k]!=-1):   return dp[i][k];
        #     tem=helper(i-1,k) #not take
        #     if(nums[i-1]<=k):
        #         tem=1 if tem==1 or helper(i-1,k-nums[i-1])==1 else 0;
        #     dp[i][k]=tem;
        #     return tem;
        # tem=helper(n,totalsum);
        # return True if tem==1 else False;

        # recursion................
        # def helper(i,k)-> bool:
        #     if k==0:    return True;
        #     if(i==0):   return False;
        #     tem=helper(i-1,k) #not take
        #     if(nums[i-1]<=k):
        #         tem=tem or helper(i-1,k-nums[i-1]);
        #     return tem;
        # return helper(n,totalsum)
        
        