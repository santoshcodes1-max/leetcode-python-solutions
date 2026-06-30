import math
class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        totalsum=sum(stones);
        target=math.ceil(totalsum/2);
        dp={}
        def dfs(i,total):
            if i==len(stones) or total>=target:
                firststone=total
                secondstone=totalsum-total;
                dp[(i,total)]=abs(firststone-secondstone);
                return dp[(i,total)];
            if (i,total) in dp:
                return dp[(i,total)];
            notPick=dfs(i+1,total);
            pick=dfs(i+1,total+stones[i]);
            dp[(i,total)]=min(pick,notPick);
            return dp[(i,total)]

        return dfs(0,0);
